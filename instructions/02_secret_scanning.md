# Exercise 2 - Secret Scanning

## Prerequisites

If you haven't already done so, you will need to follow the [Setup Instructions](00_setup.md),
ensuring the Talisman Git hook is installed before continuing.

## Secret detection with Git hooks

For this exercise, running the application is not necessary.

1. In our sample application, create and `checkout` a new branch called `test`, so that you can
   easily revert the changes in the following instructions. e.g. `git checkout -b 'test'`

1. In our sample application, create the file `danger.pem` in a text editor of your choice and add
   the line `awsSecretKey=c64e8c79aacf5ddb02f1274db2d973f363f4f553ab1692d8d203b4cc09692f79` to the
   file and save it. e.g.
   `echo 'awsSecretKey=c64e8c79aacf5ddb02f1274db2d973f363f4f553ab1692d8d203b4cc09692f79' > danger.pem`

1. Do a git add of the file. e.g. `git add danger.pem`.

   Then do a git commit. e.g. `git commit -m "testing talisman"`

   If all is working, you should be prompted by talisman about a potential secret being checked-in.

1. Let's pretend that `danger.pem` is a secret that we actually want in our repository, Use the
   output of Talisman to create a `.talismanrc` to allow this secret to be committed. The
   information you need is in the Talisman Report section, above the following message:

   ```txt
   If you are absolutely sure that you want to ignore the above files from talisman detectors, consider pasting the following format in .talismanrc file in the project root
   ```

   Your `.talismanrc` should allow you to commit file without warnings.

1. You can then unstage your changes and checkout all files to revert your local repository to its
   previous state.

   For example:

   ```sh
   git reset --hard master
   ```

1. Spend a few minutes experimenting with other (fake) secrets. What does Talisman find? What does
   it miss?
