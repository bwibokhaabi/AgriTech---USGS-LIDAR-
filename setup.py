#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'pandas>=1.1.0', 
    'numpy>=1.19.0', 
    'geopandas',
]

test_requirements = ['pytest>=3', ]

setup(
    author="bwibokhaabi",
    email="khaabiokacha@students.uonbi.ac.ke",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="This Python package allows you to retrieve, manipulate, and visualize USGS 3DEP lidar point cloud data.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='USGS_lidar',
    name='USGS_lidar',
    packages=find_packages(include=['lidar_tutorial_daisy', 'lidar_tutorial_daisy.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bwibokhaabi/AgriTech---USGS-LIDAR-',
    version='0.0.1',
    zip_safe=False,
)