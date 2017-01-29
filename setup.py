try:
    from setuptools import setup
except:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Hicham Ichkantana',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'hishamo@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
