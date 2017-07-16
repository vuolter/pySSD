pySSD
=====

A tiny, but effective, SSD checker for Python.

Working on Windows, macOS and linux.


Table of contents
-----------------

- [Status](#status)
- [Installation](#installation)
- [Usage](#usage)


Status
------

[![Travis Build Status](https://travis-ci.org/vuolter/pySSD.svg?branch=master)](https://travis-ci.org/vuolter/pySSD)
[![Requirements Status](https://requires.io/github/vuolter/pySSD/requirements.svg?branch=master)](https://requires.io/github/vuolter/pySSD/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6ee47c32da944cbcac211ac3ac4ddff2)](https://www.codacy.com/app/vuolter/pySSD?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vuolter/pySSD&amp;utm_campaign=Badge_Grade)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/vuolter/pySSD/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/vuolter/pySSD/?branch=master)

[![PyPI Status](https://img.shields.io/pypi/status/ssd.svg)](https://pypi.python.org/pypi/ssd)
[![PyPI Version](https://img.shields.io/pypi/v/ssd.svg)](https://pypi.python.org/pypi/ssd)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/ssd.svg)](https://pypi.python.org/pypi/ssd)
[![PyPI License](https://img.shields.io/pypi/l/ssd.svg)](https://pypi.python.org/pypi/ssd)


Installation
------------

Type in your command shell **with _administrator/root_ privileges**:

    pip install ssd

In Unix-based systems, this is generally achieved by superseding
the command `sudo`.

    sudo pip install ssd

If the above commands fail, consider installing it with the option
[`--user`](https://pip.pypa.io/en/latest/user_guide/#user-installs):

    pip install --user ssd


Usage
-----

Import in your script the module `sdd` and call its function `is_ssd`.

    from ssd import is_ssd

    is_ssd('/path/to/file-or-dir')

**pySSD** will return `True` if the drive, where the given path is located, is
recognized as a solid-state drive, otherwise `False`.

_That's All Folks!_


------------------------------------------------
###### © 2017 Walter Purcaro <vuolter@gmail.com>
