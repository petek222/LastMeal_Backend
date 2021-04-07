from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, Response
)
import json
from datetime import datetime
from lastMeal.models.user import User
from lastMeal.models.ingredient import Ingredient
from bson.objectid import ObjectId

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Blueprint for connection to main process
bp = Blueprint('pantry', __name__, url_prefix='/v1/pantry')

def check_identity(ing, token):
    return (ing.user.username == token)

# Create a new ingredient and associate it with a user
# ******************************************************************************
@bp.route('/create/<username>', methods=["POST"])
@jwt_required()
def create_ingredient(username):
    if (username != get_jwt_identity()):
        return ({"error": "unauthorized"}, 401)
    request_data = request.json
    name = request_data["name"]
    quantity = request_data["quantity"]
    exp_date = request_data["expiration_date"]
    exp_date = datetime.strptime(exp_date, "%Y-%m-%d")
    user = User.objects(username=username)
    if user.first() == None:
        return ({"error": "requested user not found"}, 404)

    try:
        my_ingredient = Ingredient(name=name, quantity=quantity, expiration_date=exp_date, user=user.first())
        my_ingredient.save()
        return ({"name": name, "quantity": quantity, "expiration_date": exp_date}, 201)
    except Exception as e:
        print(e)
        return ({"error": "could not save requested ingredient"}, 400)

# Retrieve all ingredients associated with a user
# ******************************************************************************
@bp.route('/<username>', methods=["GET"])
@jwt_required()
def read_ingredient(username):
    print("Retrieving ingredients.")
    if (username != get_jwt_identity()):
        return ({"error": "unauthorized"}, 401)
    user = User.objects(username=username)
    if user.first() == None:
        return ({"error": "requested user not found"}, 404)
    return ({"ingredients": json.loads(Ingredient.objects(user=user.first()).to_json())}, 200)

# Update an ingredient based on the ingredient ID
# ******************************************************************************
@bp.route('/update/<ingredient_id>', methods=["PUT"])
@jwt_required()
def update_ingredient(ingredient_id):
    print("Updating ingredient.")
    request_data = request.json
    ingredient = Ingredient.objects(id=ObjectId(ingredient_id))
    if ingredient.first() == None:
        return ({"error": "requested ingredient not found"}, 404)
    if not check_identity(ingredient.first(), get_jwt_identity()):
        return ({"error": "Unauthorized"}, 401)

    try:
        ingredient.first().update(**request_data)
        return ({"data_updated": request_data}, 200)
    except Exception as e:
        print(e)
        return ({"error": "Update Unsucessful"}, 400)

# Delete an ingredient based on the ingredient ID for a given user
# ******************************************************************************
@bp.route('/delete/<username>', methods=["DELETE"])
@jwt_required()
def delete_ingredient(username):
    print("Deleting ingredient.")
    ingredient_id = request.args.get("ingredient")
    print(username)
    print(ingredient_id)

    user = User.objects(username=username)
    ingredients = Ingredient.objects.filter(user=user.first())

    if ingredients.first() == None:
        return ({"error": "requested ingredient not found"}, 404)
    if not check_identity(ingredients.first(), get_jwt_identity()):
        return ({"error": "Unauthorized"}, 401)

    try:
        to_be_deleted = []
        for entry in ingredients:
            if entry.name == ingredient_id:
                to_be_deleted.append(entry.id)
        
        ingredients.filter(id__in=to_be_deleted).delete()
        return ({"deleted": ingredient_id}, 200)
    except Exception as e:
        print(e)
        return ({"error": "Deletion unsuccessful"}, 400)
