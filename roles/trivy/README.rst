Ansible role for the trivy installation.
Trivy is a scanner for vulnerabilities in container images, file systems,
and git repositories, as well as for configuration issues and hard-coded secrets.

**Role Variables**

.. zuul:rolevar:: trivy_package_name
   :default: trivy

Name from the required package for the trivy installation.

.. zuul:rolevar:: trivy_configure_repository
   :default: true

The package which is needed for downloading packages via https.

.. zuul:rolevar:: trivy_debian_repository_arch
   :default: amd64

Architecture from the target system.

.. zuul:rolevar:: trivy_debian_repository_key
   :default: https://aquasecurity.github.io/trivy-repo/deb/public.key

The url from which you will get the package.

.. zuul:rolevar:: trivy_debian_repository
   :default: deb [ arch={{ trivy_debian_repository_arch }} ] https://aquasecurity.github.io/trivy-repo/deb {{ ansible_distribution_release }} main

Name of the trivy debian repository.
