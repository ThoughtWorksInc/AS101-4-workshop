# Solutions

<!-- markdownlint-disable MD033 -->

Just in case things go wrongs, this is the expected output of each exercise.

You can compare these outputs to your own if you're confused by your outputs.

## Exercise 1

<details>
  <summary>Spoilers</summary>

```txt
  module         level     offender              description                                                                                                                                                                                                                                                                                                                                  mitigation
-------------  --------  --------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  --------------------------------------------------------------------------
python-bandit  low       ./config.py lines 6   hardcoded_password_string B105                                                                                                                                                                                                                                                                                                               Possible hardcoded password: 'changeme' Review the file and fix the issue.
python-bandit  low       ./config.py lines 10  hardcoded_password_string B105                                                                                                                                                                                                                                                                                                               Possible hardcoded password: 'postgres' Review the file and fix the issue.
python-piprot  low       Flask-Script          Module is one or more patch versions out of date                                                                                                                                                                                                                                                                                             Upgrade to v2.0.6 (Current: v2.0.5)
python-piprot  low       psycopg2              Module is one or more patch versions out of date                                                                                                                                                                                                                                                                                             Upgrade to v2.8.5 (Current: v2.8.4)
python-piprot  medium    SQLAlchemy            Module is one or more minor versions out of date                                                                                                                                                                                                                                                                                             Upgrade to v1.3.18 (Current: v1.1.4)
python-piprot  high      Werkzeug              Module is one or more major versions out of date                                                                                                                                                                                                                                                                                             Upgrade to v1.0.1 (Current: v0.11.10)
python-piprot  high      gunicorn              Module is one or more major versions out of date                                                                                                                                                                                                                                                                                             Upgrade to v20.0.4 (Current: v19.6.0)
python-safety  critical  flask 0.12            flask version Before 0.12.3 contains a CWE-20: Improper Input Validation vulnerability in flask that can result in Large amount of memory usage possibly leading to denial of service. This attack appear to be exploitable via Attacker provides JSON data in incorrect encoding. This vulnerability appears to have been fixed in 0.12.3.  Versions <0.12.3 are vulnerable. Update to a non vulnerable version.
python-safety  critical  werkzeug 0.11.10      Cross-site scripting (XSS) vulnerability in the render_full function in debug/tbtools.py in the debugger in Pallets Werkzeug before 0.11.11 (as used in Pallets Flask and other products) allows remote attackers to inject arbitrary web script or HTML via a field that contains an exception message.                                     Versions <0.11.11 are vulnerable. Update to a non vulnerable version.
python-safety  critical  werkzeug 0.11.10      The defaults of ``generate_password_hash`` in werkzeug 0.12 have been changed to more secure ones, see pull request ``#753``.                                                                                                                                                                                                                Versions <0.12 are vulnerable. Update to a non vulnerable version.
python-safety  critical  werkzeug 0.11.10      Werkzeug 0.15.0 refactors class:`~middleware.proxy_fix.ProxyFix` to support more headers, multiple values, and a more secure configuration.                                                                                                                                                                                                  Versions <0.15.0 are vulnerable. Update to a non vulnerable version.
```

</details>

## Exercise 3

<details>
  <summary>Spoilers</summary>

`.github/workflows/hawkeye.yml`:

```yml
# This is a basic workflow to help you get started with Actions

name: Hawkeye Scan

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
      image: derwentx/scanner-cli:latest
      # This tells GitHub Actions to mount the location where the code was checked out to /target
      options: -v /__w/as101-4-workshop/as101-4-workshop:/target

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
    # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
    - uses: actions/checkout@v2
    # Runs a set of commands using the runners shell
    - run: hawkeye scan --target web/
```

To satisfy hawkeye, just update the dependencies

</details>
