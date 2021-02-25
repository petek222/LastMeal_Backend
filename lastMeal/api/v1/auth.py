import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from lastMeal.models import User

bp = Blueprint('auth', __name__, url_prefix='/v1/user')

# Create/Register a new user
@bp.route('', methods=['GET'])
def register_user():
    print("Hey There!")
    print("lets create a user!")

    my_user = User(email='pedrobabon@gmail.com', first_name='pedro', last_name='babon').save()

    return "<h1>Here is where we can have the user register!</h1>"

# Update preexising user profile
@bp.route('/update', methods=['PUT'])
def update_user():
    return "<h1>Here is where we can have the user update their profile/login information!</h1>"

# Log In as an existing user
@bp.route('/login', methods=['POST'])
def login_user():
    return "<h1>Here is where we can have the user login!</h1>"

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
