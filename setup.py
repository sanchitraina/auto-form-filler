try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Automatically Fill All Form Fields',
	'author': 'Sanchit',
	'url': 'bin\\index.py',
	'download_url': 'Where to download it.',
	'author_email': 'rainasanchit01@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['virtualenv'],
	'scripts': [],
	'name': 'autoformfiller'
}

setup(**config)