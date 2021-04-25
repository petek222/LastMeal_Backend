from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, Response
)
import json
from lastMeal.models.user import User
from lastMeal.models.favorite import Favorite
from bson.objectid import ObjectId

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import requests

bp = Blueprint('favorite', __name__, url_prefix='/v1/favorite')

@bp.route('/create/<username>', methods=['POST'])
#@jwt_required()
def create_favorite(username):
#    if (username != get_jwt_identity()):
#        return ({"error": "unauthorized"}, 401)

    request_recv = request.json
    user = User.objects(username=username).first()
    if user == None:
        return ({"error": "requested user not found"}, 404)
    request_arr = request_recv["recipeArray"]
    for request_data in request_arr:
        recipe_id = request_data["recipe_id"]
        if Favorite.objects(recipe_id=recipe_id).first() != None:
            return ({"error": "can't favorite a recipe twice"}, 400)
        recipe_name = request_data["recipe_name"]
        picture = request_data["picture"]

        try:
            my_favorite = Favorite(user=user, recipe_id=recipe_id, recipe_name=recipe_name, picture=picture)
            my_favorite.save()
        except Exception as e:
            print(e)
            return ({"error": "could not favorite requested recipe"}, 400)
    return ({"success": "{} recipe(s) favorited".format(len(request_arr))}, 201)

@bp.route('/delete/<username>', methods=["DELETE"])
#@jwt_required()
def delete_favorite(username):
#    if (username != get_jwt_identity()):
#        return ({"error": "unauthorized"}, 401)

    recipe_id = request.args.get("recipe_id")

    user = User.objects(username=username).first()
    if user == None:
        return ({"error": "requested user not found"}, 404)

    try:
        Favorite.objects(user=user, recipe_id=recipe_id).delete()
        return ({"deleted": recipe_id}, 200)
    except Exception as e:
        print(e)
        return ({"error": "Deletion unsuccessful"}, 400)

@bp.route('/<username>', methods=["GET"])
#@jwt_required()
def read_favorite(username):
#    if (username != get_jwt_identity()):
#        return ({"error": "unauthorized"}, 401)
    user = User.objects(username=username).first()
    if user == None:
        return ({"error": "requested user not found"}, 404)
    favorites = Favorite.objects(user=user)
    info_list = []
    for item in favorites:
        info_list.append({"picture": item.picture, "recipe_id": int(item.recipe_id), "recipe_name": item.recipe_name})
    return ({"favorites": info_list}, 200)
