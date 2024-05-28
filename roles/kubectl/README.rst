This ansible role will install kubectl

**Role Variables**

Name of the kubctl package.

.. zuul:rolevar:: kubectl_configure_repository
   :default: true

Configure repository.

.. zuul:rolevar:: kubectl_debian_repository_arch
   :default: amd64

Repository architecture.

.. zuul:rolevar:: kubectl_debian_repository_key
   :default: https://raw.githubusercontent.com/kubernetes/k8s.io/main/apt/doc/apt-key.gpg

Repository gpg key.

.. zuul:rolevar:: kubectl_debian_repository
   :default: "deb [ arch={{ kubectl_debian_repository_arch }} signed-by=/usr/share/keyrings/kubectl.gpg ] https://apt.kubernetes.io/ kubernetes-xenial main"

Repository URL.
