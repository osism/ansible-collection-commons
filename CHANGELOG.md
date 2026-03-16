# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- user: add comprehensive parameter documentation to defaults/main.yml
- chore(deps): update dependency molecule to v25.5.0 (#783)
- chore(deps): update dependency ansible to v11.6.0 (#780)

### Fixed
- molecule: enhance motd tests (#782)

### CI
- zuul: refresh secrets (#781)
- zuul: rebuild osism-kubernetes (#779)

## [v0.20250407.0] - 2025-04-07

### Added
- hostname: allow to overwrite the hostname with hostname_name (#777)
- network: add MACAddress to vxlan netdev (#761)

### Changed
- configuration: make no_log configurable (#776)
- chore(deps): update dependency molecule to v25.4.0 (#778)
- chore(deps): update dependency pytest-testinfra to v10.2.2 (#775)
- chore(deps): update dependency ansible to v11.4.0 (#770)
- chore(deps): update dependency derailed/k9s to v0.40.10 (#769)
- chore(deps): update dependency derailed/k9s to v0.40.9 (#768)
- chore(deps): update dependency derailed/k9s to v0.40.8 (#767)
- chore(deps): update dependency derailed/k9s to v0.40.7 (#766)

### Removed
- Remove k9s role (#773)
- Remove kubectl role (#772)

### Fixed
- Cleanup ansible-lint configuration (#771)