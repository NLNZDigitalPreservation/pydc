try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION="0.1.0"

config = {
    'description': 'pydc',
    'author': 'Sean Mosely',
    'author_email': 'sean.mosely@gmail.com',
    'version': VERSION,
    'install_requires': ['lxml==3.6.4',],
    'packages': ['pydc'],
    'scripts': [],
    'name': 'pydc',
    'description': 'Python library for generating Dublin Core XML',
    'download_url': 'https://github.com/NLNZDigitalPreservation/pydc/archive/v'+VERSION+'.tar.gz',
    'license': 'MIT',
}

setup(**config)