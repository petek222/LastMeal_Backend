import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from lastMeal.models.user import User
from bson.objectid import ObjectId


# Blueprint for connection to main process
bp = Blueprint('auth', __name__, url_prefix='/v1/user')

# Create/Register a new user
# ******************************************************************************
#
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

    #How to create a pantry object whenever we create a user object?
    pantry_id = ObjectId()

    # First check if a user with the given username/email already exists
    if User.objects(username=username) or User.objects(email=email):
        response_obj = {
            "error": "account with supplied username/email already exists"
        }
        resp = make_response(response_obj, 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    # Using mongoengine/pymongo schema to create and save the user
    my_user = User(username = username, email=email, first_name=firstName, last_name=lastName, pantry=pantry_id)
    try:
        my_user.set_password(password)
        my_user.validate()
        my_user.save()
        response_obj = {
            "username": username,
            "email": email
        }
        resp = make_response(response_obj, 201)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    except Exception as e:
        print(e)
        response_obj = {
            "error": "Invalid username/password"
        }
        resp = make_response(response_obj, 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp

# Log In as an existing user
# Currently sessions are omitted/being punted to the native client
# ******************************************************************************
#
# @param request_data['username'] username for login
# @param request_data['password'] password for login
@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    print("let's try to login a new user")

    # grab data from request body and instiantiate validator
    request_data = request.json
    validation = User()

    username = request_data['username']
    password = request_data['password']

    # First check that the given username even exists in the db
    if not User.objects(username=username):
        response_obj = {
            "error": "supplied username does not exist"
        }
        resp = make_response(response_obj, 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    # If the user exists, we grab it from the db
    user_data = User.objects(username=username)[0]

    # ** Add a try-catch here to deal with any auth problems **

    # Impl doesnt use salt due to builtin
    if user_data.authenticate_user(password):
        response_obj = {
            "username": username,
            "email": user_data.email
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
# Let a user update their username, password, email, first name, lastname
# ******************************************************************************
#
# @param request_data['current_username'] username currently tied to account
# @param request_data['username'] username for login
# @param request_data['password'] password for login
@bp.route('/update', methods=['PUT'])
def update_user():
    print("Update preexisting user")

    # grab data from request body and instiantiate validator
    request_data = request.json
    current_username = request_data['current_username']
    validation = User()

    # Using mongoengine/pymongo schema to update and save the user's information
    # my_user = User(username = username, email=email, first_name=firstName, last_name=lastName, pantry=pantry_id)
    try:
        # my_user.set_password(password)
        # my_user.validate()
        # my_user.save()
        user_query = {"username": current_username}
        # user_update_obj = {'$set': request_data}

        validation = User()

        print("TEST")
        # print(User.objects(username=current_username))
        print(current_username)

        User.objects(username=current_username)
        
        # data.update(username=request_data['username'])


        response_obj = {
            "username": "HIIII",
            "email": "HEEEEE"
        }
        resp = make_response(response_obj, 201)
        resp.headers['Content-Type'] = 'application/json'
        return resp
    except Exception as e:
        print(e)
        response_obj = {
            "error": "Invalid username/password"
        }
        resp = make_response(response_obj, 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp



# Log out as an existing user
@bp.route('/logout', methods=['GET'])
def logout_user():
    return "Placeholder: this will most likely be handled by the frontend"

# ********************************************************************************
# Basic Getters/Setters for Users below

# Fetch user profile data by username (other?)
@bp.route('/<username>', methods=['GET'])
def fetch_user(username):

    # First check that the given username even exists in the db
    if not User.objects(username=username):
        response_obj = {
            "error": "supplied username does not exist"
        }
        resp = make_response(response_obj, 400)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    # If the user exists, we grab it from the db and return it
    user_data = User.objects.get(username=username).to_json()
    response_obj = user_data
    resp = make_response(response_obj, 200)
    resp.headers['Content-Type'] = 'application/json'
    return resp
    

# Check if a profile exists with the given username
@bp.route('/<username>', methods=['HEAD'])
def check_user(username):

    # If the user does not exist, send back a 404 not found
    if not User.objects(username=username):
        resp = make_response(404)
        return resp

    # If the user exists, we grab it from the db and return it
    user_data = User.objects.get(username=username).to_json()
    resp = make_response(200)
    return resp
    

