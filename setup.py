#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Setup script for imagingd

To install, run:

python setup.py install

"""

from setuptools import setup, find_packages

setup(
    name='imagingd',
    version='0.1.0',
    description='Imaging daemon',
    long_description='Creates images from networks stored in the CX network interchange format.',
    author='Keiichiro Ono, Eric Sage',
    author_email='eric.david.sage@gmail.com',
    url='https://github.com/ericsage/imagingd',
    license='MIT License',
    scripts=['imaging.py'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
          'imagingd = imaging:main'
        ]
    },
    install_requires=[],
    keywords=['bioinformatics', 'graph', 'network', 'cytoscape'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    include_package_data=True,
)
