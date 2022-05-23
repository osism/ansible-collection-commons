This ansible role will install lynis.

**Role Variables**

.. zuul:rolevar:: lynis_package_name
   :default: lynis

The package that should be installed.

.. zuul:rolevar:: lynis_configure_repository
   :default: true

Whether to add the lynis_debian_repository to the apt configuration.

.. zuul:rolevar:: lynis_debian_repository_arch
   :default: amd64

Repository architecture.

.. zuul:rolevar:: lynis_debian_repository_key
   :default: https://packages.cisofy.com/keys/cisofy-software-public.key

Add the repository gpg-key.

.. zuul:rolevar:: lynis_debian_repository
   :default: "deb [ arch={{ lynis_debian_repository_arch }} ] https://packages.cisofy.com/community/lynis/deb/ stable main"

Define which repository you want to install.
