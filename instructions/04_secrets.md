# Exercise 4 - Handling secrets

## TODO
- update readme, make it more readable and complete the TBD items 

## Prerequisites

If you haven't already done so, you will need to follow the [Setup Instructions](00_setup.md) before
continuing.

## Remove secrets in code

We will update our code to remove secrets in code and instead, use a secret manager to source them.

1. Encrypting sensitive variables

   Go to your forked repo directory and create an encrypted file with credentials for Postgres in it:
   ```
   ansible-vault create env_secrets
   ```
   You'd be asked to create a password for Ansible Vault. Make sure it's a strong password and store it somewhere secure, e.g. using a password manager.
  
   Once the password is entered, you'll need to paste the content of what you want to encrypt. See the format below, but make sure to replace the values with the Postgres values from the docker-compose.yml file.
   
   ```
   POSTGRES_USER="user"
   POSTGRES_PASSWORD="password"
   POSTGRES_DB="db-name"
   ```
  
1. Viewing and editing the encrypted file

   In case you've made a mistake or you want to check what is currently stored in your encrypted file, `view` and `edit` commands come in handy.

   To view the file:
   ```
   ansible-vault view env_secrets
   ````
   To edit the file:
   ```
   ansible-vault edit env_secrets
   ```  
   By default, `vi` editor would be used. You can pass in your preferred editor like so:

   `EDITOR='nano' ansible-vault edit env_secrets`
  
   For both of these commands you'd be asked to enter a password. For ease of use you could store the ansible-vault password locally, just make sure this is not in any of the repo directories. To view the encrypted file - pass in the location of the vault password:

   `ansible-vault view --vault-password-file=<path_to_vault_password> env_secrets`


1. The encrypted variables for postgress then need to be referenced in the docker-compose.yml file:
	
   ```
   POSTGRES_USER: ${POSTGRES_USER}
   POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
   POSTGRES_DB: ${POSTGRES_DB}
   ```   
   Note that we don't need to add these variables to .env file as these would be picked up from the shell. More info on passing in variables [here](https://vsupalov.com/docker-arg-env-variable-guide/) and on the variables lookup order - [here](https://vsupalov.com/override-docker-compose-dot-env/).

1. Running locally

   Go to your forked repo directory and export the previously encrypted variables to the shell environment:
   
   ```
   set +x
   export $(ansible-vault view --vault-password-file=<path_to_vault_password> env_secrets|xargs)
   ```
  
   Note: `set +x` makes sure we are not logging out the value of the variables to the standard output.

   To test what your docker-compose file will look like after the substitution run:

   `docker-compose config`

   Rebuild the containers from scratch and test your system works as expected (there should not be any errors and you should be able to submit a new message).
	
    ```
   docker-compose rm -f
   docker-compose pull  
   docker-compose up --build -d
   ```

   Once test passed, you can stop the containers:
   `docker-compose stop -t 1`

   Commit and push your changes. Note, you'd need to update the .talismanrc file in order to commit your changes.

1. Running in a pipeline

   Notice that one of your workflows just failed - lint_test. The reason for this is that you've extracted the postgres variables, but haven't specified where these values should be taken from. When we run our application locally, we've been exposing the variable values through the shell. 
We need to do a similar thing for the pipeline.

   First of all, you'd need to provide a source of the vault password.
   Luckily, github offers an option to add the secrets via: 
   Your forked repo -> Settings -> Secrets -> 'New repository secret'
   Name this secret as `VAULT_PASS`.

   To extract Postgres variables from the encrypted env_secrets file we are going to use GitHub actions.
   In your .github directory create the following folder structure: actions/prep. 
   In the prep folder create the following 3 files: Dockerfile, action.yml and entrypoint.sh.
 
   TODO :explain the usage of action.yml, Dockerfile, entrypoint.sh

   Contents for action.yml:
   
   ```
   name: 'Prep'
   descript: 'Prepares the environment variables'
   runs:
    using: 'docker'
    image: 'Dockerfile'
   ```
   Contents for the Dockerfile:
   
   ```
   FROM alpine
   RUN apk add --update ansible
   COPY entrypoint.sh /entrypoint.sh
   ENTRYPOINT ["/entrypoint.sh"]
   ```
   Contents for entrypoint.sh:
   
   ```
   #!/bin/sh
   echo $VAULT_PASS > /vault_pass.txt
   echo $(ansible-vault view --vault-password-file=/vault_pass.txt env_secrets)|xargs -n1 >> $GITHUB_ENV 
   rm /vault_pass.txt
   ```
   Note that for entrypoint.sh you have to have proper permissions: 
   
   `chmod +x entrypoint.sh`

   Now we need to update the existing workflow where Postgres variables are currently used and specify the source for them.
   We need to add the following steps to  lint_test.yml :
  
  ```
    - uses: ./.github/actions/prep
      env:
        VAULT_PASS: ${{ secrets.VAULT_PASS }}
    - name: hide credentials from the output
      run: |
        echo "::add-mask::$POSTGRES_USER"
        echo "::add-mask::$POSTGRES_PASSWORD"
        echo "::add-mask::$POSTGRES_DB"
   ```
   These would set the VAULT_PASS environment variable and mask Postgres variables. 
   Note there is a known [issue](https://github.com/actions/runner/issues/475) currently with `add-mask` that results in the variables being printed out in the    pipeline in plaintext the 1st time after the mask is added. 

   Once you push these changes, the lint_test workflow should be passing now in the pipeline.
