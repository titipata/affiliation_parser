#! /usr/bin/env python
from setuptools import setup

descr = '''Parser for MEDLINE and Pubmed Open-Access affiliation string'''

if __name__ == "__main__":
    setup(
        name='affiliation_parser',
        version='0.1',
        description='Python parser for MEDLINE and Pubmed Open-Access affiliation string',
        long_description=open('README.md').read(),
        url='https://github.com/titipata/affiliation_parser',
        author='Titipat Achakulvisut',
        author_email='titipata@u.northwestern.edu',
        license='(c) 2015 Titipat Achakulvisut',
        keywords='parser affilation',
        install_requires=['numpy', 'unidecode', 'nltk'],
        packages=['affiliation_parser'],
    )
