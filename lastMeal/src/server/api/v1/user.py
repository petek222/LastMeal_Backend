from flask import Flask
import pymongo
from pymongo import MongoClient
import functools
from lastMeal.src.server.models.user import User # 'Error' is just IDE complaining

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Blueprint for connection to main process
user = Blueprint('user', __name__)

# Create/Register a new user
@user.route('/v1/user', methods=['GET'])
def register_user():
    print("Hey There!")
    mongo_client = MongoClient('localhost', 27017)
    host_info = mongo_client['HOST']
    print ("\nhost:", host_info)
    print("lets create a user!")
    
    # Using mongoengine/pymongo schema
    my_user = User(email='pedrobabon@gmail.com', first_name='pedro', last_name='babon').save()

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