Ansbile role for installing ipmitool and its required kernel modules.

**Role Variables**

.. zuul:rolevar:: ipmitool_package_name
   :default: ipmitool

Distribution package for ipmitool.

.. zuul:rolevar:: ipmitool_kernel_modules
   :default: - ipmi_devintf
             - ipmi_si

Required kernel modules for running ipmitool.