Ansible role for managing and configuring the internal network types.

**Role Variables**

.. zuul:rolevar:: network_type
   :default: interfaces

Which type of network you want to install.
Possible values are ``interfaces`` and ``netplan``.

.. zuul:rolevar:: network_manage_devices
   :default: true

Flag whether all network devices are controlled by this role.

.. note::

  Attention!
  If true, all additional configurations are deleted.


.. zuul:rolevar:: network_allow_service_restart
   :default: false

Allow the network to restart.

.. note::

  Attention!
  This is only triggered, when the all interface file was changed.

.. zuul:rolevar:: network_restart_method
   :default: nothing

How should changed interfaces be treated?
Options:

  - ``service`` - restart the network service for the interface
  - ``interface`` - down & up the interface
  - ``nothing`` - do nothing
  - ``*`` - undefined behavior


**Configuration for type interfaces**

List of all network interface configurations:

.. zuul:rolevar:: network_interfaces

For ipv6 you want to add an additional inet6 entry.

Example configuration:

.. code-block:: yaml

   - device: eth0
     # auto & allow are only used for the first device entry
     auto: true  # enable on boot (default)
     allow: []  # array of allow-[stanzas] eg. allow-hotplug

     family: inet  # network type eg. inet | inet6 (default)
     method: dhcp  # dhcp | static (default)
     # examples for method 'static'
     # description: 'a user description'
     # address: 192.168.1.11
     # network: 192.168.1.0
     # netmask: 193.168.1.255
     # broadcast: 192.168.1.255
     # gateway: 192.168.1.1

     # transport
     # mtu: 9000 # give a non-default mtu

     # ifmetric
     # metric: 10

     # optional dns settings
     # nameservers: ['9.9.9.9']
     # dns_search: "domain.net" # appended dns search string

     # optional additional subnets/ips
     # subnets: ['192.168.123.0/24', '192.168.124.11/32']

     bridge: {}  # optional bridge parameters
     #  ports:
     #  stp:
     #  fd:
     #  maxwait:
     #  waitport:

     bond: {}  # optional bonding parameters
     #  mode:
     #  miimon:
     #  master:
     #  slaves:
     #  lacp-rate:

     # optional vlan settings
     vlan: {}
     #  raw-device: 'eth0'

     # inline hook scripts
     pre-up: []  # pre-up script lines
     up: []  # up script lines
     post-up: []  # post-up script lines (alias for up)
     pre-down: []  # pre-down script lines (alias for down)
     down: []  # down script lines
     post-down: []  # post-down script lines

.. zuul:rolevar:: network_interfaces_path
   :default: /etc/network/interfaces

Destination path where to store the interface configuration files.

.. zuul:rolevar:: network_interface_path
   :default: /etc/network/interfaces.d

Sorce path from where to get the configuration file.

.. zuul:rolevar:: network_interface_permissions
   :default: 0644

To set the file permissions for network interfaces configuration files.

.. zuul:rolevar:: network_interface_restart_commands
   :default: interface: "ifdown {{ item.item.0 }}; ifup {{ item.item.0 }}"

Commands for restarting the interface.

.. zuul:rolevar:: network_interface_required_packages
   :default: - bridge-utils
             - ifenslave
             - ifmetric
             - ifupdown
             - vlan

The packages that are required for the type interfaces-installation.


**Configuration for type netplan**

.. zuul:rolevar:: network_netplan_required_packages
   :default: netplan.io

Package which is required for the type netplan-installation.

.. zuul:rolevar:: network_netplan_path
   :default: /etc/netplan

Directory to store the configuration file.

.. zuul:rolevar:: network_netplan_file
   :default: 01-osism.yaml

The configuration file for netplan.

.. zuul:rolevar:: network_netplan_permissions
   :default: 0644

To set the file permissions for netplan configuration files.

.. zuul:rolevar:: network_netplan_remove_unmanaged_files
   :default: true

Removing unused configuration files.

.. zuul:rolevar:: network_netplan_managed_files_defaults
   :default: network_netplan_file

Name of the used configuration file.

.. zuul:rolevar:: network_netplan_managed_files_extra
   :default: []

If there are more than one used configuration file, please declare it here.

.. zuul:rolevar:: network_netplan_managed_files
   :default: network_netplan_managed_files_defaults + network_netplan_managed_files_extra

The whole used configuration files.

.. zuul:rolevar:: network_version
   :default: 2

The 01-osism-file describes the network interfaces available on your system.
Network version is needed for the network declaration.

.. zuul:rolevar:: network_renderer
   :default: networkd

The Daemon that actually provides network functionality.

.. zuul:rolevar:: network_bonds

Netplan-bond configuration. For more information please look at the netplan documentation.

.. zuul:rolevar:: network_bridges

Netplan-bridges configuration. For more information please look at the netplan documentation.

.. zuul:rolevar:: network_ethernets

Netplan-ethernet configuration. For more information please look at the netplan documentation.

.. zuul:rolevar:: network_tunnels

Netplan-tunnels configuration. For more information please look at the netplan documentation.

.. zuul:rolevar:: network_vlans

Netplan-vlans configuration. For more information please look at the netplan documentation.

.. zuul:rolevar:: network_dispatcher_package_name
   :default: networkd-dispatcher

The required package for the networkd-dispatcher.

.. zuul:rolevar:: network_dispatcher_service_name
   :default: networkd-dispatcher

The service name from the dispatcher. This is needed to start the service.

.. zuul:rolevar:: network_dispatcher_scripts
   :default: []

Where the scripts for the dispatcher are stored and where it should be run.

Example:

.. code-block:: yaml

   - src: /opt/configuration/network/vxlan.sh
     dest: routable.d/vxlan.sh
   - src: /opt/configuration/network/iptables.sh
     dest: routable.d/iptables.sh


**Configuration lldpd**

.. zuul:rolevar:: network_lldpd
   :default: false

If you want to use lldpd set the value to true. The link layer discovery protocol is a protocol to discover networks in a lan.

.. zuul:rolevar:: network_lldpd_package_name
   :default: lldpd

The package name for lldpd.

.. zuul:rolevar:: network_lldpd_service_name
   :default: lldpd

The name of the service from lldpd.


**Configuration for the dummy interfaces**

.. zuul:rolevar:: network_dummy_interfaces
   :default: []

This is a interface to avoid error because ansible does not recognize. 

Example:

.. code-block:: yaml
   
   network_dummy_interfaces:
     - lo-bgp
     - lo-vxlan

.. zuul:rolevar:: network_dummy_interface_mtu
   :default: 9000

Maximum Transfer Unit. Please look which MTU fits for your system.
