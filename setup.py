#!/usr/bin/env python3

from setuptools import setup, find_packages
from mt.geo.version import version

setup(
    name='geomt',
    version=version,
    description="The most fundamental geometric modules in Python for Minh-Tri Pham. This package is deprecated. Use package 'mtgeo' instead.",
    author=["Minh-Tri Pham"],
    packages=find_packages(),
    package_data={
        'mt.geo': ['*.pyx'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'numpy',
        'cython',
        'mtbase>=0.4.0',
        'mtgeo>=0.3.0',
    ],
    url='https://github.com/inteplus/geomt',
    project_urls={
        'Documentation': 'https://geomt.readthedocs.io/en/stable/',
        'Source Code': 'https://github.com/inteplus/geomt',
    }
)
