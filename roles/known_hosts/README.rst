This role adds the ssh hostkeys from hosts in the ansible inventory
to a known_hosts file.

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user that will own the known_hosts file.

.. zuul:rolevar:: operator_group
   :default: operator_user

The group that will own the known_hosts file.

.. zuul:rolevar:: known_hosts_group_name
   :default: all

Add hosts from this group to known_hosts.

.. zuul:rolevar:: known_hosts_destination
   :default: /home/{{ operator_user }}/.ssh

Destination where the known_hosts file is stored.