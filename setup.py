try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pydc',
    'author': 'Sean Mosely',
    'url': 'URL to get at it',
    'download_url': 'Where to download it',
    'author_email': 'sean.mosely@gmail.com',
    'version': '0.1',
    'install_requires': ['lxml',],
    'packages': ['pydc'],
    'scripts': [],
    'name': 'pydc'
}

setup(**config)