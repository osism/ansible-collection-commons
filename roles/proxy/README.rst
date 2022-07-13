This ansible role will setup the proxies.

**Role Variables**

.. zuul:rolevar:: proxy_proxies
   :default: {}

The proxies which will be configured. Please declare which you want to configure.

Example:

.. code-block:: yaml
   
   proxy_proxies:
   http: http://proxy.tld:8080
   https: http://proxy.tld:8080
   ftp: http://proxy.tld:8080


.. zuul:rolevar:: proxy_no_proxy_default
   :default: - 127.0.0.1
             - localhost

The addresses listed here are not configured via proxy.

.. zuul:rolevar:: proxy_no_proxy_extra
   :default: []

Here you can list extra addresses which are not to be configured via proxy.

.. zuul:rolevar:: proxy_no_proxy
   :default: proxy_no_proxy_default + proxy_no_proxy_extra

All addresses which should not configured via proxy

.. zuul:rolevar:: proxy_package_manager
   :default: true

Also set proxy for the package manager.

.. zuul:rolevar:: proxy_apt_conf_path
   :default: /etc/apt/apt.conf.d/01proxy

Debain specific path. This path is where to store the configuration file.
