japl.tools.Observer
=======================

.. role:: method

:method:`Observer` ()

    The Observer class works as a normal Observer, giving the user 
    the ability to set values, get values and delete values. The data
    is stored as an attribute in the Observer.

Adding data
^^^^^^^^^^^

The set method can be used to set a key to a value. Note that if the key 
already exists, it will just overwrite it.In this example we are going 
to set the attribute money to 20,000.

..  code-block:: python
    
    Observer().set("money", 20000)

Getting data
^^^^^^^^^^^^

The get method can be used to get the value from the attribute. In this 
case, we would store 20,000 in my_local_money from the observer.

..  code-block:: python
    
    my_local_money = Observer().get("money")

Deleting data
^^^^^^^^^^^^^

The rem method can be used to delete an attribute from the Observer.

..  code-block:: python
    
    Observer().rem("money")