.. _docker:

See next:

.. toctree::
    
    docker_compose


======
Docker
======

Docker installation over CLI - No Docker Desktop
=================================================

Docker over WSL
---------------

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

Docker Basics
=============

- **Run** a docker container (create + start): ``docker run [OPTIONS] <image> <comand>``
- **Start** a docker container: ``docker start -a <container_id>``
- **List** all docker process: ``docker ps -a``

.. hint::
    The ``-a`` flag attaches the output to STDIN, STDOUT or STDERR

- Execute an **additional** command in a container: ``docker exec -it <container_id> <command>``

.. hint::
    The ``it`` flag stands for ``-i`` and ``-t`` and both make sure that first, we are giving input arguments to the container we just started and second, that it's output is text-formated.

    - Keep in mind how Linux processes are structed: We usually have a STDIN, STDOUT and STDERR for each process that it's running and those communicate with us thought the terminal. 

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

    - You can pass ``sh`` as command option, which allows starting a shell within the container. You can also used for ``docker run [OPTIONS] <container> sh``, but this would restrict you to only have a single process running in your container.
    - Usually, you would start a conatiner with a specific process (e.g WebServer) and on a separate tab, append an addicional process using ``docker exec -it <container_id> sh``.


How to build our own image
--------------------------

For this we need a ``Dockerfile``. This file contains:

- A Base Image
- Commands to install additional programs/dependencies
- Command to run during the container startup

.. hint::

    In this example, we want to install and run Redis, which is a in-memory database 
    For this, we use Alpine as a base image. 
    Alpine is a light Linux distribution and contains the necessary pre-installed programs we need.

1. Open WSL, create a new directory (``mkdir <DIR_NAME>``) and enter the folder (``cd <DIR_NAME>``)
2. Start VSCode (``code .``)
3. Create a new ``Dockerfile`` and use the following code::

    # Specify the docker image we want to use as a base
    FROM alpine

    # Download and install a dependencies
    RUN apk add --update redis

    # Tell the image what to do when starting the container
    CMD ["redis-server"]

4. In your terminal, run ``docker build .``

   - Or, to follow the convention, tag a name to your image::
 
        docker build -o plain -t <your docker ID>/<project name>:<version> .

When executiong the build, the docker server will first look into our local build cache and check if alpine image has already been download before. 
If not, it will automatically download it. Under the hood, the following happens (Docker > v18.x):

1. Docker parses the Dockerfile and builds a dependency graph. In other words, docker checks the product of each instruction and what each instruction depends on.
2. Docker resolves the base image (e.g. ``alpine``) and pulls missing layers if necessary.
3. For each instruction that modifies the filesystem (e.g ``RUN`` or ``COPY``), BuildKit executes the instruction in an isolated build environment and records only the FS changes as a new **image layer**.
4. Instructions that only affect image configuration (e.g ``CMD``, ``ENTRYPOINT``, ``ENV``, or ``WORKDIR``) are stored as **image metadata** and do not generate FS layers.
5. After all layers and metadata are assembled, BuildKit exports the final image.
   - If a tag is provided, the image is saved under that name.
   - If no tag is provided, the image is stored as a dangling image identified by its **digest**.

    .. note::

        A image digest is not the same as image ID. It is a cryptographic hash containing the image metadata, the list of layer digests and the order of those layers.

        If two images have the same digest, they are identical. The image ID is derived from the digest and is a local identifier.

        *By changing the order of RUN instructions in the docker file, it may also affect the time needed to build the image, because the layer digest will be different than the one in the local cache*

.. caution::

    **Before BuildKit (before Docker v18.09)**

    1. Docker checks if the base alpine image exists locally and pulls it if necessary.
    2. For each RUN instruction, it creates a temporary container and executes the command inside of it (e.g ``apk add --update redis``).

       - ``apk`` is a package mananger for alpine distribution. It will start a sub-process of downloading and installing Redis.
  
    3. After finishing the previous step, the temporary container will be stopped and the filesystem changes will be committed into a new image layer. The temporary container is then removed. 
    4. The ``CMD`` instruction is stored as metadata in the image and it will be default command executed when the container is started.
    5. This image is saved and it's id is returned as output.

6. Run the docker image: ``docker run <image name/image id>``

