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


INSTALLATION
------------

1. The one using `sys.meta_path` (`poc_hook`)
  
   All modules inside it are meant to be separate Python packages that lives
   in its own repository. They are available in `pip`:

   * `biopy_base`: `pip install poc_hook_Biopython`

   * `biopy_togows`: `pip install poc_hook_Biopython-Nexus`

   * and so on ..

   (the names were intentionally chosen to be quite ... verbose to avoid
   clashing with the real production Biopython).

