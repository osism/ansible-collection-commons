# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This file was started on December 16, 2020. Changes prior to this date are not included in the CHANGELOG.

## [v0.20260318.0] - 2026-03-18

### Added
- New `fast` type for the hosts role with pre-computed entries and single-render template, reducing complexity from O(N²) to O(N) (osism/ansible-collection-commons#838)

### Changed
- Cache hostvars per iteration in hosts template to improve rendering performance with large inventories (osism/ansible-collection-commons#837)

### Fixed
- Ansible 2.19 deprecation warning for int conditional in operator role (osism/ansible-collection-commons#836)

## [v0.20260312.0] - 2026-03-12

No changes.

## [v0.20260127.0] - 2026-01-27

### Added
- Optional network-extra-init service for running custom bridge and ip commands after network is ready

### Changed
- Remove automatic package installation for network-extra-init, leaving package management to the deployer (osism/ansible-collection-commons#833)

### Dependencies
- molecule 25.11.0 → 25.12.0 (osism/ansible-collection-commons#829, osism/ansible-collection-commons#831)
- pytest 8.4.2 → 9.0.2 (osism/ansible-collection-commons#824)
- actions/checkout v5 → v6 (osism/ansible-collection-commons#826)

## [v0.20251126.0] - 2025-11-26

### Changed
- Disable recursive git submodule cloning in configuration role to handle Netbox submodules separately (osism/ansible-collection-commons#827)
- Use dedicated template for Netbox git private key in configuration role (osism/ansible-collection-commons#828)
- Use ftp.uni-stuttgart.de as default Ubuntu mirror for HTTPS support and higher bandwidth (osism/ansible-collection-commons#830)

## [v0.20251121.0] - 2025-11-21

### Added
- Support for customizing the PS1 prompt in operator user's `.bashrc` with prepend and replace modes (osism/ansible-collection-commons#823)

### Dependencies
- molecule 25.9.0 → 25.11.0 (osism/ansible-collection-commons#825)

## [v0.20251022.0] - 2025-10-22

### Added
- Automatic CA certificate discovery from configuration directory in the certificates role (osism/ansible-collection-commons#817)
- vfio-pci module configuration support with `kernel_modules_vfio_pci_ids` parameter (osism/ansible-collection-commons#819)

### Changed
- Certificates role uses slurp and delegation to read certificates from the manager node before distributing to all nodes (osism/ansible-collection-commons#818)
- Kernel modules are now loaded with `persistent: present` option (osism/ansible-collection-commons#819)
- Use HTTPS instead of HTTP for all Debian/Ubuntu repository mirrors (osism/ansible-collection-commons#820)
- Use canonical `archive.ubuntu.com` instead of `de.archive.ubuntu.com` for Ubuntu x86_64 repositories (osism/ansible-collection-commons#820)

### Dependencies
- ansible 11.10.0 → 11.11.0 (osism/ansible-collection-commons#815)

## [v0.20251013.0] - 2025-10-13

### Changed
- Network role: add tags to be able to skip specific tasks (osism/ansible-collection-commons#816)

### Dependencies
- molecule 25.7.0 → 25.9.0 (osism/ansible-collection-commons#812)

## [v0.20250927.0] - 2025-09-27

### Added
- Set `net.netfilter.nf_conntrack_max = 1048576` on network nodes via sysctl role (osism/ansible-collection-commons#813)

### Changed
- Cleanup `.ansible-lint` file by removing unnecessary exclude paths and skip list entries (osism/ansible-collection-commons#808)

### Fixed
- Fix operator password check to use `length` filter instead of truthy evaluation (osism/ansible-collection-commons#814)

### Dependencies
- ansible 11.8.0 → 11.10.0 (osism/ansible-collection-commons#803)
- actions/setup-python v5 → v6 (osism/ansible-collection-commons#809)
- pytest 8.4.1 → 8.4.2 (osism/ansible-collection-commons#810)

## [v0.20250824.0] - 2025-08-24

### Added
- Support for `deb822_trusted` option in repository role (osism/ansible-collection-commons#805)

### Dependencies
- actions/checkout v4 → v5 (osism/ansible-collection-commons#802)

## [v0.20250823.0] - 2025-08-23

### Added
- Netbox submodule management for the configuration role with dedicated SSH key support (osism/ansible-collection-commons#804)

### Changed
- Add cosign secrets to Zuul CI configuration (osism/ansible-collection-commons#790)
- Document parameters for the motd role (osism/ansible-collection-commons#792)
- Update parameter documentation for the certificates role (osism/ansible-collection-commons#793)
- Document parameters for the cleanup role (osism/ansible-collection-commons#794)
- Add defaults file with documentation for the configfs role (osism/ansible-collection-commons#795)
- Document parameters for the configuration role (osism/ansible-collection-commons#796)
- Document parameters for the docker-compose role (osism/ansible-collection-commons#797)
- Document parameters for the docker-login role (osism/ansible-collection-commons#798)

### Fixed
- Fix Ansible 2.19 broken conditionals by adding explicit `> 0` comparisons to length filters in configuration, known_hosts roles (osism/ansible-collection-commons#800)

### Removed
- Remove Zuul gate pipeline (osism/ansible-collection-commons#789)

### Dependencies
- ansible 11.7.0 → 11.8.0 (osism/ansible-collection-commons#791)
- molecule 25.6.0 → 25.7.0 (osism/ansible-collection-commons#799)

## [v0.20250623.0] - 2025-06-23

### Added
- Support for defining custom environment variables for the operator user through the `operator_environment` parameter (osism/ansible-collection-commons#788)

### Dependencies
- pytest 8.3.5 → 8.4.1 (osism/ansible-collection-commons#784, osism/ansible-collection-commons#786)
- ansible 11.6.0 → 11.7.0 (osism/ansible-collection-commons#785)
- molecule 25.5.0 → 25.6.0 (osism/ansible-collection-commons#787)

## [v0.20250529.0] - 2025-05-29

### Added
- Zuul job for building and pushing osism-kubernetes image (osism/ansible-collection-commons#779)

### Changed
- Refreshed Zuul secrets (osism/ansible-collection-commons#781)
- Enhanced molecule tests for motd role with additional test cases for issue.net, SSH motd configuration, pam_motd, motd-news, and RedHat support (osism/ansible-collection-commons#782)

### Dependencies
- ansible 11.4.0 → 11.6.0 (osism/ansible-collection-commons#780)
- molecule 25.4.0 → 25.5.0 (osism/ansible-collection-commons#783)

## [v0.20250407.0] - 2025-04-07

### Added
- MACAddress support for VXLAN netdev in network role, defaults to "none" (osism/ansible-collection-commons#761)
- Configurable `no_log` option for configuration role via `configuration_no_log` (osism/ansible-collection-commons#776)
- `hostname_name` variable to allow overwriting the hostname in hostname role (osism/ansible-collection-commons#777)

### Changed
- Cleaned up ansible-lint configuration, removed unused rules directory and warn list (osism/ansible-collection-commons#771)

### Removed
- kubectl role, moved to osism/osism-kubernetes (osism/ansible-collection-commons#772)
- k9s role, moved to osism/osism-kubernetes (osism/ansible-collection-commons#773)

### Dependencies
- ansible 11.3.0 → 11.4.0 (osism/ansible-collection-commons#770)
- pytest-testinfra 10.1.1 → 10.2.2 (osism/ansible-collection-commons#775)
- molecule 25.3.1 → 25.4.0 (osism/ansible-collection-commons#778)

## [v0.20250310.0] - 2025-03-10

### Added
- Optional multicast group (`Group`) support for VXLAN netdev configuration (osism/ansible-collection-commons#762, osism/ansible-collection-commons#763)

### Changed
- VXLAN netdev MTU is now configurable, defaulting to 1500 (osism/ansible-collection-commons#765)
- VXLAN network BridgeFDB entries are now only rendered when `dests` is defined (osism/ansible-collection-commons#763)

### Dependencies
- ansible 11.2.0 → 11.3.0 (osism/ansible-collection-commons#759)
- derailed/k9s v0.40.3 → v0.40.6 (osism/ansible-collection-commons#757, osism/ansible-collection-commons#764)
- molecule 25.2.0 → 25.3.1 (osism/ansible-collection-commons#758)
- pytest 8.3.4 → 8.3.5 (osism/ansible-collection-commons#760)

## [v0.20250217.0] - 2025-02-17

### Added
- Handler to reload systemd-networkd after network unit file creation
- Optional address configuration for VXLAN interfaces
- Cleanup of unmanaged networkd configuration files with `network_networkd_remove_unmanaged_files` option
- Option to disable APT recommended/suggested packages via `repository_apt_install_recommends` and `repository_apt_install_suggests`

### Changed
- Restructured VXLAN interface definitions from array to dictionary format for more predictable file naming
- Renamed `enable_phased_updates` to `repository_apt_phased_updates` in the repository role
- Added `ANSIBLE_COLLECTIONS_PATH` to molecule provisioner environment (osism/ansible-collection-commons#750, osism/ansible-collection-commons#751)

### Fixed
- Fixed VXLAN networkd unit file names to use the `name` key instead of the dictionary object
- Fixed `ANSIBLE_COLLECTIONS_PATH` in molecule to include CentOS collections path (osism/ansible-collection-commons#751)

### Dependencies
- molecule 24.12.0 → 25.2.0 (osism/ansible-collection-commons#746)
- ansible 10.7.0 → 11.2.0 (osism/ansible-collection-commons#735)
- derailed/k9s v0.32.7 → v0.40.3 (osism/ansible-collection-commons#755, osism/ansible-collection-commons#756)

## [v0.20250127.0] - 2025-01-27

### Added
- Support for creating VXLAN interfaces via systemd-networkd netdev/network files (osism/ansible-collection-commons#745)
- Write issue.net file in motd role using the same template as motd

### Fixed
- Flake E712 linting issue in molecule resolvconf tests by using `is True` instead of `== True`

## [v0.20241219.0] - 2024-12-19

### Added
- Configurable `kubectl_version` parameter for the kubectl role (osism/ansible-collection-commons#742)

### Changed
- Update kubectl repository URLs from v1.30 to v1.32 and fix GPG key replacement to prevent validation issues (osism/ansible-collection-commons#741)

## [v0.20241206.0] - 2024-12-06

### Added
- Allow unsetting and locking the operator user password (osism/ansible-collection-commons#731)
- Add `fs.inotify.max_user_instances = 1024` sysctl default for k3s_node (osism/ansible-collection-commons#738)

### Changed
- Move configuration update tasks into a separate file (osism/ansible-collection-commons#729)
- Enhance sshconfig CI tests with SSH syntax check and connection test (osism/ansible-collection-commons#715)

### Fixed
- Fix typo in packages task name ("eackages" → "packages") (osism/ansible-collection-commons#730)

### Removed
- Remove clevis role (osism/ansible-collection-commons#736)

### Dependencies
- ansible 10.4.0 → 10.7.0 (osism/ansible-collection-commons#728, osism/ansible-collection-commons#732, osism/ansible-collection-commons#739)
- derailed/k9s v0.32.5 → v0.32.7 (osism/ansible-collection-commons#733, osism/ansible-collection-commons#734)
- pytest 8.3.3 → 8.3.4 (osism/ansible-collection-commons#737)
- molecule 24.9.0 → 24.12.0 (osism/ansible-collection-commons#740)

## [v0.20241006.0] - 2024-10-06

### Added
- `proxy_enable` parameter to allow disabling proxy configuration per host (osism/ansible-collection-commons#726)
- Package cleanup tasks (autoclean and autoremove) to the packages role (osism/ansible-collection-commons#725)

### Changed
- Repository role now supports Ubuntu 24.04 on ARM architecture with DEB822 format (osism/ansible-collection-commons#727)
- Enhanced CI tests for k9s, kubectl, lynis, and trivy (osism/ansible-collection-commons#721, osism/ansible-collection-commons#722, osism/ansible-collection-commons#723, osism/ansible-collection-commons#724)
- Removed Ubuntu 24.04 skip workaround for trivy installation and tests (osism/ansible-collection-commons#724)

### Fixed
- Renovate configuration for k9s version quoting (osism/ansible-collection-commons#719)

### Dependencies
- derailed/k9s v0.32.4 → v0.32.5 (osism/ansible-collection-commons#720)

## [v0.20240924.0] - 2024-09-24

### Changed
- Manage the k9s version with Renovate (osism/ansible-collection-commons#710)
- Enhance CI tests for the Podman role (osism/ansible-collection-commons#714)
- Do not force installation of Ansible requirements in molecule (osism/ansible-collection-commons#716)
- Enhance CI tests for the resolvconf role (osism/ansible-collection-commons#717)
- Enhance CI tests for the docker-compose role (osism/ansible-collection-commons#718)

### Fixed
- Fix clevis role and add tests (osism/ansible-collection-commons#708)

### Dependencies
- pytest 8.3.2 → 8.3.3 (osism/ansible-collection-commons#711)
- ansible 10.3.0 → 10.4.0 (osism/ansible-collection-commons#712)
- molecule 24.8.0 → 24.9.0 (osism/ansible-collection-commons#713)

## [v0.20240907.0] - 2024-09-07

### Added
- Install `git` package by default to support executing prepared plays directly on nodes and managing static configurations via Git (osism/ansible-collection-commons#707)
- Install `bash-completion` package by default (osism/ansible-collection-commons#709)

### Changed
- Use CentOS instead of RHEL in certificates task name (osism/ansible-collection-commons#706)

## [v0.20240825.0] - 2024-08-25

### Added
- Install `isc-dhcp-client` package on Debian/Ubuntu, required by octavia-interface.service (osism/ansible-collection-commons#698)
- Package download-only step before installing or upgrading packages on Debian and RedHat (osism/ansible-collection-commons#702)
- Automatic host facts update when hostname changes (osism/ansible-collection-commons#705)

### Changed
- Add `needrestart` tags to packages role tasks (osism/ansible-collection-commons#700)
- Add `download` and `upgrade` tags to packages role tasks (osism/ansible-collection-commons#702)
- Add `dnf_lock_timeout` to all `ansible.builtin.dnf` tasks in packages role (osism/ansible-collection-commons#704)
- Only update package cache on CentOS without installing new packages (osism/ansible-collection-commons#703)

### Fixed
- Add missing `needrestart` tag to package task include (osism/ansible-collection-commons#701)

## [v0.20240818.1] - 2024-08-18

### Fixed
- Network role now only uses dummy-devices on Ubuntu >= 24.04, as they require netplan >= 0.107 (osism/ansible-collection-commons#696)
- Network role now skips the "Warning when used on Ubuntu >= 22.04" task on Debian (osism/ansible-collection-commons#697)

## [v0.20240818.0] - 2024-08-18

### Added
- Support for dummy devices in network role via `network_dummy_devices` (osism/ansible-collection-commons#692)
- Configurable needrestart mode in packages role via `packages_needrestart_mode` (osism/ansible-collection-commons#693)

### Changed
- Add DTRACK_API_KEY secret to Zuul configuration (osism/ansible-collection-commons#695)

### Dependencies
- ansible 10.2.0 → 10.3.0 (osism/ansible-collection-commons#691)
- molecule 24.7.0 → 24.8.0 (osism/ansible-collection-commons#694)

## [v0.20240812.0] - 2024-08-12

### Added
- lvm2 to required_packages_default (osism/ansible-collection-commons#687)
- ansible-collection-ensure-readme job to Zuul CI pipeline (osism/ansible-collection-commons#690)

### Removed
- Old and out-of-date README files from roles (osism/ansible-collection-commons#689)

### Dependencies
- pytest 8.3.1 → 8.3.2 (osism/ansible-collection-commons#688)

## [v0.20240723.0] - 2024-07-23

### Added
- Missing EPEL repository in molecule prepare for docker_login (osism/ansible-collection-commons#681)

### Changed
- Replace `ansible.builtin.package` with OS-specific package managers (`dnf`/`apt`) in docker_login role (osism/ansible-collection-commons#684)
- Require ansible >= 2.16 and remove upper version constraint (osism/ansible-collection-commons#685)

### Dependencies
- molecule 24.6.1 → 24.7.0 (osism/ansible-collection-commons#679)
- ansible 9.7.0 → 10.2.0 (osism/ansible-collection-commons#676)
- pytest 8.2.2 → 8.3.1 (osism/ansible-collection-commons#686)

## [v0.20240710.0] - 2024-07-10

### Added
- `resolvconf_maximum_number_of_nameservers` parameter to limit the number of configured nameservers (default: 3), preventing issues with Kubernetes/K3s (osism/ansible-collection-commons#677)

### Dependencies
- molecule 24.6.0 → 24.6.1 (osism/ansible-collection-commons#678)

## [v0.20240702.0] - 2024-07-02

### Added
- EPEL repository is now added by default in the repository role for RedHat family distributions (osism/ansible-collection-commons#659)
- Allow setting user passwords via the `user_list` variable in the user role (osism/ansible-collection-commons#672)

### Changed
- Rename `lock_timeout` variable to `dnf_lock_timeout` across all roles using DNF (osism/ansible-collection-commons#660)
- Use `osism.commons.repository` role to add EPEL repository in molecule tests instead of inline tasks (osism/ansible-collection-commons#661)
- Use pre-defined repositories for CentOS, AlmaLinux, and Rocky instead of custom defaults; add missing "Update package cache" task for RedHat family (osism/ansible-collection-commons#663)
- Move `apt_cache_valid_time` default variable setup from main tasks to Debian-specific tasks in the packages role (osism/ansible-collection-commons#670)
- Do not set `ansible_python_interpreter` in molecule configuration (osism/ansible-collection-commons#674)
- Support Ansible version 2.17 in collection metadata (osism/ansible-collection-commons#675)

### Fixed
- Fix repository role for RedHat family: add length checks for mirrorlist/metalink entries, improve test names and logic (osism/ansible-collection-commons#662)
- Use HTTPS for CentOS mirrorlist URLs (osism/ansible-collection-commons#662)

### Removed
- Remove kompose role (osism/ansible-collection-commons#669)

### Dependencies
- pytest 8.2.1 → 8.2.2 (osism/ansible-collection-commons#664)
- molecule 24.2.1 → 24.6.0 (osism/ansible-collection-commons#666)
- ansible 9.6.0 → 9.7.0 (osism/ansible-collection-commons#667, osism/ansible-collection-commons#673)

## [v0.20240531.0] - 2024-05-31

### Added
- New k9s role for installing the k9s Kubernetes CLI tool (osism/ansible-collection-commons#658)
- `user_sudoers_type` parameter to the user role to support user or group sudoers rules (osism/ansible-collection-commons#651)
- `motd_show_ssh` parameter to configure PrintMotd in sshd_config (osism/ansible-collection-commons#657)
- python3-kubernetes package to kubectl role on Debian-based distros (osism/ansible-collection-commons#656)

### Changed
- kubectl role now uses v1.30 package repositories instead of v1.28 (osism/ansible-collection-commons#655)
- kubectl role refactored to use distro-specific required packages via OS family variables (osism/ansible-collection-commons#654)
- Configuration role now sets directory permissions to 0770 and uses umask for git operations (osism/ansible-collection-commons#653)

### Dependencies
- pytest-testinfra 10.1.0 → 10.1.1 (osism/ansible-collection-commons#652)

## [v0.20240524.0] - 2024-05-24

### Added
- Allow deletion of authorized keys via `operator_authorized_keys_delete` and `operator_authorized_github_accounts_delete` in operator role (osism/ansible-collection-commons#641)
- Allow deletion of known_hosts entries via `known_hosts_delete` in known_hosts role (osism/ansible-collection-commons#642)
- Shortcut to fetch SSH keys from GitHub by setting `key: github` in user role (osism/ansible-collection-commons#647)
- `user_sudoers` parameter to customize sudoers file content in user role (osism/ansible-collection-commons#646)
- `user_primary_group` parameter to change primary group for users in user role (osism/ansible-collection-commons#645)

### Changed
- Overhauled user role: replaced `user_manage_type` with `user_type`, added support for additional user groups, static and remote authorized keys, loop labels, and restructured task files (osism/ansible-collection-commons#643)
- Proxy role now removes system-wide proxy settings from `/etc/environment` when no proxies are defined (osism/ansible-collection-commons#648)
- Allow skipping "Ensure config for each host exist" task in sshconfig role when `sshconfig_private_key_file` is empty (osism/ansible-collection-commons#639)
- Cleaned up README by removing inline role table, pointing to external documentation (osism/ansible-collection-commons#644)
- Migrated certificates role documentation out of repository (osism/ansible-collection-commons#640)
- Removed release notes in favor of central management in osism/release and osism/osism.github.io (osism/ansible-collection-commons#650)

### Fixed
- Cleanup of unmanaged netplan files on Debian/Ubuntu in network role (osism/ansible-collection-commons#637)
- Handling of remote SSH key downloads in user role (osism/ansible-collection-commons#649)

### Dependencies
- pytest 8.2.0 → 8.2.1 (osism/ansible-collection-commons#636)
- ansible 9.5.1 → 9.6.0 (osism/ansible-collection-commons#638)

## [v0.20240503.0] - 2024-05-03

### Added
- Testing on Ubuntu 24.04 (Noble) in Zuul CI (osism/ansible-collection-commons#619)

### Changed
- Updated platforms (add Ubuntu Noble, Debian Bookworm, EL 9; remove Ubuntu Focal, EL 8) and bumped `min_ansible_version` to 2.16.0 across all roles (osism/ansible-collection-commons#621)
- Synced default packages with osism/defaults, adding curl, dmidecode, iotop, and more (osism/ansible-collection-commons#628)
- Synced cleanup defaults with osism/defaults, adding ModemManager service cleanup and additional packages (osism/ansible-collection-commons#633)
- Use prefix variables for OS-specific defaults in operator role (osism/ansible-collection-commons#626)
- Use prefix variables for OS-specific defaults in repository role (osism/ansible-collection-commons#627)
- Use prefix variables for OS-specific defaults in packages role (osism/ansible-collection-commons#629)
- Use prefix variables for OS-specific defaults in cleanup role (osism/ansible-collection-commons#632)
- Moved `certificates_ca_package_name` parameter to OS-specific vars (osism/ansible-collection-commons#634)
- Added comment about `.crt` extension importance in certificates role (osism/ansible-collection-commons#635)
- Renamed network dispatcher task from "Enable" to "Manage" (osism/ansible-collection-commons#631)
- Removed mocked modules from ansible-lint configuration (osism/ansible-collection-commons#624)
- Zuul CI now uses ubuntu-jammy nodes instead of ubuntu-jammy-large (osism/ansible-collection-commons#620)

### Fixed
- Fixed failed Ubuntu 24.04 tests by skipping trivy installation/tests where repository is not yet available (osism/ansible-collection-commons#630)
- Fixed resolvconf test to skip gracefully when the service does not exist (osism/ansible-collection-commons#630)
- Added `util-linux-extra` package installation for Ubuntu 24.04 in systohc role (osism/ansible-collection-commons#630)
- Replaced deprecated `yes`/`no` values with `true`/`false` in YAML files across multiple roles (osism/ansible-collection-commons#630)

### Dependencies
- pytest 8.1.1 → 8.2.0 (osism/ansible-collection-commons#623, osism/ansible-collection-commons#625)
- ansible 9.4.0 → 9.5.1 (osism/ansible-collection-commons#622)

## [v0.20240417.0] - 2024-04-17

### Added
- Debian support for roles trivy, timezone, sosreport, resolvconf, motd, microcode, kubectl, lynis, docker-compose, network, and repository
- VRF support in netplan configuration (osism/ansible-collection-commons#616)

### Changed
- Renamed OS-family and distribution specific task/var files to use `-family` and `-dist` suffixes
- Enabled Debian testing for all CI jobs
- Refactored test utilities to use `get_family_role_variable` and `get_dist_role_variable` helpers
- Removed deprecated `apt-key` usage from roles lynis, trivy, and repository

### Fixed
- Fixed docker_compose molecule repo integration for ARM-based systems (osism/ansible-collection-commons#612)
- Fixed unescaped dots in .zuul.yaml regex patterns (osism/ansible-collection-commons#615)

### Dependencies
- ansible 9.3.0 → 9.4.0 (osism/ansible-collection-commons#611)
- molecule 24.2.0 → 24.2.1 (osism/ansible-collection-commons#617)

## [v0.20240327.0] - 2024-03-27

### Added
- RHEL support for the network role with interfaces and netplan task variants (osism/ansible-collection-commons#599)
- Tests for network, user, and sshconfig roles (osism/ansible-collection-commons#599)
- CentOS test for the repository role (osism/ansible-collection-commons#599)
- Support for static known_hosts entries via `known_hosts` host variable (osism/ansible-collection-commons#610)
- Support for extra known_hosts entries via `known_hosts_extra` variable (osism/ansible-collection-commons#610)

### Changed
- Replaced `osism.github.io` with `osism.tech` in documentation URLs (osism/ansible-collection-commons#608)
- Replaced `ansible.builtin.yum` with `ansible.builtin.dnf` in RedHat tasks for docker_compose, kompose, and kubectl roles (osism/ansible-collection-commons#599)
- Refactored `docker_login` and `resolvconf` CI jobs to use abstract parent job (osism/ansible-collection-commons#599)
- Simplified molecule prepare files by removing redundant package cache updates (osism/ansible-collection-commons#599)
- Refactored resolvconf role with OS-family-specific install and configure tasks for Debian and RedHat (osism/ansible-collection-commons#599)
- Moved network role OS-specific variables from defaults to `vars/Debian.yml` and `vars/RedHat.yml` (osism/ansible-collection-commons#599)
- Refactored known_hosts role to avoid duplicate entries and comments in destination file (osism/ansible-collection-commons#610)

### Removed
- Removed `known_hosts` README.rst (osism/ansible-collection-commons#610)

## [v0.20240319.0] - 2024-03-19

### Added
- Allow extra SSH config via `sshconfig_extra` variable in sshconfig role (osism/ansible-collection-commons#604)
- Support for CentOS-based distributions across multiple roles (osism/ansible-collection-commons#585)

### Changed
- Refactored Zuul molecule jobs to use a new `abstract-ansible-collection-commons-molecule` parent job, reducing duplication across all role test definitions (osism/ansible-collection-commons#605)

### Fixed
- Fixed typo in Zuul file pattern for configuration role (`configuraion` → `configuration`) (osism/ansible-collection-commons#605)

## [v0.20240311.0] - 2024-03-11

### Changed
- Update links to documentation (osism/ansible-collection-commons#600)

### Dependencies
- pytest 8.1.0 → 8.1.1 (osism/ansible-collection-commons#601)

## [v0.20240307.0] - 2024-03-07

### Dependencies

- pytest 8.0.1 → 8.1.0 (osism/ansible-collection-commons#596, osism/ansible-collection-commons#598)
- ansible 9.2.0 → 9.3.0 (osism/ansible-collection-commons#597)

## [v0.20240221.0] - 2024-02-21

### Added
- Tasks to remove old architecture-dependent repository for kubectl, lynis, and trivy (osism/ansible-collection-commons#586)
- Zuul job to push osism-ansible container image (osism/ansible-collection-commons#594)

### Changed
- Remove kubectl symlink in /usr/local/bin (osism/ansible-collection-commons#593)

### Fixed
- kubectl: fix "gpg: cannot open '/dev/tty': No such device or address" by adding `--batch --no-tty` flags (osism/ansible-collection-commons#591)

### Removed
- Remove molecule/default directory (osism/ansible-collection-commons#589)

### Dependencies
- molecule 6.0.3 → 24.2.0 (osism/ansible-collection-commons#588)
- pytest-testinfra 10.0.0 → 10.1.0 (osism/ansible-collection-commons#592)
- pytest 8.0.0 → 8.0.1 (osism/ansible-collection-commons#595)

## [v0.20240204.0] - 2024-02-04

### Added
- `still_alive` callback plugin: add `v2_playbook_on_handler_task_start` support (osism/ansible-collection-commons#567)
- Missing testinfra tests for docker_login, known_hosts, limits, vault_import, vault_init, vault_seal, and vault_unseal roles (osism/ansible-collection-commons#541)
- Molecule test jobs for docker_login, known_hosts, limits, vault_import, vault_init, vault_seal, and vault_unseal roles (osism/ansible-collection-commons#541)
- Prepared variables support in molecule converge and prepare steps (osism/ansible-collection-commons#541)
- User role for managing admin accounts and SSH access on systems (osism/ansible-collection-commons#532)
- user: Add missing README.md file required by Ansible Galaxy (osism/ansible-collection-commons#584)
- Dynamic architecture resolution (amd64, arm64, arm) for kompose, kubectl, lynis, and trivy roles (osism/ansible-collection-commons#570)

### Changed
- Refactored Zuul CI job file filters from project-level to job-level definitions (osism/ansible-collection-commons#541)
- Updated ansible-lint mock modules to use fully qualified collection names for hashivault (osism/ansible-collection-commons#541)
- Repository role uses `loop_control` with `extended` option (osism/ansible-collection-commons#573)
- Kubectl repository switched to new `pkgs.k8s.io` package source (osism/ansible-collection-commons#570)
- Lynis and trivy repository configurations no longer hardcode architecture (osism/ansible-collection-commons#570)
- resolvconf: Replace `ansible.posix.synchronize` and rsync with native copy, remove resolvconf/openresolv packages instead of stopping service (osism/ansible-collection-commons#578)
- motd: Disable the dynamic MOTD news service via configuration file instead of stopping services (osism/ansible-collection-commons#579)
- motd: Use `community.general.pamd` for PAM configuration changes in `/etc/pam.d` (osism/ansible-collection-commons#582)

### Fixed
- `known_hosts`: fix `groups` variable reference (was `group`) in defaults (osism/ansible-collection-commons#568)
- Re-add accidentally removed `clevis` role (osism/ansible-collection-commons#569)
- Network role checks if `/etc/network` directory exists before writing interfaces file on pure netplan systems (osism/ansible-collection-commons#576)
- Check whether variable is defined before use in motd and network roles (osism/ansible-collection-commons#583)

### Removed
- Vault roles (`vault_import`, `vault_init`, `vault_seal`, `vault_unseal`) and all associated molecule tests and CI jobs (osism/ansible-collection-commons#571)

### Dependencies
- actions/setup-python v4 → v5 (osism/ansible-collection-commons#561)
- ansible 8.7.0 → 9.2.0 (osism/ansible-collection-commons#557, osism/ansible-collection-commons#580)
- pytest 7.4.4 → 8.0.0 (osism/ansible-collection-commons#575)

## [v0.20240104.0] - 2024-01-04

### Added
- `still_alive` callback stdout plugin that displays a banner every 30 seconds when a task is running more than 120 seconds (osism/ansible-collection-commons#565)

### Fixed
- Reduce permissions on `/etc/netplan/01-osism.yaml` from 0644 to 0600 to avoid "Permissions are too open" warnings

### Dependencies
- ansible 8.6.1 → 8.7.0 (osism/ansible-collection-commons#560)
- molecule 6.0.2 → 6.0.3 (osism/ansible-collection-commons#562)
- pytest 7.4.3 → 7.4.4 (osism/ansible-collection-commons#563)

## [v0.20231126.0] - 2023-11-26

### Added
- `operator_authorized_github_accounts` parameter for the operator role to add SSH public keys from GitHub accounts to authorized keys
- New `limits` role for managing PAM limits via `osism.commons.limits` (osism/ansible-collection-commons#536)
- Systemd `osism.target` for docker_compose to allow starting/stopping all OSISM services at once (osism/ansible-collection-commons#534)
- `molecule/requirements.txt` to matching files for all Zuul test jobs (osism/ansible-collection-commons#b6671ce)
- Molecule unit tests with Testinfra for role verification (osism/ansible-collection-commons#528)
- `operator_authorized_keys_minimal` parameter to enforce a minimum number of SSH authorized keys in the operator role (osism/ansible-collection-commons#554)
- flake8 and python-black linting jobs to CI pipeline (osism/ansible-collection-commons#528)

### Changed
- Migrated molecule test workflows from GitHub Actions to Zuul (osism/ansible-collection-commons#520)
- Use `netplan` as default network type instead of `interfaces` in the network role (osism/ansible-collection-commons#539)
- Use systemd service type `simple` instead of `oneshot` for Docker Compose units (osism/ansible-collection-commons#535)
- Simplify limits role configuration to use `item.key` as domain directly (osism/ansible-collection-commons#537)
- Shorten Zuul job names by removing redundant `ansible-` prefix (osism/ansible-collection-commons#527)
- Use molecule driver name `default` instead of `delegated` (osism/ansible-collection-commons#b6671ce)
- Migrate documentation from Sphinx/RST to osism.github.io for services, sshconfig, packages, timezone, network, and sysctl roles (osism/ansible-collection-commons#544) (osism/ansible-collection-commons#545) (osism/ansible-collection-commons#550) (osism/ansible-collection-commons#553)
- Remove Sphinx docs build infrastructure, documentation now hosted at osism.github.io (osism/ansible-collection-commons#546)
- Check checksum of docker-compose binary before removal to avoid unnecessary reinstalls (osism/ansible-collection-commons#551)
- Allow use of ansible-core 2.16 by extending version constraint to `<2.17.0` (osism/ansible-collection-commons#559)
- Remove sosreport Molecule job from CI pipeline (osism/ansible-collection-commons#528)

### Fixed
- Incorrect `ansible_role` variables in Zuul job definitions
- Use `ansible_distribution_version` instead of `ansible_distribution` for version comparison in network role (osism/ansible-collection-commons#543)
- Only check for key files in repository role when a manager group exists (osism/ansible-collection-commons#530)
- Fix yamllint trailing whitespace issues in `.zuul.yaml` (osism/ansible-collection-commons#529)
- Change permissions of netplan configuration file from 0644 to 0600 (osism/ansible-collection-commons#548)

### Dependencies
- molecule 5.1.0 → 6.0.2 (osism/ansible-collection-commons#511)
- ansible 8.4.0 → 8.6.1 (osism/ansible-collection-commons#531) (osism/ansible-collection-commons#549) (osism/ansible-collection-commons#552)
- pytest 7.4.0 → 7.4.3 (osism/ansible-collection-commons#555)
- pytest-testinfra 8.1.0 → 10.0.0 (osism/ansible-collection-commons#556)

## [v0.20230919.0] - 2023-09-19

No changes.

## [v0.20230915.0] - 2023-09-15

### Changed
- Link to new docs website in galaxy.yml (osism/ansible-collection-commons#523)

### Dependencies
- ansible 8.3.0 → 8.4.0 (osism/ansible-collection-commons#522)
- docker/setup-buildx-action v2 → v3 (osism/ansible-collection-commons#521)

## [v0.20230906.0] - 2023-09-06

### Fixed
- Fix typo in docker_compose task name ("Unnstall" → "Uninstall") (osism/ansible-collection-commons#516)
- Fix missing backtick in network role version comparison (osism/ansible-collection-commons#519)

### Dependencies
- actions/checkout v3 → v4 (osism/ansible-collection-commons#517)
- actions/checkout v3 → v4 (osism/ansible-collection-commons#518)

## [v0.20230901.0] - 2023-09-01

### Added
- Add configurable image pull in docker_compose service via `docker_compose_pull` flag
- Add task to start and enable systemd-resolved service in resolvconf role
- Add warning when interfaces type is used on Ubuntu >= 22.04 (osism/ansible-collection-commons#509)
- Add flag to use FQDN as hostname in hostname role (osism/ansible-collection-commons#513)

### Changed
- Use C.UTF-8 instead of en_US.UTF-8 as locale in operator role (osism/ansible-collection-commons#515)

### Fixed
- Fix kubectl repository file permissions from 0600 to 0644
- Fix missing ubuntu-22.04.yml vars file for interfaces network type (osism/ansible-collection-commons#508)
- Fix use of debug module without FQCN in network role (osism/ansible-collection-commons#510)
- Fix typo in resolvconf task name ("Stopp" → "Stop")

### Dependencies
- ansible 8.2.0 → 8.3.0 (osism/ansible-collection-commons#514)

## [v0.20230722.0] - 2023-07-22

### Added
- Support for Debian in the repository role by adding Debian.yml vars file

### Changed
- Rework ansible-lint noqas from numbers to names and adjust positions for better visibility (osism/ansible-collection-commons#496)
- Run "Check if the keys directory exists" task only once in the repository role

### Fixed
- Pin Sphinx version to 6.2.1 to fix broken documentation build pipeline

### Dependencies
- ansible 8.0.0 → 8.1.0 (osism/ansible-collection-commons#499)
- ansible 8.1.0 → 8.2.0 (osism/ansible-collection-commons#501)
- molecule 5.0.1 → 5.1.0 (osism/ansible-collection-commons#500)

## [v0.20230614.0] - 2023-06-14

### Changed
- Add mock modules for community.docker and hashivault in ansible-lint configuration (osism/ansible-collection-commons#484)
- Enable fqcn-builtins ansible-lint rule (osism/ansible-collection-commons#485)
- Ignore var-naming[no-role-prefix] ansible-lint rule (osism/ansible-collection-commons#486)
- Enable var-spacing ansible-lint rule and fix Jinja2 variable spacing across all roles (osism/ansible-collection-commons#487)
- Enable parser-error ansible-lint rule (osism/ansible-collection-commons#489)
- Enable `name[template]` ansible-lint rule and adjust task names to comply (osism/ansible-collection-commons#490)
- Update supported Ansible versions to `>=2.14.0,<2.16.0` (osism/ansible-collection-commons#495)

### Fixed
- Rename `hosts` register variable to `hosts_entries` to fix ansible-lint pipeline (osism/ansible-collection-commons#494)

### Removed
- Remove Ubuntu 20.04 from CI test matrix (osism/ansible-collection-commons#488)

### Dependencies
- ansible 7.4.0 → 8.0.0 (osism/ansible-collection-commons#483, osism/ansible-collection-commons#492, osism/ansible-collection-commons#493)
- molecule 4.0.4 → 5.0.1 (osism/ansible-collection-commons#482)

## [v0.20230407.0] - 2023-04-07

### Added
- Periodic-daily jobs (yamllint, ansible-lint) in Zuul for better visibility of linter errors (osism/ansible-collection-commons#481)

### Fixed
- Ansible-lint syntax errors by adding `changed_when: true` to handlers in certificates, clevis, and network roles (osism/ansible-collection-commons#479)

### Dependencies
- molecule 4.0.3 → 4.0.4 (osism/ansible-collection-commons#480)
- ansible 7.3.0 → 7.4.0 (osism/ansible-collection-commons#478)

## [v0.20230312.0] - 2023-03-12

### Removed
- "Wait for apt lock" tasks from certificate role (osism/ansible-collection-commons#459)
- "Wait for apt lock" tasks from cleanup role (osism/ansible-collection-commons#460)
- "Wait for apt lock" tasks from clevis role (osism/ansible-collection-commons#461)
- "Wait for apt lock" tasks from configuration role (osism/ansible-collection-commons#462)
- "Wait for apt lock" tasks from docker_compose role (osism/ansible-collection-commons#463)
- "Wait for apt lock" tasks from docker_login role (osism/ansible-collection-commons#464)
- "Wait for apt lock" tasks from ipmitool role (osism/ansible-collection-commons#465)
- "Wait for apt lock" tasks from kompose role (osism/ansible-collection-commons#466)
- "Wait for apt lock" tasks from kubectl role (osism/ansible-collection-commons#467)
- "Wait for apt lock" tasks from lynis role (osism/ansible-collection-commons#468)
- "Wait for apt lock" tasks from microcode role (osism/ansible-collection-commons#469)
- "Wait for apt lock" tasks from motd role (osism/ansible-collection-commons#470)
- "Wait for apt lock" tasks from network role (osism/ansible-collection-commons#471)
- "Wait for apt lock" tasks from packages role (osism/ansible-collection-commons#472)
- "Wait for apt lock" tasks from repository role (osism/ansible-collection-commons#473)
- "Wait for apt lock" tasks from runc role (osism/ansible-collection-commons#474)
- "Wait for apt lock" tasks from sysdig role (osism/ansible-collection-commons#475)
- "Wait for apt lock" tasks from timezone role (osism/ansible-collection-commons#476)
- "Wait for apt lock" tasks from trivy role (osism/ansible-collection-commons#477)

## [v0.20230308.0] - 2023-03-08

### Changed
- Repository role now only handles `*.gpg` files in "Add repository keys via files" task (osism/ansible-collection-commons#458)

## [v0.12.0] - 2023-03-06

### Changed
- Set apt lock timeout to 300 seconds by default for all apt operations (osism/ansible-collection-commons#455)
- Replace deprecated `apt-key` with `get_url`/`copy` for GPG key management on Ubuntu 22.04+ (osism/ansible-collection-commons#456)
- Change default container registry from `index.docker.io` to `registry.airgap.services.osism.tech` (osism/ansible-collection-commons#451)

## [v0.11.0] - 2023-03-01

### Added
- New `docker_login` role for logging in to a registry independently of the docker role (osism/ansible-collection-commons#431)
- New `runc` role for setting up runc (osism/ansible-collection-commons#386)
- Add `update-configuration` tag to configuration role git clone tasks (osism/ansible-collection-commons#418)
- Repository role: add `enable_phased_updates` parameter to control phased updates on Debian/Ubuntu (osism/ansible-collection-commons#435)
- `repository_apt_acquire_forceipv4` option to force IPv4 transport with apt-get (osism/ansible-collection-commons#452)
- Motd role: also write `motd_content` into `/etc/issue` (osism/ansible-collection-commons#426)

### Changed
- Replace docker-compose package with Docker Compose plugin and add compatibility wrapper script (osism/ansible-collection-commons#428)
- Hosts role: use `internal_interface` instead of `management_interface` as default fallback (osism/ansible-collection-commons#433)
- Set default `resolvconf_minimum_number_of_nameservers` to 1 (osism/ansible-collection-commons#445)
- Replace `ansible.builtin.copy` with `ansible.builtin.template` in certificates, clevis, configuration, hostname, motd, and sysdig roles
- Refactor ansible-lint rules configuration after version update (osism/ansible-collection-commons#405)
- Add experimental rules to ansible-lint warn list (osism/ansible-collection-commons#415)
- Ansible-lint: skip `galaxy[no-changelog]` rule (osism/ansible-collection-commons#429)
- Use `.ansible-lint-rules` provided by ansible-lint zuul job instead of bundled custom rules (osism/ansible-collection-commons#444)
- Fix ansible-lint configuration issues for zuul rebuilds and add galaxy tags (osism/ansible-collection-commons#449)
- Transfer ansible-lint check from GitHub Actions to Zuul (osism/ansible-collection-commons#438)
- Remove check-yaml-syntax GitHub Action in favor of Zuul (osism/ansible-collection-commons#440)
- Replace tox-linters with yamllint in Zuul configuration (osism/ansible-collection-commons#443)
- Add squash-merge mode to Zuul configuration (osism/ansible-collection-commons#442)
- Migrate molecule tests from default to delegated driver (osism/ansible-collection-commons#419, osism/ansible-collection-commons#422, osism/ansible-collection-commons#423, osism/ansible-collection-commons#424, osism/ansible-collection-commons#425)
- Use Python 3.10 for test-role GitHub Actions (osism/ansible-collection-commons#439)
- Network role: set `changed_when: false` for localhost-delegated tasks that do not change the target host
- Add Ubuntu Jammy (22.04) to list of supported platforms across all roles (osism/ansible-collection-commons#450)
- Update required Ansible version upper bound to `<2.15.0` (osism/ansible-collection-commons#454)

### Fixed
- Configuration role: add missing `update-configuration` tags to git tasks (osism/ansible-collection-commons#427)
- Check if `hosts_interface` is defined before accessing IPv4 address in hosts template (osism/ansible-collection-commons#434)
- Timezone role: fix ansible-lint `args[module]` warning for hwclock variable (osism/ansible-collection-commons#416)
- Fix Jinja2 filter spacing in proxy role RedHat tasks
- Fix configuration test by using delegated driver and updating operator user (osism/ansible-collection-commons#425)
- Fix molecule test pipelines and update Ansible version in CI (osism/ansible-collection-commons#419)

### Removed
- Remove lldpd tasks from network role in favor of `osism.services.lldpd`
- Revert VRF support in network role due to Ubuntu 20.04 incompatibility (osism/ansible-collection-commons#436)
- Remove docker_compose test workflow (osism/ansible-collection-commons#419)

### Dependencies
- ansible 6.3.0 → 7.3.0 (osism/ansible-collection-commons#403, osism/ansible-collection-commons#408, osism/ansible-collection-commons#411, osism/ansible-collection-commons#419, osism/ansible-collection-commons#453)
- molecule 4.0.0 → 4.0.3 (osism/ansible-collection-commons#382, osism/ansible-collection-commons#409)
- molecule-docker 1.1.0 → 2.1.0 (osism/ansible-collection-commons#381)

## [v0.10.0] - 2022-09-03

### Added
- Documentation for timezone, trivy, vault_import, vault_init, vault_seal, and vault_unseal roles (osism/ansible-collection-commons#358)
- Documentation for network role (osism/ansible-collection-commons#359)
- Custom ansible-lint rules for attribute order and FQCN usage (osism/ansible-collection-commons#380)
- Introduction to the docs landing page
- Link to documentation in README (osism/ansible-collection-commons#401)

### Changed
- Support Ansible 2.13 in meta/runtime.yml by extending upper bound to <2.14.0 (osism/ansible-collection-commons#387)
- Use python3 shebang for scan_services plugin (osism/ansible-collection-commons#393)
- Replace custom `scan_services` module with `ansible.builtin.service_facts` in cleanup, motd, and services roles (osism/ansible-collection-commons#396)
- Change default timezone from `Etc/UTC` to `UTC` and ensure tzdata package is installed in timezone role (osism/ansible-collection-commons#395)
- Add "Wait for apt lock" task to timezone role (osism/ansible-collection-commons#397)
- Enable Ubuntu 22.04 in CI test matrix (osism/ansible-collection-commons#389, osism/ansible-collection-commons#395)
- Publish docs to production instead of staging (osism/ansible-collection-commons#398)
- Update documentation for kernel_modules role

### Fixed
- Remove unnecessary `become` from sosreport directory creation tasks (osism/ansible-collection-commons#384)
- Fix documentation build error in network role README (osism/ansible-collection-commons#388)
- Use `generic` group instead of `all` group in sysctl defaults (osism/ansible-collection-commons#391)
- Fix typos and formatting in documentation for configuration, hosts, network, podman, vault_seal, and vault_unseal roles

### Removed
- Remove custom `scan_services` module in favor of `ansible.builtin.service_facts` (osism/ansible-collection-commons#396)

### Dependencies
- ansible 5.9.0 → 6.3.0 (osism/ansible-collection-commons#377, osism/ansible-collection-commons#373, osism/ansible-collection-commons#402)

## [v0.9.0] - 2022-06-30

### Added
- MTU size configuration for dummy network interfaces (osism/ansible-collection-commons#317)
- `NO_PROXY` environment variable to `/etc/environment` in proxy role (osism/ansible-collection-commons#320)
- New sosreport role migrated from playbook (osism/ansible-collection-commons#326)
- Documentation building with zuul-sphinx and tox (osism/ansible-collection-commons#333)
- Documentation for motd, cleanup, certificates, configfs, configuration, docker_compose, facts, hostname, hosts, ipmitool, kernel_modules, known_hosts, kompose, kubectl, lynis, microcode, operator, packages, podman, proxy, repository, resolvconf, services, sosreport, sshconfig, state, sysctl, systohc, and sysdig roles (osism/ansible-collection-commons#344) (osism/ansible-collection-commons#342) (osism/ansible-collection-commons#345) (osism/ansible-collection-commons#346)
- Cloud-init removal in cleanup role, enabled by default via `cleanup_cloudinit` variable (osism/ansible-collection-commons#341)
- Customizable sudo command list for operator role via `operator_sudo_cmd_list` (osism/ansible-collection-commons#324)
- GitHub Action to test the sosreport role (osism/ansible-collection-commons#332)
- Clevis role for network bound disk encryption (osism/ansible-collection-commons#343)
- tox-linters job running yamllint and ansible-lint via Zuul CI (osism/ansible-collection-commons#362)
- Docs staging publishing job in Zuul post pipeline (osism/ansible-collection-commons#374)
- Default branch configuration to Zuul config (osism/ansible-collection-commons#372)
- Empty README.md files to all roles to satisfy ansible-galaxy requirements (osism/ansible-collection-commons#378)

### Changed
- Use `ansible.builtin` FQCN in configuration role (osism/ansible-collection-commons#316)
- Use Docker Compose v2 plugin instead of standalone docker-compose
- Replace deprecated `local_action` with `delegate_to: localhost` in network role (osism/ansible-collection-commons#323)
- Fix YAML truthy value to use `false` instead of `False` in molecule config
- Add `github>osism/renovate-config:python` to Renovate configuration
- Operator role now uses registered result from user creation instead of shell-based home directory lookup (osism/ansible-collection-commons#325)
- Sosreport role updated to use sha256 instead of md5, removed `last` plugin, and improved file permissions handling (osism/ansible-collection-commons#332)
- Podman role now only supports Ubuntu 22.04, removed external repository configuration (osism/ansible-collection-commons#350)
- Configuration role now shows branch name in clone task names (osism/ansible-collection-commons#361)
- Refactored repository role default handling to allow easier overrides (osism/ansible-collection-commons#363)
- Resolvconf role: reordered `when` condition placement (osism/ansible-collection-commons#369)
- Repository role: reordered `become` condition placement (osism/ansible-collection-commons#370)
- Sshconfig role: resolve operator home directory via `getent passwd` instead of hardcoded path (osism/ansible-collection-commons#365)

### Fixed
- Repository role "Check if the keys directory exists" task failing with permission denied by delegating to manager host instead of localhost (osism/ansible-collection-commons#339)

### Removed
- Container and URL install types for docker_compose role
- Debian-specific repository variables that only worked for Ubuntu (osism/ansible-collection-commons#363)
- sphinxcontrib-openapi from doc requirements due to unresolved upstream bug (osism/ansible-collection-commons#376)

### Dependencies
- osism/ansible-lint-action v1.2.0 → v2.0.0 (osism/ansible-collection-commons#315)
- ansible 5.5.0 → 5.9.0 (osism/ansible-collection-commons#319) (osism/ansible-collection-commons#328) (osism/ansible-collection-commons#334) (osism/ansible-collection-commons#348) (osism/ansible-collection-commons#364)
- docker/setup-buildx-action v1 → v2 (osism/ansible-collection-commons#335) (osism/ansible-collection-commons#368)
- actions/setup-python v3 → v4 (osism/ansible-collection-commons#367)
- molecule 3.6.1 → 4.0.0 (osism/ansible-collection-commons#371)

## [v0.8.1] - 2022-04-03

### Added
- Support for proxy configuration in the configuration role via `configuration_git_proxy` (osism/ansible-collection-commons#314)
- SSH keyscan for `ansible_host` in addition to hostname in the known_hosts role (osism/ansible-collection-commons#312)

### Changed
- Configuration role now supports Personal Access Tokens (PAT) as username and suppresses log output to avoid leaking credentials (osism/ansible-collection-commons#313)

## [v0.8.0] - 2022-03-29

### Changed
- Use an empty string by default for `/etc/motd` instead of the STIG warning banner (osism/ansible-collection-commons#310)
- Move docker fact files (`docker_containers`, `docker_images`) to `osism.services.docker`, leaving the facts role with an empty default (osism/ansible-collection-commons#311)

### Fixed
- Fix `hosts_interface` variable evaluation by resolving the interface per host in the template loop instead of from a shared default (osism/ansible-collection-commons#307)

### Dependencies
- ansible 5.4.0 → 5.5.0 (osism/ansible-collection-commons#305)
- osism/ansible-lint-action v1.1.0 → v1.2.0 (osism/ansible-collection-commons#306)

## [v0.7.0] - 2022-03-15

### Added
- AlmaLinux and Rocky Linux repository support in the repository role (osism/ansible-collection-commons#201)
- hosts: add `hosts_enable` parameter to control per-host inclusion (osism/ansible-collection-commons#215)
- hosts: add `hosts_use_dns_as_single_source_of_truth` parameter (osism/ansible-collection-commons#248)
- vault_init role for initializing Vault with kv secrets engine and approle auth (osism/ansible-collection-commons#229)
- vault_seal role for sealing Vault (osism/ansible-collection-commons#227)
- vault_unseal role for unsealing Vault (osism/ansible-collection-commons#226)
- network: support removal of unmanaged netplan configuration files (osism/ansible-collection-commons#230)
- New `known_hosts` role for managing SSH known hosts via ssh-keyscan (osism/ansible-collection-commons#263)
- New `vault_import` role for importing secrets into HashiCorp Vault (osism/ansible-collection-commons#263)
- New `certificates` role for managing CA certificates (osism/ansible-collection-commons#273)
- `sysctl_extra` parameter to allow configuration of additional sysctl parameters per host group (osism/ansible-collection-commons#278)
- Support for dummy netdev interfaces in network role (osism/ansible-collection-commons#292)
- Support for adding repository keys from a directory in repository role (osism/ansible-collection-commons#294)
- Default `nf_conntrack_max` sysctl setting (1048576) for compute nodes (osism/ansible-collection-commons#301)

### Changed
- Updated documentation and homepage URLs from osism.de to osism.tech (osism/ansible-collection-commons#198)
- Repository role now uses `ansible_distribution` instead of `ansible_os_family` for variable inclusion (osism/ansible-collection-commons#201)
- Minimum required Ansible version changed to >=2.11.0,<2.12.0
- Default git branch for configuration role changed from `master` to `main`
- Set `min_ansible_version` to 2.10.0 across all roles
- Relax `requires_ansible` in runtime.yml to allow Ansible 2.10.x and 2.11.x (osism/ansible-collection-commons#213)
- hosts: sort the list of hosts alphabetically (osism/ansible-collection-commons#216)
- Add `changed_when: false` to all "Wait for apt lock" tasks (osism/ansible-collection-commons#217)
- operator: use fully qualified `ansible.posix.authorized_key` module name (osism/ansible-collection-commons#218)
- Use fully qualified collection names (FQCNs) for Ansible tasks across multiple roles (osism/ansible-collection-commons#231, osism/ansible-collection-commons#232, osism/ansible-collection-commons#233, osism/ansible-collection-commons#234, osism/ansible-collection-commons#235, osism/ansible-collection-commons#236, osism/ansible-collection-commons#237, osism/ansible-collection-commons#238, osism/ansible-collection-commons#239, osism/ansible-collection-commons#240, osism/ansible-collection-commons#241, osism/ansible-collection-commons#242, osism/ansible-collection-commons#243, osism/ansible-collection-commons#244, osism/ansible-collection-commons#245, osism/ansible-collection-commons#246, osism/ansible-collection-commons#247, osism/ansible-collection-commons#249, osism/ansible-collection-commons#250, osism/ansible-collection-commons#251, osism/ansible-collection-commons#252, osism/ansible-collection-commons#253, osism/ansible-collection-commons#254, osism/ansible-collection-commons#255, osism/ansible-collection-commons#256, osism/ansible-collection-commons#257, osism/ansible-collection-commons#258, osism/ansible-collection-commons#259, osism/ansible-collection-commons#260, osism/ansible-collection-commons#261)
- Refactor cleanup role to use OS-family-specific service tasks (osism/ansible-collection-commons#264)
- Restrict CI push workflow builds to main branch only (osism/ansible-collection-commons#267)
- Add `osism` galaxy tag to all roles and collection metadata (osism/ansible-collection-commons#269)
- Make sysdig kernel module name configurable via `sysdig_kernel_module_name` variable (osism/ansible-collection-commons#270)
- Switch molecule dependency installation from galaxy to shell command (osism/ansible-collection-commons#266)
- Replaced deprecated `ansible.builtin.include` with `ansible.builtin.include_tasks` across multiple roles (osism/ansible-collection-commons#276, osism/ansible-collection-commons#288)
- Replaced `ignore_errors` with `failed_when: false` in cleanup and services roles (osism/ansible-collection-commons#276)
- Added missing `mode` parameters to file and template tasks in ipmitool, network, and netplan roles (osism/ansible-collection-commons#276)
- Used handler for systemd daemon reload in docker_compose role instead of inline conditional (osism/ansible-collection-commons#276)
- Added ansible-lint CI check using `osism/ansible-lint-action` (osism/ansible-collection-commons#276)
- Upgraded Ansible version to 5.2.0 in CI test workflows (osism/ansible-collection-commons#274)
- Added parameter documentation to hosts role defaults (osism/ansible-collection-commons#280)
- Replaced `ansible.builtin.shell` with `ansible.builtin.command` in cleanup role (osism/ansible-collection-commons#291)
- Bump required Ansible version upper bound to `<2.13.0`
- Delegate repository key directory existence check to localhost (osism/ansible-collection-commons#300)
- Ignore errors about unknown sysctl keys to handle system-specific parameters (osism/ansible-collection-commons#302)
- Improve publish-collection workflow and remove obsolete template/script files (osism/ansible-collection-commons#304)
- Use osism/renovate-config for Renovate configuration

### Fixed
- Re-added Debian.yml vars file for the repository role after it was renamed to Ubuntu.yml
- Configuration role default branch name corrected to `main`
- network: fix `network_dispatcher_scripts` default type from dict to list (osism/ansible-collection-commons#223)
- network: correct indentation in netplan template (osism/ansible-collection-commons#225)
- Fix file permissions in `known_hosts` role to target the known_hosts file instead of the directory, and set mode to 0600
- Fix typo in systohc role (`ansible.buitlin` → `ansible.builtin`) (osism/ansible-collection-commons#265)
- Fixed `sansible.builtin.shell` typo to `ansible.builtin.shell` in cleanup role (osism/ansible-collection-commons#285)
- Fix sysctl task name displaying full dictionary instead of just the key name (osism/ansible-collection-commons#303)

### Removed
- Zabbix roles (`zabbix_cluster`, `zabbix_configuration`, `zabbix_host`)
- Temporarily disable sysdig role tests due to broken role (osism/ansible-collection-commons#270)

### Dependencies
- molecule 3.3.4 → 3.6.1 (osism/ansible-collection-commons#205, osism/ansible-collection-commons#282, osism/ansible-collection-commons#286)
- molecule-docker 0.3.4 → 1.1.0 (osism/ansible-collection-commons#206, osism/ansible-collection-commons#212)
- actions/checkout v2 → v3 (osism/ansible-collection-commons#289)
- actions/setup-python v2 → v3 (osism/ansible-collection-commons#287)
- osism/ansible-lint-action v1.0.0 → v1.1.0 (osism/ansible-collection-commons#295)
- ansible 5.2.0 → 5.4.0 (osism/ansible-collection-commons#299)

## [v0.5.0] - 2021-07-12

### Added
- kubectl role for installing kubectl from Kubernetes apt repository (osism/ansible-collection-commons#145)
- kompose role for installing kompose from URL (osism/ansible-collection-commons#148)
- Netplan support for the network role (osism/ansible-collection-commons#149, osism/ansible-collection-commons#150, osism/ansible-collection-commons#151)
- Container install type for docker-compose role (osism/ansible-collection-commons#158)
- `network_netplan_file` argument for configurable netplan filename (osism/ansible-collection-commons#164)
- CentOS/RedHat support for cleanup, packages, repository, motd, resolvconf, and operator roles (osism/ansible-collection-commons#169, osism/ansible-collection-commons#170, osism/ansible-collection-commons#171, osism/ansible-collection-commons#172, osism/ansible-collection-commons#173, osism/ansible-collection-commons#177)
- hosts: Add `hosts_interface` argument to replace `management_interface` (osism/ansible-collection-commons#168)
- docker_compose: Fail if `ansible_os_family` is not Debian (osism/ansible-collection-commons#174)
- network: Install and enable networkd-dispatcher service (osism/ansible-collection-commons#180, osism/ansible-collection-commons#181)
- Workflow generation script and Jinja2 template for molecule test workflows
- Molecule test workflow for the timezone role
- `workflow_dispatch` trigger to all role test workflows
- CI test workflows for configfs, lynis, sysdig, ipmitool, kernel_modules, and firewall roles using delegated molecule scenario
- Delegated molecule scenario for roles that cannot run inside Docker containers
- `systohc` parameter to allow disabling the systohc role

### Changed
- docker_compose: remove installation from binary and backports repository, default to package install type (osism/ansible-collection-commons#147)
- configuration: use configurable `configuration_git_package_name` variable for git package (osism/ansible-collection-commons#154)
- Remove `become: true` from all "Wait for apt lock" tasks (osism/ansible-collection-commons#156)
- Use quoted `"on"` instead of yamllint disable-line comment in GitHub workflows (osism/ansible-collection-commons#157)
- molecule: use `apt` task instead of `package` in prepare tasks (osism/ansible-collection-commons#160)
- Company name changed from "Betacloud Solutions GmbH" to "OSISM GmbH" in all role metadata (osism/ansible-collection-commons#175)
- hosts: Set default value when `hosts_interface` is not set per host (osism/ansible-collection-commons#176)
- resolvconf: Rename `resolvconf_always_validate_dnssec` to `resolvconf_dnssec` and add `resolvconf_cache_from_localhost` and `resolvconf_read_etc_hosts` options (osism/ansible-collection-commons#178)
- proxy: Use empty dict `{}` as default for `proxy_proxies` (osism/ansible-collection-commons#162)
- Update homepage URL from osism.de to osism.tech (osism/ansible-collection-commons#179)
- Upgraded molecule test workflows to Ansible 4.2.0 and Python 3.8
- Replaced `MOLECULE_ROLE` env variable with `ANSIBLE_ROLE` in all test workflows
- Switched to sed-based `molecule.yml` preparation instead of environment variable interpolation
- Removed deprecated `--use-feature=2020-resolver` pip flag from all test workflows
- Removed QEMU static binaries step from test workflows
- Molecule test workflow template now supports configurable molecule scenario (default vs delegated)
- All existing role test workflows now explicitly specify the molecule scenario name
- Bumped collection version to 0.5.0

### Deprecated
- Zabbix support (zabbix_cluster, zabbix_configuration, zabbix_host) is deprecated

### Fixed
- Fix typo "repositroy" → "repository" in configuration role (osism/ansible-collection-commons#146)
- network: add missing `become: true` directives in handlers and tasks (osism/ansible-collection-commons#152)
- network: allow use of variables as dictionary keys in netplan configuration (osism/ansible-collection-commons#153)
- Fix required Ansible version in meta/runtime.yml to `>=2.10.0,<2.11.0` (osism/ansible-collection-commons#161)
- Fix file extension from `.ym` to `.yml` in kernel_modules role (osism/ansible-collection-commons#182)
- Galaxy metadata authors list exceeding 64 character limit

### Removed
- "PR Labeler" GitHub workflow (osism/ansible-collection-commons#155)

### Dependencies
- molecule 3.3.0 → 3.3.4 (osism/ansible-collection-commons#159, osism/ansible-collection-commons#163, osism/ansible-collection-commons#166, osism/ansible-collection-commons#167)
- molecule-docker 0.2.4 → 0.3.4 (osism/ansible-collection-commons#165)

## [v0.4.0] - 2021-04-09

### Changed
- Do not remove apport and snapd packages by default in cleanup role (osism/ansible-collection-commons#137)
- Use `default.target` instead of `multi-user.target` for docker-compose service (osism/ansible-collection-commons#138)
- Require Ansible >= 3.0.0 and drop Ubuntu 18.04 (Bionic) support (osism/ansible-collection-commons#143)

### Dependencies
- molecule 3.2.2 → 3.3.0 (osism/ansible-collection-commons#139, osism/ansible-collection-commons#140, osism/ansible-collection-commons#141)

## [v0.3.0] - 2021-01-17

### Added
- New `timezone` role for configuring system timezone and hardware clock (osism/ansible-collection-commons#97, osism/ansible-collection-commons#98)
- New `state` role for writing deployment state into custom Ansible facts (osism/ansible-collection-commons#104, osism/ansible-collection-commons#106)
- `docker_images` custom fact for collecting Docker image information (osism/ansible-collection-commons#107)
- Systemd unit file template for docker-compose services (osism/ansible-collection-commons#110, osism/ansible-collection-commons#111)
- Wait for apt lock (`/var/lib/dpkg/lock` and `lock-frontend`) before package operations across all roles (osism/ansible-collection-commons#108, osism/ansible-collection-commons#109)
- Restored `galaxy.yml` for Ansible Galaxy collection metadata (osism/ansible-collection-commons#94)
- `hosts_ignore` parameter to exclude specific hosts from `/etc/hosts` management (osism/ansible-collection-commons#112)
- `ipmitool` role for installing ipmitool and loading IPMI kernel modules (osism/ansible-collection-commons#115)
- `zabbix_configuration` role with host group management and Glance, Horizon, and Keystone templates (osism/ansible-collection-commons#116, osism/ansible-collection-commons#117, osism/ansible-collection-commons#119)
- `zabbix_host` role for creating Zabbix hosts with interfaces, inventory, and automatic template assignment (osism/ansible-collection-commons#120, osism/ansible-collection-commons#121, osism/ansible-collection-commons#122, osism/ansible-collection-commons#123)
- RabbitMQ and MariaDB Zabbix templates and host macros for monitoring (osism/ansible-collection-commons#125)
- Custom RabbitMQ Zabbix template (`OSISM - RabbitMQ`) for zabbix_configuration role (osism/ansible-collection-commons#128)
- Memcached template and connection macro support to zabbix_host role (osism/ansible-collection-commons#130)
- New `zabbix_cluster` role for managing Zabbix cluster hosts (osism/ansible-collection-commons#131)
- `cluster` and `elasticsearch` host groups to zabbix_configuration defaults (osism/ansible-collection-commons#132)
- User and group configuration for docker-compose systemd service (osism/ansible-collection-commons#134)

### Changed
- proxy: Consolidated `proxy_proxies != {}` condition into main task instead of per-distribution tasks (osism/ansible-collection-commons#95)
- network: Changed default for `network_allow_service_restart` to `false` and `network_restart_method` to `nothing` (osism/ansible-collection-commons#102)
- Replaced YAML `yes`/`no` values with `true`/`false` across all roles and moved yamllint config to project root (osism/ansible-collection-commons#100)
- Renamed Zabbix templates for Glance, Horizon, and Keystone to use "OSISM - OpenStack - ..." naming convention (osism/ansible-collection-commons#125)
- Use custom `OSISM - RabbitMQ` template instead of `RabbitMQ node by Zabbix agent` in zabbix_host role (osism/ansible-collection-commons#128)
- Ignore errors when creating Zabbix templates in zabbix_configuration role (osism/ansible-collection-commons#128)
- Use `docker-compose stop` instead of `docker-compose down` when stopping a service (osism/ansible-collection-commons#135)

### Fixed
- facts: Fixed `docker_containers` fact to use Python 3, modern Docker API client, and `print()` function (osism/ansible-collection-commons#103)
- Zabbix monitoring templates now use correct process detection patterns for Kolla-based deployments (osism/ansible-collection-commons#124)
- Wrong MariaDB Zabbix template name (osism/ansible-collection-commons#126)
- Wrong MariaDB macro name `MYSQL_PASSWORD` to `MYSQL_PASS` (osism/ansible-collection-commons#127)
- Hardcoded Zabbix server port macro value in zabbix_host role (osism/ansible-collection-commons#129)

### Removed
- Removed gilt configuration and `.information.yml` (osism/ansible-collection-commons#96)
- resolvconf: Dropped Ubuntu Xenial support and removed `resolvconf_package` variable (osism/ansible-collection-commons#101)
- `ubuntu-server` from default cleanup packages list (osism/ansible-collection-commons#133)

### Dependencies
- molecule 3.2.0 → 3.2.2 (osism/ansible-collection-commons#99, osism/ansible-collection-commons#118)
- actions/setup-python v1 → v2 (osism/ansible-collection-commons#114)
- actions/checkout v1 → v2 (osism/ansible-collection-commons#113)

## [v0.1.0] - 2020-12-16

### Added
- Initial project setup with CI workflows, license, and Ansible Galaxy configuration
- Sysdig role with repository configuration and kernel module management (osism/ansible-collection-commons#1)
- Lynis role with repository configuration and package installation (osism/ansible-collection-commons#3)
- Trivy role for container vulnerability scanning (osism/ansible-collection-commons#5)
- SSH config role for SSH configuration management (osism/ansible-collection-commons#6)
- Import hddtemp, motd, rng, and smartd roles from osism.common (osism/ansible-collection-commons#9)
- Cleanup role with service scanning and apt-daily timer disabling (osism/ansible-collection-commons#10)
- Import roles for hostname, hosts, operator, proxy, repository, and resolvconf (osism/ansible-collection-commons#22)
- Import roles from osism.common: cleanup, configfs, facts, kernel_modules, microcode, packages, services, sysctl, systohc (osism/ansible-collection-commons#25)
- Initial firewall role with ufw support and configuration file template (osism/ansible-collection-commons#27) (osism/ansible-collection-commons#28)
- Docker Compose role with file, package, and URL install types (osism/ansible-collection-commons#31)
- Configuration role with git-based configuration management (osism/ansible-collection-commons#32)
- Install jq as a required package (osism/ansible-collection-commons#41)
- Network role for managing network interfaces, bonding, VLANs, bridges, and LLDP (osism/ansible-collection-commons#52)
- Podman role with repository configuration and package installation (osism/ansible-collection-commons#21)
- gilt.yml configuration file for collection-level generics (osism/ansible-collection-commons#18)
- Docker-based molecule default test scenario (osism/ansible-collection-commons#61)
- Molecule Dockerfile with systemd support for integration testing (osism/ansible-collection-commons#87)
- Configurable `resolvconf_file` variable in resolvconf role (osism/ansible-collection-commons#87)
- Extra/default variable pattern (`_default` and `_extra` lists) for cleanup, kernel_modules, microcode, packages, proxy, resolvconf, and services roles (osism/ansible-collection-commons#92)
- CI test workflows for packages, microcode, facts, trivy, repository, proxy, sysdig, operator, configuration, motd, systohc, podman, docker_compose, sshconfig, hostname, sysctl, hosts, cleanup, resolvconf, and services roles (osism/ansible-collection-commons#61) (osism/ansible-collection-commons#62) (osism/ansible-collection-commons#63) (osism/ansible-collection-commons#64) (osism/ansible-collection-commons#65) (osism/ansible-collection-commons#67) (osism/ansible-collection-commons#68) (osism/ansible-collection-commons#69) (osism/ansible-collection-commons#70) (osism/ansible-collection-commons#77) (osism/ansible-collection-commons#78) (osism/ansible-collection-commons#79) (osism/ansible-collection-commons#80) (osism/ansible-collection-commons#81) (osism/ansible-collection-commons#82) (osism/ansible-collection-commons#83) (osism/ansible-collection-commons#84) (osism/ansible-collection-commons#85) (osism/ansible-collection-commons#87) (osism/ansible-collection-commons#88)

### Changed
- Set apt_repository file mode to 0600 for lynis and sysdig roles (osism/ansible-collection-commons#4)
- motd: overall improvements including dynamic motd disabling, configurable content, and pam configuration for login (osism/ansible-collection-commons#14)
- motd: stop the motd-news service only if it exists (osism/ansible-collection-commons#20)
- cleanup: move scan_services.py module to plugins/modules (osism/ansible-collection-commons#12)
- Move `become` directive to the top of tasks for consistent style across roles (osism/ansible-collection-commons#19)
- Disable test workflows due to timeout issues (osism/ansible-collection-commons#16)
- Remove ansible-lint from molecule requirements as test was moved to GitHub workflows (osism/ansible-collection-commons#23)
- Update README with complete list of included roles (osism/ansible-collection-commons#38)
- Use `true`/`false` instead of `yes`/`no` in proxy, packages, cleanup, configuration, docker_compose, and resolvconf roles (osism/ansible-collection-commons#53) (osism/ansible-collection-commons#54) (osism/ansible-collection-commons#55) (osism/ansible-collection-commons#56) (osism/ansible-collection-commons#57) (osism/ansible-collection-commons#58)
- Clean up GitHub Actions workflows and rename workflow files (osism/ansible-collection-commons#59)
- Migrated molecule test infrastructure from OpenStack to Docker (osism/ansible-collection-commons#61)
- Disabled idempotence and verify steps in molecule test sequence (osism/ansible-collection-commons#66)
- Renamed `MOLECULE_PACKAGE` environment variable to `MOLECULE_ROLE` in all CI workflows (osism/ansible-collection-commons#71)
- Enabled repository configuration by default in trivy role (osism/ansible-collection-commons#63)
- Changed `sysdig_configure_repository` default to `true` (osism/ansible-collection-commons#68)
- Changed default git repository in configuration role to `osism/ansible-collection-commons.git` (osism/ansible-collection-commons#70)
- Added `/etc/modules-load.d` directory creation to sysdig molecule prepare step (osism/ansible-collection-commons#72)
- Default `podman_configure_repository` to `true` (osism/ansible-collection-commons#79)
- Set `ANSIBLE_LIBRARY` path in molecule configuration (osism/ansible-collection-commons#77)
- CI test workflows now also trigger on molecule default configuration changes (osism/ansible-collection-commons#86)
- Cleanup role moves service facts collection to main tasks and fixes apt-daily timer disabling with service existence check (osism/ansible-collection-commons#85)
- Repository role removes default third-party repositories (Docker, Netdata, osquery) from defaults (osism/ansible-collection-commons#91)
- Enabled "Publish collection" GitHub Actions workflow with tag-based triggering and Ansible playbook for building/publishing to Galaxy (osism/ansible-collection-commons#89)
- Extract version from git tag reference in publish collection workflow (osism/ansible-collection-commons#93)

### Fixed
- Fixed sysdig test badge URL in README to point to correct repository (osism/ansible-collection-commons#2)
- Fix ansible-lint E208 by adding missing file mode to copy and replace tasks (osism/ansible-collection-commons#17)
- Fix handler name in firewall role (osism/ansible-collection-commons#29)
- Fix path to fact files in facts role (osism/ansible-collection-commons#30)
- Removed redundant `update_cache` parameter from repository role's package cache task (osism/ansible-collection-commons#64)
- Removed incorrect `changed_when: false` from sysdig apt-transport-https install task (osism/ansible-collection-commons#73)
- Add conditional check for `motd-news.timer` service existence before stopping it (osism/ansible-collection-commons#77)
- Skip ansible-lint for cleanup services.yml file (osism/ansible-collection-commons#15)

### Removed
- Move hddtemp, rng, and smartd service roles to osism.services collection (osism/ansible-collection-commons#24)
- Old OpenStack-based molecule configurations for lynis, sshconfig, sysdig, and trivy roles (osism/ansible-collection-commons#60)
- Remove ansible-lint GitHub Actions workflow (osism/ansible-collection-commons#59)
- Removed `clouds.yml.gpg` file (osism/ansible-collection-commons#74)
- Legacy `.information.yml`, `README.md`, and `gilt.yml` files from all roles (osism/ansible-collection-commons#75)
- Sysdig molecule test workflow due to Docker kernel module limitations (osism/ansible-collection-commons#76)
- Old disabled CI workflows for lynis, sshconfig, sysdig, and trivy (osism/ansible-collection-commons#90)

### Dependencies
- molecule 3.0.6 → 3.2.0 (osism/ansible-collection-commons#11) (osism/ansible-collection-commons#26) (osism/ansible-collection-commons#42) (osism/ansible-collection-commons#43) (osism/ansible-collection-commons#44) (osism/ansible-collection-commons#45) (osism/ansible-collection-commons#46) (osism/ansible-collection-commons#51)
- molecule-openstack 0.1 → 0.2 (osism/ansible-collection-commons#47)
- testinfra 5.2.2 → 6.0.0 (osism/ansible-collection-commons#34) (osism/ansible-collection-commons#35) (osism/ansible-collection-commons#49)
- paramiko 2.7.1 → 2.7.2 (osism/ansible-collection-commons#33)
- openstacksdk 0.48.0 → 0.52.0 (osism/ansible-collection-commons#36) (osism/ansible-collection-commons#37) (osism/ansible-collection-commons#48) (osism/ansible-collection-commons#50)

