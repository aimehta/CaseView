# CaseView #
## Get started ##
### Step 1  ###
#### Pre requisites
    Operating System: Ubuntu 14.X
    Check requirements file to run commands or run install.sh to install the basic requirements.

|    Package           |       Version |
|-----------------------| ------- |
|asn1crypto          |    0.24.0|
|canonicaljson       |    1.1.4|
|cryptography        |    2.1.4|
|Django              |    1.8.4|
|django-cors-headers |    3.0.2|
|django-filter       |    1.0.2|
|django-smtp-ssl     |    1.0|
|djangorestframework |    3.3.0|
|djangorestframework-jwt| 1.11.0|
|enum34              |    1.1.6|
|frozendict          |    1.2|
|idna                |    2.6|
|ipaddress           |    1.0.17|
|iso8601             |    0.1.12|
|keyring             |    10.6.0|
|keyrings.alt        |    3.0|
|MySQL-python        |    1.2.5|
|pip                 |    19.1.1|
|psycopg2            |    2.8.5|
|pycrypto            |    2.6.1|
|Pygments            |    2.4.2|
|pygobject           |    3.26.1|
|PyJWT               |    1.7.1|
|python-dateutil     |    2.8.0|
|pytz                |    2019.1|
|pyxdg               |    0.25|
|SecretStorage       |    2.3.1|
|securesystemslib    |    0.11.3|
|setuptools          |    41.0.1|
|simplejson          |    3.16.0|
|six                 |    1.11.0|
|wheel               |    0.33.4|
    
### Step 2  ###

#### Create a directory called test in home directory

    goto terminal and run 
    ...
    mkdir test
    ...
   
    

### Step 3  ###
#### Clone the repository

    git clone https://github.com/aimehta/CaseView.git



### Step 4  ###
#### Server Basic Setup  ####

    cd cv
    sudo python manage.py makemigrations cv_api (follow the prompts)
    sudo python manage.py migrate (Tables will be created)
    sudo python manage.py createsuperuser (give admin as username and password and leave email blank)
    

### Step 5  ###
#### Start server  ####

    sudo python manage.py runserver (This will start the server on locahost port 8000)
    
### Step 6  ###
#### Call login api  ####

    Open another terminal window/tab
    
    Run:
    curl -k -v -H "Content-Type: application/json" -X POST http://localhost:8000/api-token-auth/ -d '{"username" : "admin", "password" : "admin" }'
    
    Output:
    
    Note: Unnecessary use of -X or --request, POST is already inferred.
    *   Trying 127.0.0.1...
    * TCP_NODELAY set
    * Connected to localhost (127.0.0.1) port 8000 (#0)
    > POST /api-token-auth/ HTTP/1.1
    > Host: localhost:8000
    > User-Agent: curl/7.58.0
    > Accept: */*
    > Content-Type: application/json
    > Content-Length: 45
    > 
    * upload completely sent off: 45 out of 45 bytes
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Date: Sun, 09 May 2021 09:14:02 GMT
    < Server: WSGIServer/0.1 Python/2.7.17
    < X-Frame-Options: SAMEORIGIN
    < Content-Type: application/json
    < Allow: POST, OPTIONS
    < 
    * Closing connection 0
    {"username":"admin","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MSwiZW1haWwiOiIiLCJleHAiOjE2MjA1NTUyNDJ9.1LASLXNiECGtX41LwmC21AYx5JfDd8-AIJVxp0hy94Y","success":true,"datetime":"2021-05-09 09:14:02.264393"}
    
 
    
    




