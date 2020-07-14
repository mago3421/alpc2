from setuptools import setup, Extension
from setuptools.command.install import install
import subprocess
import os

setup(
    name='string2words',
    version='0.1',
    packages=['string2words'],
    description='Art+Logic Programming Challenge Part 2 Solution by Marc Gonzalez',
    url='git@github.com:mago3421/alpc2.git',
    author='Marc Gonzalez',
    author_email='marc.gonzalez@colorado.edu',
    license='No License',
    include_package_data=True
)
