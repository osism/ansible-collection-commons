An ansible role to install clevis library for network bound disk encryption.

**Role Variables**

.. zuul:rolevar:: clevis_packages
   :default: []

   The clevis required installation packages

.. zuul:rolevar:: clevis_tang_server
   :default: 127.0.0.1

   The tang server ip required create for tang clevis chain creation

.. zuul:rolevar:: clevis_tang_server_protocol
   :default: 80

   The tang server protocol port required create for tang clevis
   chain creation

.. zuul:rolevar:: clevis_tang_server_url
   :default: 80

   The tang server url required create for tang clevis chain creation

.. zuul:rolevar:: clevis_root_disk
   :default: /dev/sda1

   The crypt disk is required to create tang clevis chain creation

.. zuul:rolevar:: clevis_initial_luks_password
   :default: []

   The clevis_initial_luks_password is the install luks password
   which have chosen for image building procedure
