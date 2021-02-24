from flask import Flask
import pymongo # Check if this import is okay: was not working until I disabled pylint
from pymongo import MongoClient
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# app = Flask(__name__)

# This is where we will put the connection URL to our DB as desired for PyMongo, and bind it to our app
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# client = MongoClient()
# db = client.new_db

# This is how we would connect to a database for mongoengine
# connect('mongoengine_test', host='localhost', port=27017)

# We also might want to use MONGOTHON: a python-api that mimics mongoose JS

## Look a MING for schema

# PyMongo usage example
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template("index.html",
#         online_users=online_users)

user = Blueprint('user', __name__)
# @simple_page.route('/<page>')

# Create/Register a new user
@user.route('/v1/user', methods=['GET'])
def register_user():
    return "<h1>Here is where we can have the user register!</h1>"

# Update preexising user profile
@user.route('/v1/user/update', methods=['PUT'])
def update_user():
    return "<h1>Here is where we can have the user update their profile/login information!</h1>"

# Log In as an existing user
@user.route('/v1/user/login', methods=['POST'])
def login_user():
    return "<h1>Here is where we can have the user login!</h1>"

# Log out as an existing user
@user.route('/v1/user/logout', methods=['DELETE'])
def logout_user():
    return "<h1>Here is where we can have the user log out!</h1>"

# ********************************************************************************
# Basic Getters/Setters for Users below

# Fetch user profile data by username (other?)
@user.route('/v1/user/:username', methods=['GET'])
def fetch_user():
    return "<h1>Here is where we can fetch the user's information!</h1>"

# Check if a profile exists with the given username
@user.route('/v1/user/:username', methods=['HEAD'])
def check_user():
    return "<h1>Here is where we can check if a user exists!</h1>"