An ansible role to install and update CA certificates.

**Role Variables**

.. zuul:rolevar:: certificates_ca
   :default: []
   
   This is a list which contains the name and the certificate.

   .. zuul:rolevar:: name

   The name from the certificate file.

   Example:

   .. code-block:: yaml

      certificates_ca:
        - name: sample.crt
          certificate: |
            -----BEGIN CERTIFICATE-----
            [...]
            -----END CERTIFICATE-----

.. zuul:rolevar:: certificates_ca_path
   :default: /usr/local/share/ca-certificates

   The path where the certificates will be stored.

.. zuul:rolevar:: certificates_ca_package_name
   :default: ca-certificates

   The Debian package which is needed to install for the certificates.

.. zuul:rolevar:: certificates_ca_update_command
   :default: /usr/sbin/update-ca-certificates

   Command for updating the certificates.