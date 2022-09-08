japl.adb.DeltaManager.add
============================

.. role:: method
.. role:: param

DeltaManager. :method:`add` ( :param:`table_name: str, raw_path: str, destionation_path: str, write_mode: str  = 'overwrite', file_name: str  = None, nested: bool = False` )

    Adds a new table from a raw_path and stores it into a destionation_path.

..  code-block:: python
    
    DeltaManager().add("my_table", "dbfs:/mnt/raw/my_path/", "dbfs:/mnt/silver/my_path/")