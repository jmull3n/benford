# -*- coding: utf-8 -*-
"""setup py module for doing setup.py stuff"""
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='labe7_benford_calculator',
    version='0.0.1',
    description='run benford calculation on all the things!',
    long_description=readme,
    author='Jon',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
