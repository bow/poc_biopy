#!/usr/bin/env python

"""
    Biopython
    ~~~~~~~~~

    Python library for biological data processing.

    :license: See LICENSE

"""

from __future__ import print_function
from setuptools import setup


RELEASE = True
__version_info__ = ("2", "0", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""


setup(
    name="poc_pkgutil_Biopython",
    version=__version__,
    url="http://biopython.org",
    license="Biopython License",
    author="The Biopython Contributors",
    author_email="biopython@lists.open-bio.org",
    description="Python library for biological data processing",
    long_description=__doc__,
    packages=[
        "biopy",
        "biopy.ext",
        "biopy.core",
        "biopy.core._compat",
        "biopy.core.alphabet",
        "biopy.core.data",
        "biopy.seqio",
        ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ]
)
