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

To scrape a list of meets occurring in Australia on a given date, call the scrape_meets method on the scraper instance as follows:

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


Scraping Races
~~~~~~~~~~~~~~

To scrape a list of races occurring at a specified meet, call the scrape_races method on the scraper instance as follows:

	>>> races = scraper.scrape_races(meet)

meet must be a dictionary containing a 'url' key with a corresponding value representing the URL or path to the meet details page at www.punters.com.au.

The scrape_races method will return a list of dictionaries, with each dictionary providing the following keys to represent a single race's details:

+------------------+-------------+-----------------------------------------------------------------+
| Key              | Type        | Description                                                     |
+==================+=============+=================================================================+
| distance         | int         | The race's distance in metres                                   |
+------------------+-------------+-----------------------------------------------------------------+
| entry_conditions | list of str | The entry conditions for the race (age, class, sex and weights) |
+------------------+-------------+-----------------------------------------------------------------+
| number           | int         | The race's number on the meet program                           |
+------------------+-------------+-----------------------------------------------------------------+
| prize_money      | float       | The total prize money on offer for the race                     |
+------------------+-------------+-----------------------------------------------------------------+
| start_time       | datetime    | The advertised start time for the race                          |
+------------------+-------------+-----------------------------------------------------------------+
| track_circ       | int         | The length of the circular part of the track in metres          |
+------------------+-------------+-----------------------------------------------------------------+
| track_condition  | str         | The official track condition rating as at the time of the race  |
+------------------+-------------+-----------------------------------------------------------------+
| track_rail       | str         | Description of the track's rail position                        |
+------------------+-------------+-----------------------------------------------------------------+
| track_straight   | int         | The length of the straight part of the track in metres          |
+------------------+-------------+-----------------------------------------------------------------+
| url              | str         | The path to the race details page at www.punters.com.au         |
+------------------+-------------+-----------------------------------------------------------------+


Scraping Runners
~~~~~~~~~~~~~~~~

To scrape a list of active (non-scratched) runners competing in a specified race, call the scrape_runners method on the scraper instance as follows:

	>>> runners = scraper.scrape_runners(race)

race must be a dictionary containing a 'url' key with a corresponding value representing the URL or path to the race details page at www.punters.com.au.

The scrape_runners method will return a list of dictionaries, with each dictionary providing the following keys to represent a single runner's details:

+----------------------+-------------+-------------------------------------------------------------------------------------+
| Key                  | Type        | Description                                                                         |
+======================+=============+=====================================================================================+
| barrier              | int         | The barrier number that the runner is jumping from                                  |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| horse_has_blinkers   | bool        | True if the horse is wearing blinkers; False otherwise                              |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| horse_url            | str         | The path to the horse's profile page at www.punters.com.au                          |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| jockey_claiming      | float       | The weight allowance claimed by an apprentice jockey (0.0 for professional jockeys) |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| jockey_is_apprentice | bool        | True if the jockey is an apprentice; False otherwise                                |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| jockey_url           | str         | The path to the jockey's profile page at www.punters.com.au                         |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| number               | int         | The runner's number on the race card                                                |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| trainer_url          | str         | The path to the trainer's profile page at www.punters.com.au                        |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| weight               | float       | The runner's official listed pre-allowance weight                                   |
+----------------------+-------------+-------------------------------------------------------------------------------------+


Scraping Horses
~~~~~~~~~~~~~~~

To scrape a horse's profile from a specified URL, call the scrape_horse method on the scraper instance as follows:

	>>> horse = scraper.scrape_horse(url)

The scrape_horse method will return a dictionary containing the following keys representing the horse's details:

+----------------------+-------------+-------------------------------------------------------------------------------------+
| Key                  | Type        | Description                                                                         |
+======================+=============+=====================================================================================+
| colour               | str         | The horse's colour                                                                  |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| country              | str         | The horse's country of origin                                                       |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| dam                  | str         | The name of this horse's dam (mother)                                               |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| foaled               | datetime    | The date on which the horse was foaled (born)                                       |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| name                 | str         | The horse's name                                                                    |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| sex                  | str         | The horse's sex                                                                     |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| sire                 | str         | The name of the horse that sired (fathered) this horse                              |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| url                  | str         | The path to the horse's profile page at www.punters.com.au                          |
+----------------------+-------------+-------------------------------------------------------------------------------------+


Scraping Jockeys
~~~~~~~~~~~~~~~~

To scrape a jockey's profile from a specified URL, call the scrape_jockey method on the scraper instance as follows:

	>>> jockey = scraper.scrape_jockey(url)

