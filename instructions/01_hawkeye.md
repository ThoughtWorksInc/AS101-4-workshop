# Exercise 1

## Prerequisites

If you haven't already done so, you will need to follow the [Setup Instructions](00_setup.md) before
continuing

## Hawkeye

We will use [Hawkeye](https://github.com/hawkeyesec/scanner-cli) to scan automatically scan the code
base for secrets and vulnerabilities. This is a useful tool to have in your pipeline, in order to
prevent anyone in your team from accidentally committing secrets or vulnerabilities.

**Note:** normally you would use the `hawkeyesec/scanner-cli:latest` docker image, however this is
currently using an outdated version of the [safety](https://pypi.org/project/safety/) pypi package
(see: <https://github.com/hawkeyesec/scanner-cli/issues/163>). so for this exercise I have created
my own docker image at `derwentx/scanner-cli:latest` which has the latest version while I wait for
the a request to go through. Do not use my docker image in production, this is only a temporary fix.

**Note:** Hawkeye also makes some assumptions about your repository structure. In this case,
`requirements.txt` needs to be in the root of the folder that is being scanned, this is why the
docker command mounts the `web/` directory at `/target` in the container instead of the root of the
repository.

You can use the Hawkeye docker image to scan your repository with:

```bash
docker run --rm -v "$PWD/web:/target" derwentx/scanner-cli:latest
```

Did you find anything interesting?

**Note:** If you run Hawkeye on the root of the repo with the `java-find-secbugs` enabled, and you
have Talisman installed globally, then there may be a symlink in `.git/hooks/pre-commit` that will
trip up Hawkeye with the following error:

```txt
[error] Unexpected error occurred! ENOENT: no such file or directory, stat '/target/.git/hooks/pre-commit'
```

This is why I have added a `.hawkeyerc` to disable the `java-find-secbugs` module.
