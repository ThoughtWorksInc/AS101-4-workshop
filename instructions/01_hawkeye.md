# Exercise 1

## Prerequisites

If you haven't already done so, you will need to follow the [Setup Instructions](00_setup.md) before
continuing.

## Hawkeye

We will use [Hawkeye](https://github.com/hawkeyesec/scanner-cli) to automatically scan the code
base for secrets and vulnerabilities. This is a useful tool to have in your pipeline, in order to
prevent anyone in your team from accidentally committing secrets or vulnerabilities.

You can use the Hawkeye docker image to scan your repository with:

```bash
docker run --rm -v "$PWD/web:/target" hawkeyesec/scanner-cli:latest
```

Did you find anything interesting?

**Note:** If you run Hawkeye on the root of the repo with the `java-find-secbugs` enabled, and you
have Talisman installed globally, then there may be a symlink in `.git/hooks/pre-commit` that will
trip up Hawkeye with the following error:

```txt
[error] Unexpected error occurred! ENOENT: no such file or directory, stat '/target/.git/hooks/pre-commit'
```

If you get the error shown above, add the `java-find-secbugs` module  to `.hawkeyerc` to resolve the error.
