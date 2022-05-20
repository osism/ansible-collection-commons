This role populates the ``/etc/hosts`` file with the hosts from the ansible
inventory. For each host, if ``host_enable`` is ``true``, the IPv4 address
of the ``hosts_interface`` is added to ``/etc/hosts``.

**Role Variables**

.. zuul:rolevar:: hosts_enable
   :default: true

Whether to include hosts by default.

.. zuul:rolevar:: hosts_interface

The IPv4 address assigned to this interface is placed in the hosts file.

.. zuul:rolevar:: hosts_group_name
   :default: all

Write only hosts that are included in this group to the hosts file.

.. zuul:rolevar:: hosts_use_dns_as_single_source_of_truth
   :default: false

Set this parameter to True if DNS is to be used as a single source of
truth. No hosts from the hosts defined under hosts_group_name are then
included in the hosts file.

.. zuul:rolevar:: hosts_type
   :default: block

valid values: [block, local, template] # TODO

.. zuul:rolevar:: hosts_file
   :default: /etc/hosts

Path to the managed hosts file.

.. zuul:rolevar:: hosts_file_backup
   :default: true

If this value is set to true, a backup of the file is created before any
changes are made.

.. zuul:rolevar:: hosts_file_reset
   :default: false

If the type block is used and this value is set to True the hosts file is
always completely reset.

.. zuul:rolevar:: hosts_ignore
   default: []

A list of hosts that should not be included in the hosts file.

.. zuul:rolevar:: hosts_additional_entries
   :default: {}

A dictionary with entries in the form FQDN: IP_ADDRESS which are added
to the end of the hosts file.