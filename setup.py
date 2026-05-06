#!/usr/bin/env python
"""
File: setup.py
Author: Jordan Mirocha (updated)
Description: Installs ares.
"""
import os
from setuptools import setup, find_packages

setup(
    name='ares',
    version='0.1',
    description='Accelerated Reionization Era Simulations',
    author='Jordan Mirocha',
    author_email='mirochaj@gmail.com',
    url='https://github.com/mirochaj/ares',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'h5py',
    ],
)

# Try to set up $HOME/.ares
HOME = os.getenv('HOME')
if not os.path.exists('{!s}/.ares'.format(HOME)):
    try:
        os.mkdir('{!s}/.ares'.format(HOME))
    except:
        pass

for fn in ['defaults', 'labels']:
    if not os.path.exists('{0!s}/.ares/{1!s}.py'.format(HOME, fn)):
        try:
            f = open('{0!s}/.ares/{1!s}.py'.format(HOME, fn), 'w')
            print("pf = {}", file=f)
            f.close()
        except:
            pass
