import setuptools
import tiafork

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


AUTHOR = 'Nathan Ramos, CFA®'
AUTHOR_EMAIL = 'info@nrcapitalmanagement.com'
PACKAGE = 'tiafork'
PACKAGE_DESC = 'Fork of tia: Toolkit for integration and analysis'
VERSION = tiafork.__version__
URL = "https://github.com/nathanramoscfa/tiafork"
REQUIRED = ['pandas', 'numpy']
REQUIRED_FOR_TESTS = []

LONG_DESC = long_description

setuptools.setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=PACKAGE_DESC,
    include_package_data=True,
    install_requires=REQUIRED,
    long_description=LONG_DESC,
    name=PACKAGE,
    packages=['tiafork', 'tiafork.analysis', 'tiafork.bbg', 'tiafork.rlab', 'tiafork.tests',
              'tiafork.util', 'tiafork.analysis.model'],
    package_dir={'tiafork': 'tiafork'},
    test_suite='tiafork.tests',
    tests_require=REQUIRED_FOR_TESTS,
    url=URL,
    version=VERSION,
    keywords=['bloomberg', 'backtesting', 'technical analysis', 'pdf'],
    download_url=URL,
    license='BSD (3-clause)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Utilities',
    ],
)
