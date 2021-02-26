from flask import Flask
import pymongo
from pymongo import MongoClient
import functools
from lastMeal.src.server.models.user import User # 'Error' is just IDE complaining
import bcrypt

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Blueprint for connection to main process
user = Blueprint('user', __name__)

# Connect to DB
mongo_client = MongoClient('localhost', 27017)
db = mongo_client["user"] # Added line to have access to db
host_info = mongo_client['HOST'] 

# Create/Register a new user
@user.route('/v1/user', methods=['GET'])
def register_user():
    print("Hey There!")
    print ("\nhost:", host_info)
    print("lets create a user!")

    # Obviously these fields will need to take in the JSON sent from the client in actuality
    # This is just for testing
    username = 'pedobabon22'
    email = 'peter.e.koncelik@vanderbilt.edu'
    user_salt = bcrypt.gensalt()
    password = "userpassword"
    user_hash = bcrypt.hashpw(password.encode('utf-8'), user_salt) # Make sure this accepts API argument when real

    validation = User()
    
    # First check if a user with the given username/email already exists
    if db.user.find({'username': { "$in": [username]}}).count() > 0 or db.user.find({'email': { "$in": [email]}}).count() > 0:
        return "<h1>Username/Email already exists: please try different values</h1>" 

    # Perform Validation Checks on requisite fields, and create the user if valid
    if validation.validate_username(username) and validation.validate_email(email):
        # Using mongoengine/pymongo schema
        my_user = User(username = username, email=email, first_name='pedro', last_name='babon', salt=user_salt, hash=user_hash).save()
        return "<h1>User Successfully Registered!"

    # Otherwise return a false (change for API as needed)
    else:
        return "<h1>Invalid Username/Email, please try again!</h1>"

# Log In as an existing user
# Remember to add in user_sessions here for logins
@user.route('/v1/user/login', methods=['POST'])
def login_user():
    return "<h1>Here is where we can have the user login!</h1>"

# Update preexising user profile
@user.route('/v1/user/update', methods=['PUT'])
def update_user():
    return "<h1>Here is where we can have the user update their profile/login information!</h1>"

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