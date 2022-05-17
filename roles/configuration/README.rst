This ansible role configures the system with all required parameters that are needed
for cloning the ansible-collection-commons repository.

**Role Variables**

Generic Variables:

   .. zuul:rolevar:: operator_user
   :default: dragon
   
   The default user.

   .. zuul:rolevar:: operator_group
   :default: "{{ operator_user }}"

   The default group.

   .. zuul:rolevar:: configuration_type
   :default: git

   That is the configuration source for the OSISM ansible collections.

Directories:

   .. zuul:rolevar:: configuration_directory
   :default: /opt/configuration
   
   The directory where the cofiguration will be stored in.

Parameters for configuration type "git":

   .. zuul:rolevar:: configuration_git_package_name
   :default: git

   # Fix me

   .. zuul:rolevar:: configuration_git_proxy
   :default: ""

   If you have to use a proxy to be able to reach your git use this variable.

   .. zuul:rolevar:: configuration_git_public_key
   :default: ""

   The public key from the keypair which you use to connect to git.

   .. zuul:rolevar:: configuration_git_private_key
   :default: ""

   The private key from the keypair which you use to connect to git.

   .. zuul:rolevar:: configuration_git_private_key_file
   :default: ~/.ssh/id_rsa.configuration

   The path where your keypair is stored.

   .. zuul:rolevar:: configuration_git_version
   :default: main

   The branch version which should be used.

   .. zuul:rolevar:: configuration_git_host
   :default: github.com
   
   The host from where you get the repositories.

   .. zuul:rolevar:: configuration_git_port
   :default: 22

   The Port that is used for downloading the repoository.

   .. zuul:rolevar:: configuration_git_repository
   :default: osism/ansible-collection-commons.git

   The name of the repository which is needed.

   .. zuul:rolevar:: configuration_git_protocol
   :default: ssh

   Which protocol will be used for the downloads.

   .. zuul:rolevar:: configuration_git_username
   :default: git

   This is an Personal Access Token and it is GitHub specific. 
   If you use GitHub you will need to use this.

   .. zuul:rolevar:: configuration_git_repository_url

   This is a variable which is composed of:
   "{{ configuration_git_protocol }}://{{ configuration_git_username }}@{{ configuration_git_host }}:{{ configuration_git_port }}/{{ configuration_git_repository }}"

   Short example: https://github.com/osism/ansible-collection-commons

