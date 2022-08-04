Ansible role for timezone configuration.

**Role Variables**

.. zuul:rolevar:: timezone_hwclock
   :default: UTC

Whether the hardware clock is in UTC or in local timezone. Possible values are local and UTC.

.. zuul:rolevar:: timezone_name
   :default: UTC

Name of the timezone for the system clock.
