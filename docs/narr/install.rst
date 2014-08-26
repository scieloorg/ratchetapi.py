.. _install:

Installation
============

This part of the documentation covers the installation process of ratchetapi.py.


Pip
---

Installing ratchetapi.py is simple with `pip <http://www.pip-installer.org/>`_::

   $ pip install ratchetapi


Get the Code
------------

ratchetapi.py is actively developed on GitHub, check it out 
`here <https://github.com/scieloorg/ratchetapi.py>`_.

You can either clone the public repository::

    git clone git://github.com/scieloorg/ratchetapi.py.git

Download the `tarball <https://github.com/scieloorg/ratchetapi.py/tarball/master>`_::

    $ curl -OL https://github.com/scieloorg/ratchetapi.py/tarball/master

Or, download the `zipball <https://github.com/scieloorg/ratchetapi.py/zipball/master>`_::

    $ curl -OL https://github.com/scieloorg/ratchetapi.py/zipball/master


Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install


Settings up the logger handler
==============================

It is expected that the application using `ratchetapi` defines a logger for `ratchetapi`, e.g.::

    logging.getLogger('ratchetapi').addHandler(logging.StreamHandler())

See the official `docs <http://docs.python.org/2.7/howto/logging.html#configuring-logging>`_ for more info.

