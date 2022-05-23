This ansible role checks if kompose is already installed, if not triggers an install and checks the checksum.

**Role Variables**

.. zuul:rolevar:: kompose_install_type
   :default: url

From which source the download should done.

.. zuul:rolevar:: kompose_version
   :default: 1.22.0

Which version of kompose should be installed.

.. zuul:rolevar:: kompose_checksum
   :default: 6203d67263886bbd455168f59309496d486fc3a6df330b7ba37823b283bd9ea5

The checksum of the downloaded file.

.. zuul:rolevar:: kompose_url
   :default: "https://github.com/kubernetes/kompose/releases/download/v{{ kompose_version }}/kompose-linux-amd64"

Url for the download.
