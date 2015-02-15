try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Interroute',
    'author': 'Chy Lau',
    'url': 'https://github.com/ChyLau/interroute',
    'download_url': 'https://github.com/ChyLau/interroute',
    'author_email': 'chyho.lau@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['interroute'],
    'scripts': [],
    'name': 'interroute'
}

setup(**config)
