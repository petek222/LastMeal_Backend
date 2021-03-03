## LastMeal: Native App Backend

This repo contains all the backend code for the API of the LastMeal team's application. We are writing the API itself with Flask, connecting to a MongoDB instance for the database, and cloud deploying via AWS. Actual code to be added over time. 

### Serving the app:

Nginx is listening on port 80, and routes incoming traffic to the last\_meal.sock file in the ~/last\_meal directory. Gunicorn is running as a systemd process, and is bound to that socket as well, passing along requests to the app itself, which is made available through the wsgi.py file in ~/last\_meal/lastMeal

Both nginx and the last\_meal systemd process should be enabled in systemctl, meaning they're on by default when the server reboots. To see if this is the case, run:

```
sudo systemctl status nginx last_meal
```

If either of these are not active, try:

```
sudo systemctl start foo
```

If you make a change to the configuration files for nginx or the last\_meal systemd process:

```
sudo systemctl restart foo
```

Lastly, while this configuration is useful for running a server, it doesn't provide a wealth of debug information. In order to run the server locally, where (I believe) you'll be able to print to the console, do:

```
sudo systemctl stop last_meal
```

Then navigate to ~/last\_meal and run 

```
export FLASK_APP=lastMeal
export FLASK_ENV=development
. venv/bin/activate
flask run --host=0.0.0.0
```

And send requests to http://$SERVER\_IP:5000

## API Reference: User

The User API contains a number of endpoints that are useful for providing basic profile and user mangement features

### Register

Used to create a new user account

**URL** : `/v1/user/register`

**Methods** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[8 < length < 19]",
    "password": "[8 < length < 19]"
    "email": "[valid email address]""
} 
```

**Data example**

```json
{
    "username": "pedrobabon",
    "password": "1849Sicily",
    "email": "pedrobabon@myspace.com",
    "first_name": "Pedro",
    "last_name": "Babon"
}
```

#### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "pedrobabon"
    "email": "pedrobabon@myspace.com"
}
```



#### Error Response

**Condition** : If 'username'/'password'/etc invalid.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Invalid username/password"
}
```

**Condition** : If 'username'/'email' already exist in account.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "account with supplied username/email already exists"
}
```
