Ansible role for installing kernel modules. The configured modules are
both loaded immediately via ``modprobe`` as well as added to the
``/etc/modules`` so that they will be automatically installed on boot.

**Role Variables**

.. zuul:rolevar:: kernel_modules_default
   :default: [ "bonding", "8021q" ]

Default list of kernel modules to install.

.. zuul:rolevar:: kernel_modules_extra
   :default: []

List of extra modules to install.

.. zuul:rolevar:: kernel_modules
   :default: kernel_modules_default + kernel_modules_extra

All modules which you want to install.
