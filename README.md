## LastMeal: Native App Backend

This repo contains all the backend code for the API of the LastMeal team's application. We are writing the API itself with Flask, connecting to a MongoDB instance for the database, and cloud deploying via AWS. Actual code to be added over time. 

## Serving the app:

#### For Group 3 members running on a server:

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

#### For local testing:

If you don't have a server or want to print debug information, you can run the app locally. Clone the repo, then navigate to last\_meal and run

```
export FLASK_APP=lastMeal
export FLASK_ENV=development
. venv/bin/activate
flask run --host=0.0.0.0
```

(Windows):

```
set FLASK_APP=lastMeal
set FLASK_ENV=development
venv\Scripts\activate
flask run --host=0.0.0.0
```

And send requests to http://$SERVER\_IP:5000

(If you want to run the app on the server, but still print debug information, the above steps must be prefaced with `sudo systemctl stop last_meal`.

## API Reference

* [User](user.md) : `/v1/user/`

