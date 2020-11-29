#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='qshell',
    packages=find_packages(include=['qshell']),
    version='0.1.0',
    description='A interactive command shell wrapper from python projects',
    author='QSoloX',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_suite='test',

)
