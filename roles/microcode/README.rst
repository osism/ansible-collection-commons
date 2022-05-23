Ansible role for the installation of microcode.

**Role Variables**

.. zuul:rolevar:: microcode_packages_default
   :default: - amd64-microcode
             - intel-microcode

The packages that are needed for microcode

.. zuul:rolevar:: microcode_packages_extra
   :default: []

Extra packages which you want to install.

.. zuul:rolevar:: microcode_packages
   :default: microcode_packages_default + microcode_packages_extra

The whole packages that will be installed.
