japl.adb.DeltaManager.mount
============================

.. role:: method
.. role:: param

DeltaManager. :method:`mount` ( :param:`storage: str, key: str, mount_point: str = '/mnt/', mounts: List[str] = ["raw", "silver", "gold"],  postfix: str = '-zone', include_tqdm: bool = False` )

    Adds a new table from a raw_path and stores it into a destionation_path.

..  code-block:: python
    
    DeltaManager().method("mystorageaccount", "SECRET_KEY")