This role configures sysctl (Kernelparameters). It can be used to tune
the components from a system to a better perfoming way.Be aware that if
you do it in the wrong way it can slow down the system too.

**Role Variables**

.. zuul:rolevar:: sysctl_defaults

In this section are the parameters for elesticsearch, rabbitmq and the notes
``all`` or ``compute`` are declared in a list.

.. zuul:rolevar:: sysctl_extra

Here you can declare extra variables that you want to configure. 
