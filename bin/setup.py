try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Brew Project',
    'author': 'Mark Miraglia',
    'url': 'insert the URl when we have it',
    'download_url': 'where to download it',
    'author_email': 'markmiraglia@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['brew'],
    'scripts': [],
    'name': 'brew'
}

setup(**config)
