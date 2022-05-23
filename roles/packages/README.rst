This ansible role installs a number of required packages.

**Role Variables**

.. zuul:rolevar:: upgrade_packages
   :default: true

For updating the package cache.

.. zuul:rolevar:: required_packages_default
   :default: - ethtool
             - jq
             - rsyslog

The required packages which are needed.

.. zuul:rolevar:: required_packages_extra
   :default: []

Extra packages which you want to install.

.. zuul:rolevar:: required_packages
   :default: required_packages_default + required_packages_extra + required_packages_distribution

The whole packages which should be installed.

**Debian Variables**

.. zuul:rolevar:: apt_cache_valid_time
   :default: 3600

Update the apt cache if it is older than the cache_valid_time.
This option is set in seconds.


.. zuul:rolevar:: required_packages_distribution
   :default: - debsums
             - selinux-utils
             - ssh

Required packages for Debian

**RedHat Variables**

.. zuul:rolevar:: required_packages_distribution
   :default: - libselinux-utils
             - openssh

Required packages for RedHat