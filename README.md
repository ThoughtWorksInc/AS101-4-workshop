# sample-flask-application

This application is intended for use with the `sample-deploy-pipeline` Jenkins application located here: https://github.com/wilvk/sample-deploy-pipeline

## Overview

This application consists of two containers:

- A frontend website written in Python Flask
- A backend database using PostreSQL

It is a simple message posting application where messages entered by the user in the web interface are written to the PostgreSQL database. The web front-end shows all messages entered by users.

## Forking the repository

Firstly, make a git fork of this repository through the Github user interface. This will allow you to make commits and push changes to your own copy of the source code.

Then make a clone of your fork of this repository to your local computer.

## Talisman

[Talisman](https://github.com/thoughtworks/talisman) is a Secrets Scanning application for git to prevent committing and pushing of secrets to your git source control server.

It works by using git hooks into the local copy of the source code you are working on.

We want to run Talisman on this repository to scan it for secrets.

### Installing Talisman

We want to follow the instructions on the [Talisman README.md](https://github.com/thoughtworks/talisman#installation-as-a-global-hook-template
) for installing Talisman as a global hook template.


Before we install Talisman, make a note of the path of your forked, cloned repository. e.g. 

```
$ pwd
/Users/willvk/source/sample-flask-application
```

We can then download and run an install script to load the Talisman binaries for our specific Operating System. At the prompt for what local repositories to add the hook to, enter the path `/tmp`. This will prevent it installing Talisman for all the repositories under your home path.

```
curl --silent  https://raw.githubusercontent.com/thoughtworks/talisman/master/global_install_scripts/install.bash > /tmp/install_talisman.bash && /bin/bash /tmp/install_talisman.bash
```

For example:

![](./images/1.png)

Talisman also sets an environment variable called `$TALISMAN_HOME` in your bash profile that points to the home path of Talisman on your system. This needs to be present in your resource file (`.bashrc`, `.bash_profile`, `.zshrc`, etc) for Talisman to run. You may need to either source your bash profile or restart the terminal to make sure it is there. You can check it is present by running:

```bash
$ env | grep TALISMAN_HOME
TALISMAN_HOME=/Users/willvk/.talisman/bin
```


