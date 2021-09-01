#! /usr/bin/env python
import os

from setuptools import setup

descr = """Python Parser for MEDLINE and Pubmed Open-Access affiliation string"""

_root = os.path.dirname(os.path.realpath(__file__))
requirements = os.path.join(_root, "requirements.txt")
REQUIREMENTS = [x.strip() for x in open(requirements).readlines()]

if __name__ == "__main__":
    setup(
        name="affiliation_parser",
        version="0.1",
        description=descr,
        long_description=open("README.md").read(),
        url="https://github.com/titipata/affiliation_parser",
        author="Titipat Achakulvisut",
        author_email="titipata@u.northwestern.edu",
        license="(c) 2015 Titipat Achakulvisut",
        keywords="parser affilation",
        install_requires=REQUIREMENTS,
        packages=["affiliation_parser"],
    )
