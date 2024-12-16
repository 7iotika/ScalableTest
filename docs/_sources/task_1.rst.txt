.. _task_1:

Task 1. Architecture
=====================

The **Plans** function enables the customization of user access to system features based on their user type.

By default, the system has 4 types of end-users. Below is a description of their characteristics.

.. note::
    
   Please note that the list of user types can be customized for each partner separately. Additionally, the available features, access rights and transition conditions can also be customized.

..  list-table::
    :widths: 10 10 10 10
    :header-rows: 1
    :stub-columns: 1

    * - User type
      - Session limit
      - Operations per day
      - Operations per week

    * - guest
      - 20 minutes
      - 5 operations
      - 20 operations

    * - basic
      - 20 minutes
      - 20 operations
      - 50 operations

    * - company
      - no limits
      - no limits
      - no limits

    * - advanced
      - no limits
      - no limits
      - no limits


.. warning::

   When the limit is reached, the user enters the "idle" state.

The verification procedure **KYC** (Know Your Customer) allows to increase the **guest** user type up to the **basic**. The other types can also be upgraded or downgraded, depending on the configurable conditions, for example:

.. image:: /_images/plantuml.png
  :align: center


