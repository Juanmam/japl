DeltaManager
============

The DeltaManager class consist of a series of pre-build operations to easily 
interact with tables in the datalake. It is a singleton instance, so no variable
is needed to keep it persistant overtime.

.. toctree::
   :maxdepth: 3
   :caption: Modules:

   add
   mount
   update
   rollback
   delete
   delete_all