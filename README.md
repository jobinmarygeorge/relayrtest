# relayrtest

Software versions
*****************
minikube version: v1.14.0
helm version    : v3.4.1
kubectl version : v1.19.2 [server]
kubectl version : v1.18.6 [client]

create the helm chart with help pf create command of helm
**************************************************

helm create relayr

add mysql dependency to the Chart.yml file
dependencies:
  - name: mysql
    version: chart version 
    repository: repo 
    condition: enable condition

add the dependency details in the vaules.yaml file as well


creating secrets
****************

for creating secrets create a helm_vars directory

add you data to be stored as encrypted

in our case database details are stored 

1. database password      : MYSQLDB_PASSWORD
2. database               : MYSQL_DATABASE
3. database user          : MYSQLDB_USER
4. database root_password : MYSQL_ROOT_PASSWORD

create the data basesetails save it secrets file in followoing format

mariadb:
    auth:
        database: <database>
        password: <password >
        username: <username>
        rootPassword: <rootpassword>

once saved generate the pgp key. [which should be installed plugin to be installed ]

add a new file to the helm_vars file named .sops.yaml

1. create gpg key gpg --gen-key
2. gpg --fingerprint to get the finger print
3. add the this valuie to .sops.yanl file 
    ---
    creation_rules:
      - pgp: 'add the value to the gpg key'
4. encrypt the value in secrets.yaml 
    helm secrets enc ./helm_vars/secrets.yaml

5. you can decrypt and check value
    helm secrets dec ./helm_vars/secrets.yaml 
    cat value in secrets.yaml.dec


Running the appplication 
1. check dependencies
  helm repo update
  helm dep update

2. encrypt the secrets
3. check the encrypted values
4. run in debug --dry run mode to check the whole structure
  helm secrets install appname . -f ./helm_vars/secrets.yaml -f values.yaml  --dry-run --debug
   appname= relayr


Accesing the application
************************

1. run minikube 
2. access the with http://minikubeip:nodeport
3. create table for database [table name alredy given as hello ]
  http://minikubeip:nodeport/create_table

4. access  http://minikubeip:nodeport/login to add the string to the database table
5. access the data from database with http://minikubeip:nodeport/temp