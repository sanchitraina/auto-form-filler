try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Project X',
	'author': 'Sanchit Raina',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'rainasanchit01@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['projectx'],
	'scripts': [],
	'name': 'projectx'
}

setup(**config)