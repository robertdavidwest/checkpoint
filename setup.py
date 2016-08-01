from distutils.core import setup
from checkpoint import __version__

setup(
    name='checkpoint',
    version=__version__,
    author='Robert West',
    author_email='robert.david.west@gmail.com',
    packages=['checkpoint'],
    scripts=[],
    description='Easily and quickly shelve variables at some point in your code - a checkpoint! :)',
    long_description=open('README.md').read(),
    install_requires=[
        'getpass',
        'shelve',
        'time',
        'dateutil',
        'os',
        'pandas'
    ]
)