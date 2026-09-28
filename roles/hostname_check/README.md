# hostname_check

Refuses a host whose kernel name disagrees with the name other components will
derive for it.

## Why

`gethostname()` and `getaddrinfo(..., AI_CANONNAME)` can return different
strings: a short kernel name that resolves to an FQDN. Components differ in
which one they use, and none of them is wrong on its own:

| component | derives the name via | gets |
|---|---|---|
| kolla `compute_id` lookup | `ansible_facts.nodename` (`uname -n`) | short |
| nova `CONF.host` | `socket.gethostname()` | short |
| libvirt `hypervisor_hostname` | `virGetHostname()` | FQDN |
| libvirt SASL server realm | Cyrus `get_fqhostname()` | FQDN, lowercased |
| OVN `Chassis.hostname` | ovn-controller's own lookup | FQDN |

Breakage happens where one component's name is used as a lookup key against a
name another component stored. Three such lookups are known, each fatal: the
`compute_id` delivery overwrites a registered compute's identity, nova-compute
cannot authenticate to libvirtd, and OVN refuses to bind any port. Nothing
establishes that three is the whole list, which is why this role refuses the
*condition* rather than guarding each lookup.

## What it checks

Two conditions, both required:

1. `gethostname()` equals its `getaddrinfo(AI_CANONNAME)` form.
2. `gethostname()` is lowercase — Cyrus folds case and libvirt does not, so a
   mixed-case name breaks the SASL lookup even when (1) holds.

## Where it runs

After `osism.commons.hostname`, `osism.commons.hosts` **and**
`osism.commons.resolvconf`, since all three can change the answer. Running it
earlier measures a state that is about to change.

## Variables

| variable | default | meaning |
|---|---|---|
| `hostname_check_enabled` | `true` | run the check at all |
| `hostname_split_accepted` | `false` | downgrade the refusal to a warning |

`hostname_split_accepted` exists for a cluster already in this state that cannot
be renamed yet: the refusal is how such an operator finds out, and the variable
is how they proceed. It records the decision; it does not make the state safe.
