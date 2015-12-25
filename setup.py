try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Argparse Visual Types',
    'author': 'Ian Millington',
    'url': 'https://github.com/idmillington/argvtypes',
    'download_url': 'https://github.com/idmillington/argvtypes',
    'author_email': 'idmillington@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['argvtypes'],
    'scripts': [],
    'name': 'argvtypes'
}

setup(**config)
