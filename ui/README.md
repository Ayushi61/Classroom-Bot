# ClassBot Admin UI documentation

## High Level Diagram
![fin](https://user-images.githubusercontent.com/59896588/93835394-126c7300-fc4d-11ea-9294-35b513ad408c.jpg)


## Setup and Installations
This section gives a detailed description of the steps required to setup a development environment for the admin UI of the project.
The UI was built using react by leveraging standard react libraries. 

### Prerequisites
* [Node.js](https://nodejs.org/en/download/)
* [Docker](https://docs.docker.com/get-docker/)
* [Docker-Compose](https://docs.docker.com/compose/)
* [make](https://www.gnu.org/software/make/)  
    Make should be pre-installed in linux and mac os. For windows please consider setting up a virtual machine. However, this is not a hard requirement. All commands can be run locally from the Makefile in the project

### Steps to Install
Follow the below steps and commands to setup and run the admin ui locally

#### Local Installation
1. Clone the git repository and from the root folder run the below command to install all the dependencies for the Admin UI  
`make ui.install`

2. Finally navigate back to the root directory of the project and run the below command to start the development server  
    `make ui.local.start`

4. The admin ui will run in the url http://localhot:3000

#### Docker Installation
1. Clone the git repository and ensure the docker daemon on your machine is started

2. From the root directory run the below commands  
    `make ui.build`  This command will create the build of the Admin UI application in the ui/classroom-bot-ui/build path

3. Finally build the docker image and run the container using the following commands  
    `make ui.docker.build`  
    `make ui.docker.run`  

4. Similar to above the app will run in the url http://localhot:3000.

* Please ensure that the Database and the Django apis are running before you start the Admin UI

### Other relevant commands

#### Running Test Cases
In order to run the tests use the command `make ui.local.test`

#### Running Linters
In order to run linters use the command `make ui.docker.lint`. The linter will spin up a docker container and will run eslint within the container.

