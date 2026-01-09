.. _docker:

=================================================
Docker installation over CLI - No Docker Desktop
=================================================

Docker over WSL
===============

The following steps are used to install *Ubuntu 24.04.3 LTS* distribution in the WSL environment.

The steps were taken from the `Docker documentation  <https://docs.docker.com/engine/install/ubuntu/>`__ and require admin rights::

    sudo apt update
    sudo apt install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
    Types: deb
    URIs: https://download.docker.com/linux/ubuntu
    Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
    Components: stable
    Signed-By: /etc/apt/keyrings/docker.asc
    EOF
    sudo apt update

Install Docker packages::

    sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Check docker installation::

    docker run hello-world

.. hint::

    In case `docker run` fails because of user rights, you can add your linux user to the dockier group::
    
        sudo groupadd docker
        sudo usermod -aG docker $USER

    Restart your WSL for the changes to take effect. For more information, see `Docker post-installation steps  <https://docs.docker.com/engine/install/linux-postinstall/>`__.