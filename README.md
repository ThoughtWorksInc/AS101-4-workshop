# sample-flask-application

## Requirements

* Docker
* Docker-compose
* Forking the repository

Make a git fork of this repository through the Github user interface. This will allow you to make commits and push changes to your own copy of the source code.

Then, make a clone of your fork of this repository to your local computer:

```bash
git clone https://github.com/[REPLACE-WITH-YOUR-FORK]/sample-flask-app.git
```

## Exercise 1 - secret detection in code

For this exercise, running the application is not necessary.

### 01-01 - Hawkeye

We will use [Hawkeye](https://github.com/hawkeyesec/scanner-cli) to scan secrets in the code base.

Run Hawkeye in Docker with:

```console
docker run --rm -v $PWD:/target hawkeyesec/scanner-cli:latest
```

Did you find anything interesting?

## Exercise 2 - secret detection with Git hooks

For this exercise, running the application is not necessary.

### 02-01 Talisman

1. Follow the Talisman installation instructions in [Talisman.md](talisman.md)

2. In our sample application, open the file `web/config.py` in a text editor of your choice. 

Add a benign change to the file by adding an exra line to the end of the file, or a space somewhere. It can be anything as long as it doesn't affect the code.

Save the file.

3. Do a git add of the file. e.g. `git add web/config.py`.

Then do a git commit. e.g. `git commit -m "testing talisman"`

If all is working, you should be prompted by talisman about a potential secret being checked-in.

You can then unstage your changes and checkout all files to revert your local repository to it's previous state.

For example:

```sh
git reset
git checkout .
```

## Exercise 3 - CI/CD

### 03-01 Install the build server

Run the build server by following the instructions in the `sample-deploy-pipeline` Jenkins repository located [here](https://github.com/wilvk/sample-deploy-pipeline/blob/master/getting-started.md).

### 03-02 Run the Flask application via the build server

The Flask application consists of two docker containers:

* A frontend website written in Python Flask
* A backend database using PostgreSQL

It is a simple message-posting application where messages entered by the user in the web interface are written to the PostgreSQL database. The web front-end shows all messages entered by users.

Configure the CI/CD pipeline by following instructions available in [building-the-pipeline.md](https://github.com/wilvk/sample-deploy-pipeline/blob/master/building-the-pipeline.md)

### 03-03 Install and run Hawkeye

Follow the instructions available in [adding-hawkeye.md](https://github.com/wilvk/sample-deploy-pipeline/blob/master/adding-hawkeye.md)

## Exercise 4 - Handling secrets

### 04-01 - Remove secrets in code

We will update our code to remove secrets in code and instead, use Ansible Vault to source them.

Follow the instructions in [handling-secrets.md](https://github.com/wilvk/sample-deploy-pipeline/blob/master/handling-secrets.md).