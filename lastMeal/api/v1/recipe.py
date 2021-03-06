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
import datetime as dt
import requests

# Blueprint for connection to main process
bp = Blueprint('recipes', __name__, url_prefix='/v1/recipes')

api_key = ''

# Basic Recipe Request Based on Ingredients
@bp.route('', methods=['POST'])
#@jwt_required()
def fetch_recipes():
    request_data = request.json

    ingredientList = request_data['ingredients']

    if ingredientList is None:
        return ({"error": "no ingredients were passed"}, 400)

    try:
        body = {
            'ignorePantry': True,
            'ingredients': ingredientList,
            'limitLicense': False,
            'number': 10,
            'ranking': 1,
            'apiKey': api_key
        }

        endpoint = "https://api.spoonacular.com/recipes/findByIngredients"

        headers={
            "X-Mashape-Key": api_key,
            "X-Mashape-Host": "mashape host"
        }
        
        r = requests.get(endpoint, params=body, headers=headers)
        recipe_results = r.json()

        print("TESTING SPOONACULAR RECIPE API")
        print(recipe_results)

        new_data = {}

        new_data['recipe_data'] = recipe_results
        return ({'recipe_data': new_data}, 200)
    
    except Exception as e:
        print(e)
        return ({"error": "Error in recipe fetch request"}, 400)

@bp.route('/<recipe_id>', methods=['GET'])
# @jwt_required()
def fetch_recipe_info(recipe_id):

    if recipe_id is None:
        return ({"error": "No recipe ID was passed"}, 400)
    
    try:
        endpoint = "https://api.spoonacular.com/recipes/" + recipe_id + "/information"

        body = {
            'apiKey': api_key
        }

        headers={
            "X-Mashape-Key": api_key,
            "X-Mashape-Host": "mashape host"
        }

        r = requests.get(endpoint, params=body, headers=headers)
        recipe_info_results = r.json()

        new_data = {}

        new_data['recipe_info'] = recipe_info_results
        return ({'recipe_id': recipe_id, 'recipe_data': new_data}, 200)

    except Exception as e:
        print(e)
        return ({"error: Error in recipe info fetch request"}, 400)

@bp.route('save/<recipe_id>', methods=['GET'])
# @jwt_required()
def user_favorite_recipe(recipe_id):
    pass 
    # placeholder for user-favorited recipes; make sure that data is parsed before saving, and that the recipe ID is saved
    # Upon clicking on the UI, we can redirect to the same recipeInfo page that we do for the pantry/recipe page


# Space here for any additional parsing we want to do in the backend