The scrape_jockey method will return a dictionary containing the following keys representing the jockey's details:

+----------------------+-------------+-------------------------------------------------------------------------------------+
| Key                  | Type        | Description                                                                         |
+======================+=============+=====================================================================================+
| name                 | str         | The jockey's name                                                                   |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| url                  | str         | The path to the jockey's profile page at www.punters.com.au                         |
+----------------------+-------------+-------------------------------------------------------------------------------------+


Scraping Trainers
~~~~~~~~~~~~~~~~~

To scrape a trainer's profile from a specified URL, call the scrape_trainer method on the scraper instance as follows:

	>>> trainer = scraper.scrape_trainer(url)

The scrape_trainer method will return a dictionary containing the following keys representing the trainer's details:

+----------------------+-------------+-------------------------------------------------------------------------------------+
| Key                  | Type        | Description                                                                         |
+======================+=============+=====================================================================================+
| name                 | str         | The trainer's name                                                                  |
+----------------------+-------------+-------------------------------------------------------------------------------------+
| url                  | str         | The path to the trainer's profile page at www.punters.com.au                        |
+----------------------+-------------+-------------------------------------------------------------------------------------+


Scraping Performances
~~~~~~~~~~~~~~~~~~~~~

To scrape a list of completed (not abandoned), official (non-trial) performances from a specified profile URL, call the scrape_performances method on the scraper instance as follows:

	>>> performances = scraper.scrape_performances(url)

The scrape_performances method will return a list of dictionaries, with each dictionary providing the following keys to represent a single performance's details:

+--------------------+-------------+-------------------------------------------------------------------------+
| Key                | Type        | Description                                                             |
+====================+=============+=========================================================================+
| barrier            | int         | The barrier that the runner jumped from for the race                    |
+--------------------+-------------+-------------------------------------------------------------------------+
| carried            | float       | The actual weight carried by the runner after allowances (in kilograms) |
+--------------------+-------------+-------------------------------------------------------------------------+
| date               | datetime    | The date on which the performance occurred                              |
+--------------------+-------------+-------------------------------------------------------------------------+
| distance           | int         | The actual distance of the race (in metres)                             |
+--------------------+-------------+-------------------------------------------------------------------------+
| horse_url          | str         | The path to the horse's profile page at www.punters.com.au              |
+--------------------+-------------+-------------------------------------------------------------------------+
| jockey_url         | str         | The path to the jockey's profile page at www.punters.com.au             |
+--------------------+-------------+-------------------------------------------------------------------------+
| lengths            | float       | The lengths this runner finished behind the winner (0.0 for winners)    |
+--------------------+-------------+-------------------------------------------------------------------------+
| race_prize_money   | float       | The total prize money offered for the race (in AU$)                     |
+--------------------+-------------+-------------------------------------------------------------------------+
| runner_prize_money | float       | The prize money won by this runner in this race (in AU$)                |
+--------------------+-------------+-------------------------------------------------------------------------+
| result             | int         | The final result achieved by the runner in this performance             |
+--------------------+-------------+-------------------------------------------------------------------------+
| starters           | int         | The total number of runners competing in the race                       |
+--------------------+-------------+-------------------------------------------------------------------------+
| starting_price     | float       | The starting price recorded for the runner in this race (in AU$)        |
+--------------------+-------------+-------------------------------------------------------------------------+
| track              | str         | The name of the track at which the race occurred                        |
+--------------------+-------------+-------------------------------------------------------------------------+
| track_condition    | str         | The official track condition rating at the time of the race             |
+--------------------+-------------+-------------------------------------------------------------------------+
| weight             | float       | The official listed pre-allowance weight for the runner (in kilograms)  |
+--------------------+-------------+-------------------------------------------------------------------------+
| winning_time       | float       | The winning time for the winner of the race (in seconds)                |
+--------------------+-------------+-------------------------------------------------------------------------+


Testing
-------

To run the included test suite, execute the following command from the root directory of the pypunters repository::

	python setup.py test

The above command will ensure all test dependencies are installed in your current Python environment. For more concise output during subsequent test runs, the following command can be executed from the root directory of the pypunters repository instead::

	nosetests

The tests for individual components of pypunters can be run by executing any of the following commands from the root directory of the pypunters repository::

	nosetests pypunters.test.meets
	nosetests pypunters.test.races
	nosetests pypunters.test.runners
	nosetests pypunters.test.horses
	nosetests pypunters.test.jockeys
	nosetests pypunters.test.trainers
	nosetests pypunters.test.performances


Version History
---------------

1.0.0 (21 April 2016)
	Initial release
