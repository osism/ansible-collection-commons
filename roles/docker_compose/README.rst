Ansible role for configuration and installation of docker-compose including its components.

**Role Variables**

.. zuul:rolevar:: docker_compose_install_type
   :default: package

Source of docker-compose installation.
Currently only 'package' is supported.

.. zuul:rolevar:: docker_compose_package_name
   :default: docker-compose

The name of the docker-compose package to uninstall.

.. zuul:rolevar:: docker_compose_plugin_package_name
   :default: docker-compose-plugin

The name of the docker-compose-plugin package to install.

.. zuul:rolevar:: docker_compose_service_user
   :default: "{{ operator_user | default('dragon') }}"

The user the docker-compose service should run with.

.. zuul:rolevar:: docker_compose_service_group
   :default: "{{ operator_group | default('dragon') }}"

The group the docker-compose service should run with.
