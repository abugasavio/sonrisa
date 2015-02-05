#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sonrisa
version = sonrisa.__version__

setup(
    name='sonrisa',
    version=version,
    author='',
    author_email='savioabuga@gmail.com',
    packages=[
        'sonrisa',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['sonrisa/manage.py'],
)
