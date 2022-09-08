japl.adb.DeltaManager.rollback
==============================

.. role:: method
.. role:: param

DeltaManager. :method:`rollback` ( :param:`table_name: str, no_of_versions: int = 1, aim_version: int = None, date: str = None, timestamp: str = '00:00:00'` )

    Returns a table to a previous version, by number of version, a specific verion or by a timestamp.

.. note::
    | Date Format: YYYY-MM-DD
    | Time Format: HH:MM:SS

Return n versions
^^^^^^^^^^^^^^^^^

    Does a rollback by 2 versions.. So this would be, current_version - 2.

..  code-block:: python
    
    DeltaManager().rollback("my_table", 2)

Return to version
^^^^^^^^^^^^^^^^^

    Does a rollback to the second version. So this would be, version = 2.

..  code-block:: python
    
    DeltaManager().rollback("my_table", aim_version = 2)

Return by datetime
^^^^^^^^^^^^^^^^^^

    Does a rollback to the version as of the 22nd of march, 2001, 6 am.

..  code-block:: python
    
    DeltaManager().rollback("my_table", date = '2001-03-22', timestamp = '06:00:00')   