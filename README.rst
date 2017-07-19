pySSD
=====

Table of contents
-----------------

-  `Description`_
-  `Installation`_
-  `Usage`_

Description
-----------

A tiny, but effective, Solid-State Drive checker for Python.

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

If in your system missing the command ``pip``, but you're sure you have
installed the `Python Interpreter`_ and the package ``setuptools``
(>=20.8.1), you can try to install **pySSD** from the sources, in this
way:

1. Get the latest tarball of the source code in format `ZIP`_ or `TAR`_.
2. Extract the downloaded archive.
3. From the extracted path, launch the command
   ``python setup.py install``.

Usage
-----

Import in your script the module ``sdd`` and call its function
``is_ssd``.

::

    from ssd import is_ssd

    is_ssd('/path/to/file-or-dir-or-dev')

Return value will be ``True`` if the drive, where the given path is
located, was recognized as SSD, otherwise ``False``.

    **Note:** Ramdisks are always recognized as SSD under Windows.

*That's All Folks!*

.. _Description: #description
.. _Installation: #installation
.. _Usage: #usage
.. _--user: https://pip.pypa.io/en/latest/user_guide/#user-installs
.. _Python Interpreter: https://www.python.org
.. _ZIP: https://github.com/vuolter/pySSD/archive/master.zip
.. _TAR: https://github.com/vuolter/pySSD/archive/master.tar.gz
