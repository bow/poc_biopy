#!/usr/bin/env python

"""
    Biopython-Statistics
    ~~~~~~~~~~~~~~~~~~~~

    Biopython extension for common statistical functions

    :license: See LICENSE

"""

from __future__ import print_function
from setuptools import setup


RELEASE = True
__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""


setup(
    name="poc_hook_Biopython-Statistics",
    version=__version__,
    url="http://biopython.org",
    license="Biopython License",
    author="Peter Cock",
    description="Biopython extension for common statistical functions",
    long_description=__doc__,
    packages=["biopy_statistics"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "poc_hook_Biopython==2.0.0",    
        "numpy>=1.8",
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
