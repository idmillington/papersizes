try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Paper sizes and manipulations',
    'author': 'Ian Millington',
    'url': 'https://github.com/idmillington/papersizes',
    'download_url': 'https://github.com/idmillington/papersizes',
    'author_email': 'idmillington@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['papersizes'],
    'scripts': [],
    'name': 'papersizes'
}

setup(**config)
