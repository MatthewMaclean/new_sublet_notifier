from os import chdir
from os.path import dirname

try:
    from setuptools import setup, find_packages
except ImportError:
    # setuptools wasn't available, so install and try again
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from sublet_notifier import get_package_version, SUBLET_NOTIFIER_MAIN

root_dir = dirname(__file__)

if root_dir != "":
    chdir(root_dir)

setup(
    name='new_sublet_notifier',
    version=get_package_version(),
    author='Matthew Maclean',
    author_email='matthewcmaclean@gmail.com',
    description='Will notify of new sublets available.',
    entry_points={
        'console_scripts': {
            '%s = sublet_notifier.cli:main' % SUBLET_NOTIFIER_MAIN,
        }
    },
    packages=find_packages(exclude="test"),
    include_package_data=True,
    install_requires=[
        'mechanize==0.2.5',
    ],
    test_suite='unittest2.collector',
    tests_require=[
        'unittest2>=0.5.1',
        'pep8>=1.5.7',
    ],
)
