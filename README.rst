pypunters
=========

Python web scraper for www.punters.com.au


Installation
------------

To install the latest release of pypunters to your current Python environment, execute the following command::

	pip install pypunters

Alternatively, to install pypunters from a source distribution, execute the following command from the root directory of the pypunters repository::

	python setup.py install

To install pypunters from a source distribution as a symlink for development purposes, execute the following command from the root directory of the pypunters repository instead::

	python setup.py develop


Usage
-----

To use pypunters, you must first import the pypunters package into your Python interpreter as follows:

	>>> import pypunters


Testing
-------

To run the included test suite, execute the following command from the root directory of the pypunters repository::

	python setup.py test

The above command will ensure all test dependencies are installed in your current Python environment. For more concise output during subsequent test runs, the following command can be executed from the root directory of the pypunters repository instead::

	nosetests
