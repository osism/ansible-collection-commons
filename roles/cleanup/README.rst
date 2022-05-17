An ansible role for cleanup not longer needed packages, services and timers.

**Role Variables**

.. zuul:rolevar:: cleanup_packages_default
   :default: lxc

The packages which not needed anymore per default.

.. zuul:rolevar:: cleanup_packages_extra
   :default: []

Packages, which you can declare what you not needed anymore

.. zuul:rolevar:: cleanup_packages
   :default: cleanup_packages_default + cleanup_packages_extra + cleanup_packages_distribution

The whole packages from the first and second parameters including the distribution packages, which should be cleaned up.

.. zuul:rolevar:: cleanup_services_default
   :default: []

The services which are no longer needed per default.

.. zuul:rolevar:: cleanup_services_extra
   :default: []

Services that you can declare which you not needed anymore.

.. zuul:rolevar:: cleanup_services
   :default: cleanup_services_default + cleanup_services_extra + cleanup_services_distribution

The whole services from the default and your declaration which will be deleted.

.. zuul:rolevar:: cleanup_cloudinit
   :default: true

If you want to cleanup the cloudinit file let the default set to true, if not set it to false.

Distribution specific variables:

Debian:
    .. zuul:rolevar:: cleanup_services_distribution
       :default: []
    
    Services from Debian which are not longer needed.

    .. zuul:rolevar:: cleanup_packages_distribution
       :default: - libvirt-bin
                 - lxd
                 - open-iscsi

    Debian packages which are no longer needed.

    .. zuul:rolevar:: cleanup_cloudinit_package_name
       :default: cloud-init

    Debian cloudinit package declaration.

RedHat:
    .. zuul:rolevar:: cleanup_services_distribution
       :default: []
    
    Services from RedHat which are no longer needed.

    .. zuul:rolevar:: cleanup_packages_distribution
       :default: - libvirt
                 - iscsi-initiator-utils

    RedHat packages which are no longer needed.

    .. zuul:rolevar:: cleanup_cloudinit_package_name
       :default: cloud-init
    
    RedHat cloudinit package declaration.