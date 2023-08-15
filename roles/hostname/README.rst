Ansible role for setting the hostname. It uses either the short
or the full hostname from the ansible inventory.

**Role Variables**

.. zuul:rolevar:: hostname_use_fqdn
   :default: false

Whether to use the full name (`inventory_hostname`) instead of the
short name (`inventory_hostname_short`) as hostname.
