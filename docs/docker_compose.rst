.. _docker_compose:

==============
Docker Compose
==============

Docker compose is used to start multiple Docker containers at the same time, conect them together and automate the process of executing ``docker run``.

For this, it uses a file called ``docker-compose.yml``.

In this example, we want to start two different containers at the same time:

- "**redis-server**", that use redis image as base image
- "**node-app**", that uses a Dockerfile in the source directory

1. Start yor WSL environment, create project's directory, enter it and start SVCode.
2. Create the file ``docker-compose.yml`` with the following content::

    services: 
    redis-server:
        image: 'redis'
    node-app:
        build: . 
        ports:
        - "4001:8081"

3. Create a ``package.json`` file to specify the dependencies::

    {
        "dependencies": {
            "express": "*",
            "redis": "2.8.0"
        },
        "scripts": {
            "start": "node index.js"
        }
    }

4. Create a ``index.js`` file::

    const express = require('express');
    const redis = require('redis');

    const app = express();
    const client = redis.createClient({
        host: 'redis-server',
        port: 6379
    });
    client.set('visits', 0);

    app.get('/', (req, res) => {
        client.get('visits', (err, visits) => {
            res.send('Number of visits is ' + visits);
            client.set('visits', parseInt(visits) + 1);
        });
    });

    app.listen(8081, () => {
        console.log('Listening on port 8081');
    });

5. Finally, create a ``Dockerfile``::

    FROM node:alpine

    WORKDIR '/app'

    COPY package.json .
    RUN npm install
    COPY . .

    CMD ["npm", "start"]

6. In your terminal, start both services:
   
   - To start multiple docker containers: ``docker compose up``
   - To lauch multiple containers in the background: ``docker compose up -d``
   - To stop multiple docker containers: ``docker compose down``