Ansible role for installing kernel modules.

**Role Variables**

.. zuul:rolevar:: kernel_modules_default
   :default: - bonding
             - 8021q

Kernel modules which you want to install.

.. zuul:rolevar:: kernel_modules_extra
   :default: []

Extra modules defiened in a list which you want to install.

.. zuul:rolevar:: kernel_modules
   :default: kernel_modules_default + kernel_modules_extra

All modules which you want to install.