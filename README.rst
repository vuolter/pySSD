pySSD
=====

Table of contents
-----------------

-  `Description`_
-  `Installation`_
-  `Usage`_

Description
-----------

A tiny, but effective, SSD checker for Python.

Working on Windows, macOS and linux.

Installation
------------

Type in your command shell **with *administrator/root* privileges**:

::

    pip install ssd

In Unix-based systems, this is generally achieved by superseding the
command ``sudo``.

::

    sudo pip install ssd

If the above commands fail, consider installing it with the option
`--user`_:

::

    pip install --user ssd

Usage
-----

Import in your script the module ``sdd`` and call its function
``is_ssd``.

::

    from ssd import is_ssd

    is_ssd('/path/to/file-or-dir')

**pySSD** will return ``True`` if the drive, where the given path is
located, is recognized as a solid-state drive, otherwise ``False``.

*That's All Folks!*


.. _Description: #description
.. _Installation: #installation
.. _Usage: #usage
.. _--user: https://pip.pypa.io/en/latest/user_guide/#user-installs
