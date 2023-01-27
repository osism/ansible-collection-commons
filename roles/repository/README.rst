Ansible role to configure the default repository sources.

**Role Variables**

.. zuul:rolevar:: repositories
   :default: {}

A dict of ``name:repository`` pairs, these will be used as the
list of package sources. The format of the ``repository`` values
is distribution-specific.

If not set explicitly, some default repositories are configured.
For Ubuntu, these are mirrors of the ``main``, ``restricted``,
``universe`` and ``multiverse`` repositories for each of the
release, ``-backports``, ``-security`` and ``-updates`` pockets.

.. zuul:rolevar:: repository_cache_valid_time
   :default: 120

Only for Debian/Ubuntu:

Update the apt cache if it is older than the ``cache_valid_time``.
This option is set in seconds.

.. zuul:rolevar:: repository_key_files_directory
   :default: ""

Only for Debian/Ubuntu:

Keys stored in this directory are added to APT as trusted keys.

.. zuul:rolevar:: repository_keys

Only for Debian/Ubuntu:

List of URLs from which to collect GPG keys that APT should trust.

.. zuul:rolevar:: repository_key_ids

Only for Debian/Ubuntu:

Dict of ``ID:keyserver`` pairs, each key ID is fetched from its
keyserver and added to APT as trusted key.

.. zuul:rolevar:: enable_phased_updates
   :default: false

Only for Debian/Ubuntu:

Enable phased updates.
