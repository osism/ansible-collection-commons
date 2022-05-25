Ansible role for manage services.

**Role Variables**

.. zuul:rolevar:: services_warning_default
   :default: nscd

Have a look at services_warning.

.. zuul:rolevar:: services_warning_extra

Have a look at services_warning.

.. zuul:rolevar:: services_warning

Services which shouldn't be running. They will be displayed in a debug message.

.. zuul:rolevar:: services_required_default
   :default: cron

Have a look at services_required.

.. zuul:rolevar:: services_required_extra

Have a look at services_required.

.. zuul:rolevar:: services_required

The services declared in a list which should be managed.
