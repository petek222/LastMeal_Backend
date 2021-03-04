from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
import json
from lastMeal.models.user import User
from bson.objectid import ObjectId

# Blueprint for connection to main process
bp = Blueprint('pantry', __name__, url_prefix='/v1/pantry')


# Create a new ingredient and associate it with a user
# ******************************************************************************
@bp.route('/create/<username>', methods=["POST"])
def create_ingredient(username):
    print("Creating a new ingredient.")

# Retrieve all ingredients associated with a user
# ******************************************************************************
@bp.route('/<username>', methods=["GET"])
def create_ingredient(username):
    print("Retrieving ingredients.")

# Update an ingredient based on the ingredient ID
# ******************************************************************************
@bp.route('/update/<ingredient_id>', methods=["POST"])
def create_ingredient(ingredient_id):
    print("Updating ingredient.")

# Delete an ingredient based on the ingredient ID
# ******************************************************************************
@bp.route('/delete/<ingredient_id>', methods=["DELETE"])
def create_ingredient(ingredient_id):
    print("Deleting ingredient.")