# Schoolbox API

The schoolbox-api is a simple API that has been developed in order to list, create, update and remove students from a DB (complete CRUD).

[Back-end]

Language: Python

Frameworks: Flask

DB: MySQL

[Front-end]

Just a simple HTML5

Enjoy it!


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

In order to run this app, you need just install Docker CE and Docker Compose.

For more information, see https://docs.docker.com/install/ and https://docs.docker.com/compose/install/.

Clone this repository:

```
git clone https://github.com/ebarros29/schoolbox-api

cd schoolbox-api
```

### Installing

A step by step series of examples that tell you how to get a development env running

Installing Docker CE and start Docker daemon

```
https://docs.docker.com/install/
```

Installing Docker Compose

```
https://docs.docker.com/compose/install/
```

## Running the environment

```
docker-compose up -d
```

## Running the tests

Simple tests to make sure that is everthing fine.

### Break down into end to end tests

Checking if all containers are running. You should see 2 containers up, the first one refers to web-api, the second one to mysql. 

Use the below command in order to check containers status:

```
docker ps -a
```

You can check the logs of each container using the below command:

```
docker logs <container id>
```

## Authors

* **Emerson Barros** - *Initial work* - [ebarros29](https://github.com/ebarros29)

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.-->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
