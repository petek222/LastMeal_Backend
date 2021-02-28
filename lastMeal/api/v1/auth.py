import functools
import bcrypt
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from lastMeal.models.user import User
from pymongo import MongoClient

# Blueprint for connection to main process
bp = Blueprint('auth', __name__, url_prefix='/v1/user')

# Connect to DB
mongo_client = MongoClient('localhost', 27017)
db = mongo_client["user"] # Added line to have access to db
host_info = mongo_client['HOST'] 

# Create/Register a new user
# We want to replace the returns and params with JSON grabs and responses
# This also needs more robust error handling via try-catch
@bp.route('', methods=['GET'])
def register_user():
    print ("\nhost:", host_info)
    print("let's try to register a new user!")

    # Obviously these fields will need to take in the JSON sent from the client in actuality
    # This is just for testing
    username = 'tedk2'
    email = 'teddy.koncelik@loyola.edu'
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
# Currently sessions are omitted/being punted to the native client
# We want to replace the returns and params with JSON grabs and responses
# This also needs more robust error handling via try-catch
@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    print("let's try to login a new user")

    # grab data from request body and instiantiate validator
    request_data = request.json
    validation = User()

    username = request_data['username']
    password = request_data['password']

    # First check that the given username even exists in the db
    if not db.user.find({'username': { "$in": [username]}}).count() > 0:
        return "<h1>Supplied username does not exist</h1>" 
    
    # If the user exists, we grab the stored salt and hash from the db
    user_data = db.user.find_one({'username': username}, {'hash':1, 'salt':1, 'email':1})
    stored_hash = user_data['hash']
    stored_salt = user_data['salt']
    stored_email = user_data['email']

    # Impl doesnt use salt due to builtin
    if bcrypt.checkpw(password.encode('utf8'), stored_hash.encode('utf8')):
        response_obj = {
            "username": username,
            "email": stored_email
        }
        resp = make_response(response_obj, 200)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    else:
        error_obj = {
            "error": "unauthorized"
        }
        resp = make_response(error_obj, 401)
        resp.headers['Content-Type'] = 'application/json'
        return resp

# Update preexising user profile
@bp.route('/v1/user/update', methods=['PUT'])
def update_user():
    return "<h1>Here is where we can have the user update their profile/login information!</h1>"

# Log out as an existing user
@bp.route('/logout', methods=['DELETE'])
def logout_user():
    return "<h1>Here is where we can have the user log out!</h1>"

# ********************************************************************************
# Basic Getters/Setters for Users below

# Fetch user profile data by username (other?)
@bp.route('/:username', methods=['GET'])
def fetch_user():
    return "<h1>Here is where we can fetch the user's information!</h1>"

# Check if a profile exists with the given username
@bp.route('/:username', methods=['HEAD'])
def check_user():
    return "<h1>Here is where we can check if a user exists!</h1>"
