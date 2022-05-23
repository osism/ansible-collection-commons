Ansible role to configure distribution-specific repositories.

**Role Variables**

.. zuul:rolevar:: repositories

A dict of ``name:repository`` pairs, these will be added to the
list of package sources. The format and default settings are
distribution-specific.

.. zuul:rolevar:: repository_cache_valid_time
   :default: 120

Update the apt cache if it is older than the cache_valid_time.
This option is set in seconds.

.. zuul:rolevar:: repository_key_files_directory
   :default: /opt/configuration/environments/generic/files/repository/keys

Keys stored in this directory are added to APT as trusted keys.

.. zuul:rolevar:: repository_keys

List of URLs from which to collect GPG keys that APT should trust.

.. zuul:rolevar:: repository_key_ids

Dict of ``ID:keyserver`` pairs, each key ID is fetched from its
keyserver and added to APT as trusted key.
