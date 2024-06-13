Ansible role to configure the operator user with all its dependencies.

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The operator user name.

.. zuul:rolevar:: operator_user_id
   :default: 45000

ID for the operator user.

.. zuul:rolevar:: operator_group
   :default: dragon

The group for the operator user.

.. zuul:rolevar:: operator_group_id
   :default: 45000

ID for the group.

.. zuul:rolevar:: operator_shell
   :default: /bin/bash

The default shell for the operator.

.. zuul:rolevar:: operator_authorized_keys
   :default: []

List of SSH public keys to add to the authorized keys for the operator account.

.. zuul:rolevar:: operator_authorized_github_accounts
   :default: []

List of Github accounts from which the SSH public keys are added to the authorized keys.

.. zuul:rolevar:: operator_password

Encrypted password string to set for the operator user (optional).

.. zuul:rolevar:: operator_password_root

Encrypted password string to set for the root user (optional).

.. warning:: 
   Use "mkpasswd --method=sha-512" to generate an encrypted password.
   Do not set this variable to a clear-text password.

.. zuul:rolevar:: operator_sudo_nopasswd
   :default: true

Whether the operator user can invoke sudo without a password.

.. zuul:rolevar:: operator_sudo_cmd_list
   :default: ALL

Commands that the user can use with sudo.

.. zuul:rolevar:: operator_groups

Additional groups for the operator user. The default list of groups is distribution
specific.
