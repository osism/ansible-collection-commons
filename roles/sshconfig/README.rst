Ansible Role for configuring the ssh-client. Makes it possible to connect
via ssh to the hosts.

**Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user who will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: operator_user

The group which will own th econfiguration directory.

.. zuul:rolevar:: sshconfig_destination
   :default: /home/{{ operator_user }}/.ssh

Directory where the configuration file will be stored in.

.. zuul:rolevar:: sshconfig_groupname
   :default: all

The groups (hosts) which will be configured.

.. zuul:rolevar:: sshconfig_order
   :default: 20

Priority for the ssh configuration file. The file will be stored in the
config.d directory where oether files might exist. They are read in alphabetical 
order and with this variable you can minipulate the order in which it will
be evaluated.

.. zuul:rolevar:: sshconfig_port
   :default: 22

The port on which the ssh-service will listen for connections.

.. zuul:rolevar:: sshconfig_private_key_file
   :default: /opt/ansible/secrets/id_rsa.operator

The file in which the ssh key from the operator is stored.

.. zuul:rolevar:: sshconfig_user
   :default: operator_user

User which should be used to establish the ssh connection.
