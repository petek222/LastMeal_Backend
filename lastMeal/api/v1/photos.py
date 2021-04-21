import functools
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import requests
import os

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

bp = Blueprint('photos', __name__, url_prefix='/v1/photos')

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

#set the route to nothing, because if we use a trailing slash, making a GET request to
# /v1/photos?ingredient=apple redirects us to /v1/photos/?ingredient=apple
@bp.route('', methods=['GET'])
@jwt_required()
def register_user():
    ingredient = request.args.get("ingredient")

    if ingredient is None:
        return ({"error": "no ingredient was passed"}, 400)

    base_url = "https://api.pexels.com/v1/search"
    payload = {"query": ingredient, "per_page": 1}
    headers = {"Authorization": PEXELS_API_KEY}
    r = requests.get(base_url, params=payload, headers=headers)
    try:
        resp = r.json()
        image_url = resp["photos"][0]["src"]["small"]
        return ({"src": image_url}, 200)
    except Exception as e:
        print(e)
        return ({"error": "Image could not be retrieved"}, 400)
