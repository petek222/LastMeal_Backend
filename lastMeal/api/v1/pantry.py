from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, Response
)
import json
from datetime import datetime
from lastMeal.models.user import User
from lastMeal.models.ingredient import Ingredient
from bson.objectid import ObjectId

# Blueprint for connection to main process
bp = Blueprint('pantry', __name__, url_prefix='/v1/pantry')

# Create a new ingredient and associate it with a user
# ******************************************************************************
@bp.route('/create/<username>', methods=["POST"])
def create_ingredient(username):
    print("Creating a new ingredient.")
    request_data = request.json
    name = request_data["name"]
    quantity = request_data["quantity"]
    exp_date = request_data["expiration_date"]
    exp_date = datetime.strptime(exp_date, "%Y-%m-%d")
    user = User.objects(username=username)
    if user.first() == None:
        return ({"error": "requested user not found"}, 400)

    try:
        my_ingredient = Ingredient(name=name, quantity=quantity, expiration_date=exp_date, user=user.first())
        my_ingredient.save()
        return ({"name": name, "quantity": quantity, "expiration_date": exp_date}, 201)
    except Exception as e:
        print(e)
        return ({"error": "could not save requested ingredient"}, 401)

## Retrieve all ingredients associated with a user
## ******************************************************************************
#@bp.route('/<username>', methods=["GET"])
#def create_ingredient(username):
    #print("Retrieving ingredients.")

## Update an ingredient based on the ingredient ID
## ******************************************************************************
#@bp.route('/update/<ingredient_id>', methods=["POST"])
#def create_ingredient(ingredient_id):
    #print("Updating ingredient.")

## Delete an ingredient based on the ingredient ID
## ******************************************************************************
#@bp.route('/delete/<ingredient_id>', methods=["DELETE"])
#def create_ingredient(ingredient_id):
    #print("Deleting ingredient.")