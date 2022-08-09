Install the configuration directory.

**Generic Role Variables**

.. zuul:rolevar:: operator_user
   :default: dragon

The user that will own the configuration directory.

.. zuul:rolevar:: operator_group
   :default: "{{ operator_user }}"

The group that will own the configuration directory.

.. zuul:rolevar:: configuration_type
   :default: git

That is the source type for the configuration. Currently only ``git``
is supported.

.. zuul:rolevar:: configuration_directory
   :default: /opt/configuration

The directory where the configuration will be stored in.

**Variables for configuration type ``git``**

.. zuul:rolevar:: configuration_git_package_name
   :default: git

Name of the package to install for the ``git`` binary.

.. zuul:rolevar:: configuration_git_proxy
   :default: ""

If you have to use a proxy to be able to reach your git server use this variable.

.. zuul:rolevar:: configuration_git_public_key
   :default: ""

The public key from the keypair which you use to connect to git.

.. zuul:rolevar:: configuration_git_private_key
   :default: ""

The private key from the keypair which you use to connect to git.

.. zuul:rolevar:: configuration_git_private_key_file
   :default: ~/.ssh/id_rsa.configuration

The path where your keypair is stored.

.. zuul:rolevar:: configuration_git_version
   :default: main

The branch name which should be used.

.. zuul:rolevar:: configuration_git_host
   :default: github.com

The host from where you get the repositories.

.. zuul:rolevar:: configuration_git_port
   :default: 22

The port that is used for downloading the repository.

.. zuul:rolevar:: configuration_git_repository
   :default: osism/ansible-collection-commons.git

The name of the repository which is needed.

.. zuul:rolevar:: configuration_git_protocol
   :default: ssh

Which protocol will be used for the downloads.

.. zuul:rolevar:: configuration_git_username
   :default: git

The username that is used for downloading the repository.
