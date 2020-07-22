# Exercise 3 - CI/CD

## TODO

- rewrite this to use GitHub Actions

## 03-01 Install the build server

Run the build server by following the instructions in the `sample-deploy-pipeline` Jenkins repository located [here](https://github.com/wilvk/sample-deploy-pipeline/blob/master/getting-started.md).

## 03-02 Run the Flask application via the build server

The Flask application consists of two docker containers:

- A frontend website written in Python Flask
- A backend database using PostgreSQL

It is a simple message-posting application where messages entered by the user in the web interface are written to the PostgreSQL database. The web front-end shows all messages entered by users.

Configure the CI/CD pipeline by following instructions available in [building-the-pipeline.md](https://github.com/wilvk/sample-deploy-pipeline/blob/master/building-the-pipeline.md)

## 03-03 Install and run Hawkeye

Follow the instructions available in [adding-hawkeye.md](https://github.com/wilvk/sample-deploy-pipeline/blob/master/adding-hawkeye.md)
