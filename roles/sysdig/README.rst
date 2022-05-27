Ansible role for installation and configuration sysdig.
Sysdig is a system visibility tool with native support for containers.

**Role Variables**

.. zuul:rolevar:: sysdig_package_name
   :default: sysdig

The required package which is needed.

.. zuul:rolevar:: sysdig_kernel_module_name
   :default: sysdig_probe

The kernel module name for configuring and enabling sysdig.

.. zuul:rolevar:: sysdig_configure_repository
   :default: true

For downloading packages via https, this package is needed first.

.. zuul:rolevar:: sysdig_debian_repository_arch
   :default: amd64

This means the architecture from the system where you want to install sysdig.

.. zuul:rolevar:: sysdig_debian_repository_key
   :default: https://s3.amazonaws.com/download.draios.com/DRAIOS-GPG-KEY.public

The Url where the package will be downloaded from.

.. zuul:rolevar:: sysdig_debian_repository
   :default: deb [ arch={{ sysdig_debian_repository_arch }} ] https://download.sysdig.com/stable/deb stable-{{ sysdig_debian_repository_arch }}/

Repository name from the sysdig-file for debian distributions.
