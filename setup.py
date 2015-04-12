#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pru",
    version="0.1.0",
    author="Adam Dobrawy",
    author_email="naczelnik@jawnosc.tk",
    packages=[
        "pru",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["pru/manage.py"],
)