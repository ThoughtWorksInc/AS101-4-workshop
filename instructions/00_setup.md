# Getting Started

## Requirements

This workshop requires the following tools to be installed on your machine:

- Docker
- Docker-compose

Check if you already have these tools installed:
```bash
docker version
docker-compose version
```
If they are, you can skip to [Pulling Docker images](#pulling-docker-images).

Otherwise, the easiest way to install them on MacOS is to install [colima](https://github.com/abiosoft/colima#installation) `docker` and `docker-compose` via the
[Homebrew package manager](https://docs.brew.sh/Installation).

```bash
brew install colima
brew install docker
brew install docker-compose
```

And start colima

```bash
colima start
```

## Pulling Docker images

This is the slowest step of the exercise, so it's best to start it first so that it can run in the
background, and you can proceed to the next step while the images are downloading.

```bash
docker pull postgres:12.2  # from docker-compose.yml
docker pull python:3.7  # from web/Dockerfile
docker pull hawkeyesec/scanner-cli:latest  # for exercise 1
```

## Forking the repository

Make a git fork of this repository through the Github user interface. This will allow you to make
commits and push changes to your own copy of the source code.

Then, make a clone of your fork of this repository to your local computer. In your fork, click the
`⤓ Code` and copy either the `SSH` or `HTTPS` command into your terminal.

```bash
git clone https://github.com/[YOUR-GITHUB-USERNAME]/as101-4-workshop.git
```

Change directory into your forked, cloned repository and make a note of the path.

```bash
cd as101-4-workshop
pwd
```

The `pwd` command will output your current directory.

```txt
/path/to/your/as101-4-workshop
```

## Git Authentication

There are several ways you can clone this repository. The default is https (remote url looks like `https://github.com/ThoughtWorksInc/AS101-4-workshop.git`) but you can also use ssh (remote looks like `git@github.com:ThoughtWorksInc/AS101-4-workshop.git`). You can check which one you are using with `git remote -v`.

If you are using an SSH origin and have multiple git accounts, you may want to review [these instructions](https://sites.google.com/thoughtworks.com/infosec-hub/awareness-deprecated/git-account-segregation) on git account segregation.

If you are using an HTTPS origin, ensure you have an access token which has the following scopes:

- repo
- workflows

## Using the Echo app

### Starting the Application

To see the sample app running, run the following terminal command: `docker-compose up --build`.

Then in your browser go to `localhost:8000`.

If everything is working, you should be able to submit basic messages to the site, and they will
show up in the messages feed.

### Stopping the Application

To stop the application, go back to the terminal from which you started the application, and type
`Control-C`.

## Talisman

[Talisman](https://github.com/thoughtworks/talisman) is a Secrets Scanning application for git to
prevent committing and pushing of secrets to your repository.

It works by using git hooks in the local copy of the source code you are working on. Installing
Talisman on your local copy of a repository won't affect other users of the same repository, however
if you have other git hooks installed, there are extra steps required for them to all play nicely.

If you don't know whether you already have Talisman installed, you can check using [these instructions](#testing-talisman-installed-correctly).

If you're not sure about Talisman, you can install it
[on each repository individually](#installation-to-a-single-project). There are also instructions to
[install it globally](#installation-as-a-global-hook-template).

You will need to use one of these sets of instructions to install talisman into the `as101-4-workshop`
repo so that we can scan it for secrets in the exercises.

### Installation to a single project

Talisman provides
[instructions](https://github.com/thoughtworks/talisman#installation-to-a-single-project) for
installing to a single repository:

```bash
# Download the talisman installer script
curl https://raw.githubusercontent.com/thoughtworks/talisman/master/install.sh > ~/install-talisman.sh
chmod +x ~/install-talisman.sh
```

```bash
# Install to a single project as a pre-commit hook
cd as101-4-workshop # if you're not already in this directory
~/install-talisman.sh pre-commit
```

### Installation as a Global Hook Template

Follow these instruction to
[install Talisman globally](https://github.com/thoughtworks/talisman#installation-as-a-global-hook-template)
only if you're confident that Talisman won't break your existing git hooks.

### Testing Talisman installed correctly

We can verify that Talisman is installed into the `as101-4-workshop` repository by viewing the
`.git/hooks/` folder. Open up a terminal in your `as101-4-workshop` repository and check with

```bash
ls -al .git/hooks/
```

If you've installed talisman globally, you should see a symlink entry which looks like this

```txt
pre-commit -> /Users/derwent/.talisman/bin/talisman_hook_script
```

If you've installed talisman to this repo only, you should see a single executable file entry which
looks like this

```txt
pre-commit
```

To verify that the pre-push binary is indeed talisman, you can run

```bash
TALISMAN_DEBUG=true .git/hooks/pre-commit
```

Which should output some talisman debug info.

## Ansible (Required for [Secrets](instructions/04_secrets.md) exercise)

There are two options to install ansible: globally or locally. Note that ansible installation is time-consuming (can take half an hour or more).

### Installing Ansible globally

Install using Homebrew:

```bash
brew install ansible
```

Or follow the [instructions](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#from-pip) on ansible's official site. 

### Installing Ansible locally via `virtualenv`. 

You'll need to insall `pyenv` (Python version management tool) and `pyenv-virtualenv` (a plugin to manage Python virtual environments on pyenv) via brew.

```
brew install pyenv
brew install pyenv-virtualenv
```
Update your bash configuration file `~/.bash_profile` (or ` ~/.zshrc ` in case you use Zsh) by running the following in your terminal.

```
echo ‘export PYENV_ROOT=”$HOME/.pyenv”’ >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
echo ‘eval “$(pyenv virtualenv-init -)”’ >> ~/.bash_profile
```
Run `source ~/.bash_profile` (or `source ~/.zshrc` if using Zsh) for the changes to take effect.

Create a new Python virtual environment for the version of Python you want. We are using 3.8.5 in this example.

```
pyenv install 3.8.5
pyenv virtualenv 3.8.5 <your-virtual-env-name>
```

Set the local Python environment in your forked project directory.
```
cd <path-to-your-directory>
pyenv local <your-virtual-env-name>
```
To confirm that you have the correct version of Python running in pyenv.
```
python -V
```
You should also see the newly created Python environment set in `.python-version` file in your forked repo directory.

Install Ansible into your virtual Python environment.

```
pip install ansible
```

To check that Ansible is isntalled correctly, run `ansible --version` and you should see Ansible version installed along with other information.
