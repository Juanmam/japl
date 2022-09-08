japl.exceptions.EmptyDataFrameException
=======================================

.. role:: method

:method:`EmptyDataFrameException` ()

    An error used when a DataFrame should have data and got nothing.

..  code-block:: python
    
    if df.empty():
         raise EmptyDataFrameException()