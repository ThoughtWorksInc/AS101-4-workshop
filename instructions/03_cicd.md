# Exercise 3 - CI/CD

This repository has a GitHub Action workflow in `.github/workflows/lint_test.yml`. This file tells
GitHub what to do each time a commit / pull request is submitted. In this example, we're simply
running `flake8` (Python linter) inside the `web` docker container.

In this exercise, we will modify this repository's workflows to add a second workflow definition
which automatically scans the repo with Hawkeye.

You can read more about GitHub workflow definitions
[here](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions).

## Prerequisites

If you haven't already done so, you will need to follow the [Setup Instructions](00_setup.md) before
continuing. In particular, ensure that you have
[forked this repository](00_setup.md#forking-the-repository) (please do not push solutions to this exercise to the `thoughtworksinc` repository).

## Create the workflow definition

Go to `.github/workflows` and create a new workflow file `hawkeye.yml` You can use the template yaml below as a starting point.

See if you can create a workflow called `Hawkeye Scan` which has the following steps

1. checks out the repo (`uses: actions/checkout@v2`)
2. runs `hawkeye scan --target web/` using the `scanner-cli` container.

For step two, You will need to use the
[`jobs.<job_id>.container`](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idcontainer)
syntax to run a step in the `scanner-cli` container. At the time of writing, it was necessary to use the
[jobs.<job_id>.container.options](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idcontaineroptions) syntax
to mount the cloned repository inside the container with
`-v /__w/as101-4-workshop/as101-4-workshop:/target`, so a skeleton yaml file with the
definition filled out for you has been provided below.

All you need to do is fill out the workflow name and define the second step of the job. Because we have configured the job to use the `scanner-cli` image, you should be able to run the `hawkeye` binary directly in this step. You step definition should only require you to use the run
[`run`](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstepsrun) keyword to execute `hawkeye scan --target web/`

```yml
name: ... # <Name your workflow>
# Controls when the action will run. Triggers the workflow on push or pull request on any branch
on: [push, pull_request]
# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "scan"
  scan:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    container:
      # This tells GitHub Actions to use our docker image
      image: hawkeyesec/scanner-cli:latest
      # This tells GitHub Actions to mount the location where the code was checked out to /target
      options: -v /__w/as101-4-workshop/as101-4-workshop:/target

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      - ... # <Fill out the second step>
```

When you've written your definition, simply push it to your fork on GitHub, and view the result in the Actions
tab of the repo. You might need to enable workflows as these are disabled by default.

![actions](images/../../images/actions_tab.png)

We expect the workflow to fail, since some of the dependencies are out of date.

## Fix Hawkeye errors

Try to modify your repository so that hawkeye does not show any critical errors locally.

Re-build the app and verify that it still works before pushing.
