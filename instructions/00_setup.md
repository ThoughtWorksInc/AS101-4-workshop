# Getting Started

## Requirements

- Docker
- Docker-compose

## Forking the repository

Make a git fork of this repository through the Github user interface. This will allow you to make commits and push changes to your own copy of the source code.

Then, make a clone of your fork of this repository to your local computer:

```bash
git clone https://github.com/[REPLACE-WITH-YOUR-FORK]/sample-flask-app.git
```

change directory into your forked, cloned repository and make a note of the path.

```bash
cd sample-flask-app
pwd
```

```txt
/path/to/your/sample-flask-app
```

## Pulling docker images

This is the slowest step of the exercise, so it's best to start it first, so that it can run in the background.

```bash
docker pull postgres:12.2  # from docker-compose.yml
docker pull python:3.7  # from web/Dockerfile
docker pull derwentx/scanner-cli:latest  # for exercise 1
docker pull hawkeyesec/scanner-cli:latest  # for exercise 1
```

## Starting the Application

To see the sample app running, make sure you have docker-compose installed, then run the following command:

`docker-compose up --build`

Then in your browser go to `localhost:8000`

## Stopping the Application

To stop the application, from the command line enter `Control-C`.

**Note:**

If starting the application, you should stop the application before proceeding with the [sample-deploy-pipeline](https://github.com/wilvk/sample-deploy-pipeline) instructions as we will spin up this application in a GitHub Actions pipeline.

## Installing Talisman

[Talisman](https://github.com/thoughtworks/talisman) is a Secrets Scanning application for git to prevent committing and pushing of secrets to your git source control server.

It works by using git hooks into the local copy of the source code you are working on.

We want to run Talisman on this repository to scan it for secrets.

### Downloading Talisman

Run the following command:

```bash
curl --silent \
https://raw.githubusercontent.com/thoughtworks/talisman/master/global_install_scripts/install.bash \
  -o /tmp/install_talisman.bash && /bin/bash /tmp/install_talisman.bash
```

This command comes from the official [Talisman instructions](https://github.com/thoughtworks/talisman#installation-as-a-global-hook-template
)

It will download and run an install script to load the Talisman binaries for our specific Operating System.

### Configuring Talisman as a global hook template

At the prompt for what local repositories to add the hook to, enter the path listed by `pwd` above for your repository.

This will prevent it installing Talisman for all the repositories under your home path.

For example:

![talisman_install](../images/1.png)

### Testing Talisman installed correctly

From the command prompt, enter `talisman`. It should return a list of command options.

If this step fails, verify that Talisman has set an environment variable called `$TALISMAN_HOME` in your bash profile that points to the home path of Talisman on your system.

This needs to be present in your resource file (`.bashrc`, `.bash_profile`, `.zshrc`, etc) for Talisman to run. You may need to either source your bash profile or restart the terminal to make sure it is there.

You can check it is present by running:

```bash
$ env | grep TALISMAN_HOME
TALISMAN_HOME=/Users/willvk/.talisman/bin
```

If it's not present add it with:

```bash
echo "TALISMAN_HOME=$HOME/.talisman/bin" >> ~/.bashrc
source  ~/.bashrc
```
