Ansible role for configuring nameserver and its components.

**Role Variables**

.. zuul:rolevar:: resolvconf_nameserver_default
   :default: - 9.9.9.9
             - 149.112.112.112

The default IP addresses from the nameservers you want to choose for the configuration.

.. zuul:rolevar:: resolvconf_nameserver_extra

If you want to install extra nameservers declare it here.

.. zuul:rolevar:: resolvconf_nameserver

The whole list of nameservers you want to configure.

.. zuul:rolevar:: resolvconf_fallback_nameserver

Alternitive nameserver with IPv4 and IPv6 addresses in a list if no DNS server information is known.
If this option is not set, a compiled-in list is used instead.

.. zuul:rolevar:: resolvconf_search
   :default: osism.test

This is the local domain.

.. zuul:rolevar:: resolvconf_minimum_number_of_nameservers
   :default: 2

The minimum number of nameserver of name servers that must be configured.

.. zuul:rolevar:: resolvconf_cache
   :default: true

The cache for resolvconf. That means that requests are stored and takes the results from earlier requests.
This is for a better performance because not every request is a new network request.

.. zuul:rolevar:: resolvconf_cache_from_localhost
   :default: false

Sometimes in the case of development you will need to set the localhost cache on false.
For this you can use this parameter.

.. zuul:rolevar:: resolvconf_dns_over_tls
   :default: false

If true it will encrypted all connections, if false not. Please beware that you, if you want to use it, need a DNS server
that supports DNS-over-TLS. You need a valid certificate too. Using DNS-over-TLS results in a little performance loss.

.. zuul:rolevar:: resolvconf_dnssec
   :default: allow-downgrade

Does not enforce secured DNS requests. Fallback to normal (insecure) DNS is allowed. To enforce DNSSEC set this variable to true.
This will only work on systems where DNSSEC is supported. Using it results in a little perfomance loss.

.. zuul:rolevar:: resolvconf_read_etc_hosts
   :default: true

If set to true it allowes the systemd-resolved to read the /etc/hosts.

.. zuul:rolevar:: resolvconf_file
   :default: /etc/resolv.conf

Path to the configuration file.
