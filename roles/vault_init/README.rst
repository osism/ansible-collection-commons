This ansible role will configure policies inside the vault-server for the
key-value-store (kv).

**Role Variables**

.. zuul:rolevar:: vault_token
   :default: ""

Token to login to vault.

.. zuul:rolevar:: vault_protocol
   :default: http

The protocol which will be used to connect to vault.

.. zuul:rolevar:: vault_host
   :default: vault

Hostname of the vault-server.

.. zuul:rolevar:: vault_port
   :default: 8200

The Port which vault will use for connections.

.. zuul:rolevar:: vault_url
   :default: {{ vault_protocol }}://{{ vault_host }}:{{  vault_port }}

Address from the vault server for connections to the server.

.. zuul:rolevar:: vault_rules_read
   :default: path "kv/*" {capabilities = ["read"]}

Vault-read-policy.
Configures a policy to allow reads from the key-value-store.

.. zuul:rolevar:: vault_rules_write
   :default: |
             path "kv/*" {
             capabilities = ["create", "read", "update", "delete", "list"]}

Vault-write-policy.
Configures a policy to allow every action to the key-value-store.
