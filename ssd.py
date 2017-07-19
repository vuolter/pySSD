# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

from os.path import dirname, expanduser, ismount, realpath, splitdrive


def _fullpath(path):
    return realpath(expanduser(path))


def _mountpoint(path):
    head = dirname(_fullpath(path))
    while not ismount(head):
        head = dirname(head)
    return head


def _blkdevice(path):
    import psutil

    partitions = psutil.disk_partitions()
    mount = _mountpoint(path)

    # if os.name == 'nt':
        # mount = mount.upper()

    device = next(dp.device for dp in partitions if dp.mountpoin == mount)
    block = device.rsplit('/', 1)[-1]

    return block


def is_nt_ssd(path):
    import win32file

    flag = False

    path = _fullpath(path)
    drive = splitdrive(path)[0].upper()

    drivetype = win32file.GetDriveType(drive)

    if drivetype == win32file.DRIVE_RAMDISK:
        flag = True

    elif drivetype in (win32file.DRIVE_FIXED, win32file.DRIVE_REMOVABLE):
        import wmi

        c = wmi.WMI()
        phy_to_part = 'Win32_DiskDriveToDiskPartition'
        log_to_part = 'Win32_LogicalDiskToPartition'
        index = dict((log_disk.Caption, phy_disk.Index)
                     for phy_disk in c.Win32_DiskDrive()
                     for partition in phy_disk.associators(phy_to_part)
                     for log_disk in partition.associators(log_to_part))

        c = wmi.WMI(moniker='//./ROOT/Microsoft/Windows/Storage')
        flag = bool(c.MSFT_PhysicalDisk(DeviceId=str(index[drive]),
                                        MediaType=4))

    return flag


def is_osx_ssd(path):
    import subprocess

    block = _blkdevice(path)
    cmd = 'diskutil info {0} | grep "Solid State"'.format(block)
    try:
        out = subprocess.check_output(cmd)
        flag = 'y' in out.lower()

    except subprocess.CalledProcessError:
        flag = False

    return flag


def is_posix_ssd(path):
    block = _blkdevice(path)
    path = '/sys/block/{0}/queue/rotational'.format(block)
    try:
        with open(path) as fp:
            flag = bool(fp.read().strip())

    except (IOError, OSError):
        flag = False

    return flag


def is_ssd(path):
    if os.name == 'nt':
        _is_ssd = is_nt_ssd
    elif sys.platform == 'darwin':
        _is_ssd = is_osx_ssd
    else:
        _is_ssd = is_posix_ssd

    return _is_ssd(path)
