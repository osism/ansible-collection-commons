This andible role transports facts into a state file.

**Role Variables**

.. zuul:rolevar:: state_name
   :default: osism

The name which the state file will have.

.. zuul:rolevar:: state_section
   :default: status

This declares the section in the file where the facts have to be added.

.. zuul:rolevar:: state_option
   :default: deployed

Given option that a fact must have befor adding to the file.

.. zuul:rolevar:: state_value
   :default: false

The value that is given for checking a fact. # Fix me
