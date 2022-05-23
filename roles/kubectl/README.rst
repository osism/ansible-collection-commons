This ansible role will install kubectl

**Role Variables**

.. zuul:rolevar:: kubectl_package_name
   :default: kubectl

The package what should be installed.

.. zuul:rolevar:: kubectl_configure_repository
   :default: true

Install apt-transport-https, because the kubectl repository can only be added via https.

.. zuul:rolevar:: kubectl_debian_repository_arch
   :default: amd64

Repository architecture.

.. zuul:rolevar:: kubectl_debian_repository_key
   :default: https://packages.cloud.google.com/apt/doc/apt-key.gpg

Add the repository gpg-key.

.. zuul:rolevar:: kubectl_debian_repository
   :default: "deb [ arch={{ kubectl_debian_repository_arch }} ] https://apt.kubernetes.io/ kubernetes-xenial main"

Define which repository you want to install.
