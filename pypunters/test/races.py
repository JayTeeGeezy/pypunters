from datetime import datetime

from .common import ScraperTest


class RacesTest(ScraperTest):

	def test_expected_races(self):
		"""The scrape_races method should return a list containing all expected races"""

		meet = {
			'date':		datetime(2016, 2, 1),
			'track':	'Kilmore',
			'url':		'/racing-results/victoria/Kilmore/2016-02-01/'
		}
		expected_races = [
			{
				'number':			1,
				'distance':			1100,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 13, 10),
				'url':				'/form-guide/Kilmore_69146/Wandong-Bus-and-Coach-Maiden-Plate_411192/'
			},
			{
				'number':			2,
				'distance':			1200,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 13, 45),
				'url':				'/form-guide/Kilmore_69146/Book-now-for-Valentines-Day-14-Feb-Maiden-Plate_411193/'
			},
			{
				'number':			3,
				'distance':			1450,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 14, 20),
				'url':				'/form-guide/Kilmore_69146/Montmorency-RSL-Maiden-Plate_411194/'
			},
			{
				'number':			4,
				'distance':			1600,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 14, 55),
				'url':				'/form-guide/Kilmore_69146/Sunday-Sessions-%40-Trackside-7-Feb-Maiden-Plate_411195/'
			},
			{
				'number':			5,
				'distance':			1100,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 15, 32),
				'url':				'/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/'
			},
			{
				'number':			6,
				'distance':			1200,
				'prize_money':		16000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 16, 12),
				'url':				'/form-guide/Kilmore_69146/Wilson-Medic-One-Rising-Stars-0-58-Handicap_411197/'
			},
			{
				'number':			7,
				'distance':			1900,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 16, 52),
				'url':				'/form-guide/Kilmore_69146/Sportsmans-Lunch-%40-Trackside-26-Feb-BM64-Handicap_411198/'
			},
			{
				'number':			8,
				'distance':			1600,
				'prize_money':		16000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 17, 32),
				'url':				'/form-guide/Kilmore_69146/Book-Now-Jet-Roofing-Kilmore-Pacing-Cup-0-58-Handicap_411199/'
			}
		]

		scraped_races = self.scraper.scrape_races(meet)

		self.assertIsInstance(scraped_races, list)
		self.check_expected_items(expected_races, scraped_races)