# Getting Started

## Requirements

This workshop requires the following tools to be installed on your machine:

- Docker
- Docker-compose

The easiest way to install these on MacOS is using the
[Homebrew package manager](https://docs.brew.sh/Installation).

See
[these instructions](https://medium.com/crowdbotics/a-complete-one-by-one-guide-to-install-docker-on-your-mac-os-using-homebrew-e818eb4cfc3)
for installing `docker`

`docker-compose` can be installed with the following terminal command

```bash
brew install docker-compose
```

## Pulling docker images

This is the slowest step of the exercise, so it's best to start it first so that it can run in the
background, and you can proceed to the next step while the images are downloading.

```bash
docker pull postgres:12.2  # from docker-compose.yml
docker pull python:3.7  # from web/Dockerfile
docker pull derwentx/scanner-cli:latest  # for exercise 1
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

change directory into your forked, cloned repository and make a note of the path.

```bash
cd as101-4-workshop
pwd
```

the `pwd` command will output your current directory.

```txt
/path/to/your/as101-4-workshop
```

## Using the Echo app

### Starting the Application

To see the sample app running, run the following terminal command:

`docker-compose up --build`

Then in your browser go to `localhost:8000`

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

If you're not sure about Talisman, you can install it
[on each repository individually](#installation-to-a-single-project). There are also instructions to
[install it globally](#installation-as-a-global-hook-template)

You will need to use of these sets of instructions to install talisman into the `as101-4-workshop`
repo so that we can scan it for secrets in the exercises.

### Installation to a single project

Talisman contains
[instructions](https://github.com/thoughtworks/talisman#installation-to-a-single-project) for
installing to a single repository, however these instructions install a version of Talisman that is
2 years out of date and is incompatible with these exercises.

I have made some modification to install.sh which are currently being reviewed in this
[pull request](https://github.com/thoughtworks/talisman/pull/249) which install a newer `talisman`
binary and allow you to install talisman as a `pre-commit` hook instead of a `pre-push` hook.

While that's being reviewed, you can use these instructions instead:

```bash
# Download the talisman installer script
curl https://raw.githubusercontent.com/derwent-m/talisman/master/install.sh > ~/install-talisman.sh
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
