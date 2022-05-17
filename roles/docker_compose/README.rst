Ansible Role for configuration and installation docker including its components.

**Role Variables**

.. zuul:rolevar:: docker_compose_install_type
:default: package

Source of docker-compose installation.

.. zuul:rolevar:: docker_compose_package_name
:default: docker-compose

The name of the docker-compose package which is needed.

.. zuul:rolevar:: docker_compose_plugin_package_name
:default: docker-compose-plugin

The package-name from the used docker plugin.

.. zuul:rolevar:: docker_compose_service_user
:default: "{{ operator_user | default('dragon') }}"

The user docker should run with.

.. zuul:rolevar:: docker_compose_service_group
:default: "{{ operator_group | default('dragon') }}"

The group of the user docker should run with.