Ansible role to install podman.

**Role Variables**

.. zuul:rolevar:: podman_action
   :default: deploy

Name for which file should be included.

Example: ``config.yml`` or ``deploy.yml``

.. zuul:rolevar:: podman_package_name
   :default: podman

The required package for podman.
