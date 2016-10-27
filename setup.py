from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'BMP280',
	  version 			= '2.0.1',
	  author			= 'Thomas Foerster',
	  author_email		= 'tom.psnn@gmail.com',
	  description		= 'Library for accessing pressure and temperature sensors on the BMP280 chip .',
	  license			= 'MIT',
	  url				= 'https://github.com/TomFoerster/BMP280',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
	  install_requires	= ['Adafruit-GPIO>=0.6.5'],
	  packages 			= find_packages())
