#!/usr/bin/env python

"""
    Biopython-Nexus
    ~~~~~~~~~~~~~~~

    Biopython extension for parsing Nexus files.

"""

## Heavily adapted from simplejson ~ check its LICENSE

from __future__ import print_function
import sys
from setuptools import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError


RELEASE = True
__version_info__ = ("0", "1", "0")
__version__ = ".".join(__version_info__)
__version__ += "-dev" if not RELEASE else ""

IS_PYPY = hasattr(sys, 'pypy_translation_info')


if sys.platform == 'win32' and sys.version_info > (2, 6):
   # 2.6's distutils.msvc9compiler can raise an IOError when failing to
   # find the compiler
   # It can also raise ValueError http://bugs.python.org/issue7511
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError,
                 IOError, ValueError)
else:
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)


class BuildFailed(Exception):
    pass


class ve_build_ext(build_ext):
    # This class allows C extension building to fail.

    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError:
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except ext_errors:
            raise BuildFailed()


def run_setup(with_binary):
    if with_binary:
        kw = dict(
            ext_modules = [
                Extension("biopy.nexus.cnexus", ["biopy_nexus/cnexus.c"]),
            ],
            cmdclass=dict(build_ext=ve_build_ext),
        )
    else:
        kw = dict()

    setup(
        name="poc_hook_Biopython-Nexus",
        version=__version__,
        url="http://biopython.org",
        license="Biopython License",
        author="Frank Kauff & Cymon J. Cox",
        description="Biopython extension for parsing Nexus files",
        long_description=__doc__,
        packages=["biopy_nexus"],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            "poc_hook_Biopython==2.0.0",    
        ],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
        ],
        **kw
    )

try:
    run_setup(not IS_PYPY)
except BuildFailed:
    print("C modules can not be compiled. Exiting.")
    sys.exit(1)
