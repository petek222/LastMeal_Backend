import functools
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from lastMeal.models.user import User
from bson.objectid import ObjectId

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


# Blueprint for connection to main process
bp = Blueprint('auth', __name__, url_prefix='/v1/user')

# Create/Register a new user
# ******************************************************************************
#
# @method: POST
# @param request_data['username'] username for account
# @param request_data['password'] password for account
# @param request_data['email'] email for account
# @param first_name = request_data['first_name']
# @param last_name = request_data['last_name']
@bp.route('/register', methods=['POST'])
def register_user():
    print("let's try to register a new user!")

    request_data = request.json

    # Grab the needed fields from request body
    username = request_data['username']
    email = request_data['email']
    password = request_data['password']
    firstName = request_data['first_name']
    lastName = request_data['last_name']

    # First check if a user with the given username/email already exists
    if User.objects(username=username) or User.objects(email=email):
        return ({"error": "account with supplied username/email already exists"}, 400)

    # Using mongoengine/pymongo schema to create and save the user
    my_user = User(username = username, email=email, first_name=firstName, last_name=lastName)
    try:
        my_user.set_password(password)
        my_user.validate()
        my_user.save()
        return ({"username": username, "email": email}, 201)
    except Exception as e:
        print(e)
        return ({"error": "Invalid username/password"}, 400)
        return resp

# Log In as an existing user
# Currently sessions are omitted/being punted to the native client
# ******************************************************************************
#
# @method: GET, POST
# @param request_data['username'] username for login
# @param request_data['password'] password for login
@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    print("let's try to login a new user")

    # grab data from request body and instiantiate validator
    request_data = request.json

    username = request_data['username']
    password = request_data['password']

    # First check that the given username even exists in the db
    if not User.objects(username=username):
        return ({"error": "supplied username does not exist"}, 400)

    try:
        # If the user exists, we grab it from the db
        user_data = User.objects(username=username).first()

        # Impl doesnt use salt due to builtin
        if user_data.authenticate_user(password):
            access_token = create_access_token(identity=username)
            return ({"username": username, "email": user_data.email, "token": access_token}, 200)
        else:
            return ({"error": "unauthorized"}, 401)
    except Exception as e:
        print(e)
        return ({"error": "Login unsuccessful"}, 401)

# Update preexising user profile (not including password)
# Let a user update their username, email, first name, lastname
# ******************************************************************************
#
# @method: PUT
# @path /update/<username>: current username of account to change
# (needed to separate for username changes)
# @param request_data['username'] username for login
# @param request_data['password'] password for login
@bp.route('/update/<username>', methods=['PUT'])
@jwt_required()
def update_user_profile(username):
    print("Update preexisting user")
    if (username != get_jwt_identity()):
        return ({"error": "unauthorized"}, 401)

    # grab data from request body and instiantiate validator
    request_data = request.json

    # First check that the given username even exists in the db
    if not User.objects(username=username):
        return ({"error": "supplied username does not exist"}, 400)

    # Otherwise, use mongoengine/pymongo schema to update and save the user's information
    try:
        User.objects(username=username).first().update(**request_data)
        return ({"data_updated": request_data}, 201)
    except Exception as e:
        print(e)
        return ({"error": "Update Unsucessful"}, 400)

# Change the password of a preexising user profile 
# Let a user update their username, email, first name, lastname
# ******************************************************************************
#
# @method: PUT
# @path /password/<username>: username of account to receive password change
# @param request_data['password'] password for account login
@bp.route('/password/<username>', methods=['PUT'])
@jwt_required()
def update_user_password(username):
    if (username != get_jwt_identity()):
        return ({"error": "unauthorized"}, 401)

    # grab data from request body and instiantiate validator
    request_data = request.json
    changed_password = request_data['password']

    try:
        current_user = User.objects(username=username).first()
        
        current_user.set_password(changed_password)
        current_user.validate()
        current_user.save()
        return ({"username": username}, 201)
    except Exception as e:
        print(e)
        return ({"error": "Invalid username/password"}, 400)

# Log out as an existing user
@bp.route('/logout', methods=['GET'])
def logout_user():
    return "Placeholder: this will most likely be handled by the frontend"

# ********************************************************************************
# Basic Getters/Setters for Users below

# Fetch user profile data by username 
# ******************************************************************************
#
# @method: GET
# @path /<username>: username corresponding to the account of interest
@bp.route('/<username>', methods=['GET'])
@jwt_required()
def fetch_user(username):
    if (username != get_jwt_identity()):
        return ({"error": "unauthorized"}, 401)

    # First check that the given username even exists in the db
    if not User.objects(username=username):
        return ({"error": "supplied username does not exist"}, 404)

    # If the user exists, we grab it from the db and return it
    user_data = User.objects.get(username=username).to_json()
    return (user_data, 200)
    

# Check if a profile exists with the given username
# ******************************************************************************
#
# @method: HEAD
# @path /<username>: username corresponding to the account of interest
@bp.route('/<username>', methods=['HEAD'])
def check_user(username):
    # If the user does not exist, send back a 404 not found
    if not User.objects(username=username):
        return ('', 404)
    # If the user exists, return a status 200
    else:
        return ('', 200)
    

