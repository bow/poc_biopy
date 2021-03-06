#!/usr/bin/env python

"""
    Biopython-TogoWS
    ~~~~~~~~~

    Biopython extension to interface with TogoWS

    :license: See LICENSE

"""

from __future__ import print_function
from setuptools import setup


RELEASE = True
__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""


setup(
    name="poc_pkgutil_Biopython-TogoWS",
    version=__version__,
    url="http://biopython.org",
    license="Biopython License",
    author="Peter Cock",
    description="Biopython extension to interface with TogoWS",
    long_description=__doc__,
    packages=["biopy", "biopy.ext", "biopy.ext.togows"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "poc_pkgutil_Biopython==2.0.0",    
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ]
)
