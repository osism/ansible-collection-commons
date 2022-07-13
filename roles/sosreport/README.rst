This ansible role installs and configures sosreport. Sosreport helps to
collect informations from the configured plugins.

**Role Variables**

.. zuul:rolevar:: sosreport_unarchive
   :default: false

By default the sosreport will be unarchived on the destination machine
after running. 

.. zuul:rolevar:: sosreport_tmpdir
   :default: /tmp/sosreport

It is a temporary directory where the reports will be stored on the machine
where the report is generated.

.. zuul:rolevar:: sosreport_required_packages
   :default: sosreport

Required packages for sosreport.

.. zuul:rolevar:: sosreport_name 

The name will include by default the hostname and the date.
It is the name under which the report will be stored.

.. zuul:rolevar:: sosreport_archive_filename

This will be the name from the archived sosreport.

.. zuul:rolevar:: sosreport_archive_directory

The directory where the archived sosreports will be stored in.

.. zuul:rolevar:: sosreport_plugins
   :default: - apt
             - auditd
             - block
             - devices
             - docker
             - dpkg
             - filesys
             - hardware
             - kernel
             - kvm
             - md
             - memory
             - networking
             - pci
             - process
             - processor
             - python
             - services
             - ssh
             - system
             - systemd
             - ubuntu
             - udev
             - usb
             - xfs

From where sosreport should collect the informations which you needed.

.. zuul:rolevar:: operator_user
   :default: dragon

The user with which sosreport should run and own the reqired directories.

.. zuul:rolevar:: operator_group
   :default: operator_user

The group from the user with which sosreport should run and own the reqired directories.
