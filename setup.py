#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

with open('README.md', 'r') as fd:
    long_description = fd.read()

import os, re;
with open(os.path.join(os.path.dirname(__file__), 'pythonvideoannotator_module_gitsync','__init__.py')) as fd:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)


setup(
	name='Python video annotator - module - gitsync',
	version=version,
	description="""""",
	author=['Pedro Cotovio'],
	author_email='pepedro97@gmail.com',
	url='https://github.com/fchampalimaud/pythonvideoannotator-module-gitsync',
	long_description = long_description,
    long_description_content_type = 'text/markdown',
	packages=find_packages(),	
)
