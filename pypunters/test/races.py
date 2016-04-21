from datetime import datetime

from .common import ScraperTest


class RacesTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.meet = {
			'date':		datetime(2016, 2, 1),
			'track':	'Kilmore',
			'url':		'/racing-results/victoria/Kilmore/2016-02-01/'
		}
		cls.expected_races = [
			{
				'number':			1,
				'distance':			1100,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 13, 10),
				'url':				'/form-guide/Kilmore_69146/Wandong-Bus-and-Coach-Maiden-Plate_411192/',
				'entry_conditions':	[
					'Three-Years-Old and Upwards',
					'Maiden',
					'No sex restriction',
					'Set Weights'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			2,
				'distance':			1200,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 13, 45),
				'url':				'/form-guide/Kilmore_69146/Book-now-for-Valentines-Day-14-Feb-Maiden-Plate_411193/',
				'entry_conditions':	[
					'Three-Years-Old',
					'Maiden',
					'Fillies',
					'Set Weights'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			3,
				'distance':			1450,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 14, 20),
				'url':				'/form-guide/Kilmore_69146/Montmorency-RSL-Maiden-Plate_411194/',
				'entry_conditions':	[
					'Three-Years-Old and Upwards',
					'Maiden',
					'No sex restriction',
					'Set Weights'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			4,
				'distance':			1600,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 14, 55),
				'url':				'/form-guide/Kilmore_69146/Sunday-Sessions-%40-Trackside-7-Feb-Maiden-Plate_411195/',
				'entry_conditions':	[
					'Three-Years-Old and Upwards',
					'Maiden',
					'No sex restriction',
					'Set Weights'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			5,
				'distance':			1100,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 15, 32),
				'url':				'/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/',
				'entry_conditions':	[
					'No age restriction',
					'BenchMark 64',
					'No sex restriction',
					'Handicap'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			6,
				'distance':			1200,
				'prize_money':		16000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 16, 12),
				'url':				'/form-guide/Kilmore_69146/Wilson-Medic-One-Rising-Stars-0-58-Handicap_411197/',
				'entry_conditions':	[
					'No age restriction',
					'0 - 58',
					'No sex restriction',
					'Handicap'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			7,
				'distance':			1900,
				'prize_money':		20000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 16, 52),
				'url':				'/form-guide/Kilmore_69146/Sportsmans-Lunch-%40-Trackside-26-Feb-BM64-Handicap_411198/',
				'entry_conditions':	[
					'No age restriction',
					'BenchMark 64',
					'No sex restriction',
					'Handicap'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			},
			{
				'number':			8,
				'distance':			1600,
				'prize_money':		16000.00,
				'track_condition':	'Good 4',
				'start_time':		datetime(2016, 2, 1, 17, 32),
				'url':				'/form-guide/Kilmore_69146/Book-Now-Jet-Roofing-Kilmore-Pacing-Cup-0-58-Handicap_411199/',
				'entry_conditions':	[
					'No age restriction',
					'0 - 58',
					'No sex restriction',
					'Handicap'
				],
				'track_circ':		1735,
				'track_straight':	320,
				'track_rail':		'True Entire Circuit'
			}
		]

		cls.scraped_races = cls.scraper.scrape_races(cls.meet)

	def setUp(self):
		
		self.assertIsInstance(self.scraped_races, list)

	def test_expected_races(self):
		"""The scrape_races method should return a list containing all expected races"""

		self.check_expected_items(self.expected_races, self.scraped_races)

	def test_unexpected_races(self):
		"""The scrape_races method should return a list that does not contain any unexpected races"""

		self.check_unexpected_items(self.expected_races, self.scraped_races)