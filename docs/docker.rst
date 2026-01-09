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

    In case `docker run` fails because of user rights, you can add your linux user to the docker group::
    
        sudo groupadd docker
        sudo usermod -aG docker $USER

    Restart your WSL for the changes to take effect. For more information, see `Docker post-installation steps  <https://docs.docker.com/engine/install/linux-postinstall/>`__.

Usefull commands
================

Docker run: 
docker run -> docker create + docker start

docker start -a <container_id>

To list all docker process:
``docker ps -a``

Execute an additional command in a container: ``docker exec -it <container_id> <command>``

.. hint::
    The ``it`` flag stands for ``-i`` and ``-t`` and both make sure that first, we are giving input arguments to the container we just started and second, that it's output is text-formated.

    Keep in mind how Linux processes are structed: We usually have a STDIN, STDOUT and STDERR for each process that it's running and those communicate with us thought the terminal. 

.. mermaid::
    
    block
    columns 2
    PA["Process A \n ping google.com"] 
    PB["Process B \n redis-cli"]
    block:group1
        PA_IN["STDIN"]
        PA_OUT["STDOUT"]
        PA_ERR["STDERR"]
    end
    block:group2
        PB_IN["STDIN"]
        PB_OUT["STDOUT"]
        PB_ERR["STDERR"]
    end
    space:3
    Terminal
    PB_IN --> Terminal
    Terminal --> PB_OUT
    Terminal --> PB_ERR
