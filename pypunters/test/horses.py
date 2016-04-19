from datetime import datetime

from .common import ScraperTest


class HorsesTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.url = '/horses/Tycoon-Tony_395471/'
		cls.expected_values = {
			'url':		cls.url,
			'name':		'Tycoon Tony',
			'colour':	'bay',
			'sex':		'gelding',
			'sire':		'Written Tycoon',
			'dam':		'Real Ruby',
			'country':	'Australia',
			'foaled':	datetime(2011, 10, 1)
		}

		cls.scraped_values = cls.scraper.scrape_horse(cls.url)

	def setUp(self):

		self.assertIsInstance(self.scraped_values, dict)

	def test_expected_values(self):
		"""The scrape_horse method should return a dictionary containing all expected values"""

		self.check_expected_values(self.expected_values, self.scraped_values)

	def test_unexpected_values(self):
		"""The scrape_horse method should return a dictionary that does not contain any unexpected values"""

		self.check_unexpected_values(self.expected_values, self.scraped_values)