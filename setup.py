import os
import re

v = open(os.path.join(os.path.dirname(__file__), 'NAME', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Your Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'Your email',
    'version': VERSION,
    'install_requires': [],
    'tests_require': ['nose'],
    'packages': ['NAME', 'NAME.test'],
    'scripts': [],
    'name': 'NAME'
}

setup(**config)
