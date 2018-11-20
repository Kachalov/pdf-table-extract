#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import setuptools


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_DIR, 'README.md')).read()

setuptools.setup(
    name='pdf-table-extract',
    version='0.1.1',
    description='Extract Tables from PDF files',
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords='PDF, tables',
    author='Ian McEwan',
    author_email='ijm@ashimaresearch.com',
    url='https://github.com/codeRuth/pdf-table-extract/',
    download_url=(
        'https://github.com/codeRuth/pdf-table-extract/archive/0.1.tar.gz'
    ),
    license='MIT-Expat',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=['numpy'],
    entry_points={
        'console_scripts': ['pdf-table-extract=pdftableextract.scripts:main']
    }
)
