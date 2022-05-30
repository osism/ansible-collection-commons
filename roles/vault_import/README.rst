Ansible role for importing secrets to hashicorp vault.

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

.. zuul:rolevar:: vault_secrets_path
   :default: /opt/configuration/environments/secrets.yml

This path contains the file with the secrets which should imported to vault.
