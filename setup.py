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
    'version': '0.1.0',
    'install_requires': ['lxml==3.6.4',],
    'packages': ['pydc'],
    'scripts': [],
    'name': 'pydc'
}

setup(**config)