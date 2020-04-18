## Talisman

[Talisman](https://github.com/thoughtworks/talisman) is a Secrets Scanning application for git to prevent committing and pushing of secrets to your git source control server.

It works by using git hooks into the local copy of the source code you are working on.

We want to run Talisman on this repository to scan it for secrets.

### Installing Talisman

We want to follow the instructions on the [Talisman README.md](https://github.com/thoughtworks/talisman#installation-as-a-global-hook-template
) for installing Talisman as a global hook template.

Before we install Talisman, change directory into your forked, cloned repository and make a note of the path.

```bash
$ cd sample-flask-app
$ pwd
/Users/willvk/source/wilvk/sample-flask-application
```

We can then download and run an install script to load the Talisman binaries for our specific Operating System. At the prompt for what local repositories to add the hook to, enter the path listed by `pwd` above for your repository. This will prevent it installing Talisman for all the repositories under your home path.

```
curl --silent \
https://raw.githubusercontent.com/thoughtworks/talisman/master/global_install_scripts/install.bash \
  /tmp/install_talisman.bash && /bin/bash /tmp/install_talisman.bash
```

For example:

![](./images/1.png)

Talisman also sets an environment variable called `$TALISMAN_HOME` in your bash profile that points to the home path of Talisman on your system. This needs to be present in your resource file (`.bashrc`, `.bash_profile`, `.zshrc`, etc) for Talisman to run. You may need to either source your bash profile or restart the terminal to make sure it is there.

You can check it is present by running:

```bash
$ env | grep TALISMAN_HOME
TALISMAN_HOME=/Users/willvk/.talisman/bin
```

### Testing Talisman installed correctly

From the command prompt, enter `talisman`. It should return a list of command options.

In our sample application, open the file `web/config.py` in a text editor of your choice. Add a benign change to the file by adding an exra line to the end of the file, or a space somewhere. It can be anything as long as it doesn't affect the code.

Save the file.

Do a git add of the file. e.g. `git add web/config.py`.

Then do a git commit. e.g. `git commit -m "testing talisman"`

If all is working, you should be prompted by talisman about a potential secret being checked-in.

You can then unstage your changes and checkout all files to revert your local repository to it's previous state.

For example:

```sh
git reset
git checkout .
```
