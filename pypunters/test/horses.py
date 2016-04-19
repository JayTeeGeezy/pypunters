from datetime import datetime

from .common import ScraperTest


class HorsesTest(ScraperTest):

	def test_expected_values(self):
		"""The scrape_horse method should return a dictionary containing all expected values"""

		url = '/horses/Tycoon-Tony_395471/'
		expected_values = {
			'url':		url,
			'name':		'Tycoon Tony',
			'colour':	'bay',
			'sex':		'gelding',
			'sire':		'Written Tycoon',
			'dam':		'Real Ruby',
			'country':	'Australia',
			'foaled':	datetime(2011, 10, 1)
		}

		scraped_values = self.scraper.scrape_horse(url)

		self.assertIsInstance(scraped_values, dict)
		self.check_expected_values(expected_values, scraped_values)