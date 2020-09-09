# AppSec 101 Module 4 Workshop: Sample Flask Application

> :warning: **Warning:** this repository deliberately contains vulnerabilities for the purpose of an information security training course, do not use the code from this repository in production.

The application consists of two docker containers:

- A frontend website written in Python Flask
- A backend database using PostgreSQL

It is a simple message-posting application where messages entered by the user in the web interface are written to the PostgreSQL database. The web front-end shows all messages entered by users.

## Instructions

- [0. Setup](instructions/00_setup.md)
- [1. Hawkeye](instructions/01_hawkeye.md)
- [2. Secret Scanning](instructions/02_secret_scanning.md)
- [3. CI/CD](instructions/03_cicd.md)
