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

To use pypunters, you must first import the pypunters package into your Python interpreter and create an instance of pypunters.Scraper. Instantiation of pypunters.Scraper requires a HTTP client and a HTML parser.

The HTTP client can be any object that conforms to the Requests API, supporting code such as the following::

	response = http_client.get(url)
	response.raise_for_status()
	content = response.text

The HTML parser can be any callable that conforms to the lxml.html.fromstring signature, supporting code such as the following::

	html = html_parser(content)

pypunters has only been tested with cache_requests and lxml.html.fromstring. These dependencies can be met as follows:

	>>> import cache_requests
	>>> http_client = cache_requests.Session()

	>>> from lxml import html
	>>> html_parser = html.fromstring

With these dependencies in place, pypunters.Scraper can be instantiated as follows:

	>>> import pypunters
	>>> scraper = pypunters.Scraper(http_client, html_parser)


Scraping Meets
~~~~~~~~~~~~~~

To scrape a list of meets occurring on a given date, call the scrape_meets method on the scraper instance as follows:

	>>> from datetime import datetime
	>>> date = datetime(2016, 2, 1)
	>>> meets = scraper.scrape_meets(date)

The scrape_meets method will return a list of dictionaries, with each dictionary providing the following keys to represent a single meet's details:

+-------+----------+---------------------------------------------------------+
| Key   | Type     | Description                                             |
+=======+==========+=========================================================+
| date  | datetime | The date on which the meet occurs                       |
+-------+----------+---------------------------------------------------------+
| track | str      | The name of the track at which the meet occurs          |
+-------+----------+---------------------------------------------------------+
| url   | str      | The path to the meet details page at www.punters.com.au |
+-------+----------+---------------------------------------------------------+


Testing
-------

To run the included test suite, execute the following command from the root directory of the pypunters repository::

	python setup.py test

The above command will ensure all test dependencies are installed in your current Python environment. For more concise output during subsequent test runs, the following command can be executed from the root directory of the pypunters repository instead::

	nosetests

The tests for individual components of pypunters can be run by executing any of the following commands from the root directory of the pypunters repository::

	nosetests pypunters.test.meets
