Ansible role to manage access for admin users.

Creates user accounts and/or manages SSH access for them.

**Role variables**

.. zuul:rolevar:: user_manage_type
   :default: accounts

Which type of access to manage. Valid options are:
  ``accounts``: Creates user-specific accounts for all admins
  ``keyfile``: Adds public SSH keys for all admins to a file

.. zuul:rolevar:: user_ssh_file
   :default: ``~/.ssh/authorized_keys``

Which file to add the SSH keys to.

.. zuul:rolevar:: user_list
   :default: []

List of admin accounts. Each entry is a dict with the keys:
  ``name``; Unix username for the account
  ``key``: URL where the public SSH key for the account can be found

.. zuul:rolevar:: user_delete
   :default: []

List of admin accounts to delete. This is a plain list of
the Unix usernames whose accounts and homedirs will be
deleted.
