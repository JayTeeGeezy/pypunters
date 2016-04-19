from setuptools import setup


def read_text(filename):
	with open(filename) as f:
		return f.read()


setup(
	name='pypunters',
	version='0.0.0',
	description='Python web scraper for www.punters.com.au',
	long_description=read_text('README.rst'),
	classifiers=[
		'Development Status :: 1 - Planning',
		'Environment :: No Input/Output (Daemon)',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.4',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	keywords='web scraper punters',
	url='https://github.com/JayTeeGeezy/pypunters',
	author='Jason Green',
	author_email='JayTeeGeezy@outlook.com',
	license='MIT',
	packages=[
		'pypunters'
	],
	scripts=[
	],
	entry_points={
		'console_scripts': [
		]
	},
	install_requires=[
		'cssselect'
	],
	test_suite='nose.collector',
	tests_require=[
		'cache_requests',
		'cssselect',
		'lxml',
		'nose'
	],
	dependency_links=[
	],
	include_package_data=True,
	zip_safe=False
	)