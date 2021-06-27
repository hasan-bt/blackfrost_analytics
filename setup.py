# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in blackfrost_analytics/__init__.py
from blackfrost_analytics import __version__ as version

setup(
	name='blackfrost_analytics',
	version=version,
	description='Blackfrost Analytics',
	author='Hasan Raza',
	author_email='hasan.raza@blackfrosttechnologies.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
