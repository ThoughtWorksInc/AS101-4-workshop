# Getting Started

## Forking the repository

Firstly, make a git fork of this repository through the Github user interface. This will allow you to make commits and push changes to your own copy of the source code.

Then, make a clone of your fork of this repository to your local computer.

## Starting the Application

To see the sample app running, make sure you have docker-compose installed, then run the following command:

`docker-compose up --build`

Then in your browser go to `localhost:8000`

### Stopping the Application

To stop the application, from the command line enter `Control-C`.

**Note:**

If starting the application, you should stop the application before proceeding with the [sample-deploy-pipeline](https://github.com/wilvk/sample-deploy-pipeline) instructions as we will spin up this application in a Jenkins deployment pipeline.

Attempting to have two copies of the `sample-flask-app` container running at the same time on your computer is not possible as we are using [Docker-in-Docker](https://www.docker.com/blog/docker-can-now-run-within-docker/) (dind) to spin up the container from a Jenkins container and the exposed ports will conflict between the two containers.
