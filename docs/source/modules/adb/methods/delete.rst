japl.adb.DeltaManager.delete
============================

.. role:: method
.. role:: param

DeltaManager. :method:`delete` ( :param:`table_name: str` )

    Deletes the specified table and the parquet file associated with it.

..  code-block:: python
    
    DeltaManager().delete("my_table")