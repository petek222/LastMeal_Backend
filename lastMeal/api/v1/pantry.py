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

# Retrieve all ingredients associated with a user
# ******************************************************************************
@bp.route('/<username>', methods=["GET"])
def read_ingredient(username):
    print("Retrieving ingredients.")
    user = User.objects(username=username)
    if user.first() == None:
        return ({"error": "requested user not found"}, 400)
    return ({"ingredients": json.loads(Ingredient.objects(user=user.first()).to_json())}, 200)

# Update an ingredient based on the ingredient ID
# ******************************************************************************
@bp.route('/update/<ingredient_id>', methods=["POST"])
def update_ingredient(ingredient_id):
    print("Updating ingredient.")
    request_data = request.json
    ingredient = Ingredient.objects(id=ObjectId(ingredient_id))
    if ingredient.first() == None:
        return ({"error": "requested ingredient not found"}, 400)

    try:
        ingredient.first().update(**request_data)
        return ({"data_updated": request_data}, 201)
    except Exception as e:
        print(e)
        return ({"error": "Update Unsucessful"}, 400)
    return 'ok'

## Delete an ingredient based on the ingredient ID
## ******************************************************************************
#@bp.route('/delete/<ingredient_id>', methods=["DELETE"])
#def create_ingredient(ingredient_id):
    #print("Deleting ingredient.")