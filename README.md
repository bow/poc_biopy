POC-BIOPY
=========

Proof of concept (POC) for a distributed Biopython setup.

POC modules:

  * `biopy_base`: Base Biopython install, contains core sequence objects

  * `biopy_togows`: Pure-python extension

  * `biopy_nexus`: Extension requiring C compilation

  * `biopy_statistics`: Extension depending on numpy


WARNING
-------

This is not for any kind of production use. The codebase are mainly adapted
from the official Biopython distribution, except one where it is mentioned
explicitly.
