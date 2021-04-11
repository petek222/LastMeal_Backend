# API for pulling and computing suggested expiration dates

# This is how dates are being sent from the frontend to the server
# 2021-04-30
# string

# This is how dates are being recieved from the server by the frontend (we think)
# Object {
#   "$date": 1619481600000,
# }

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

# Blueprint for connection to main process
bp = Blueprint('exp', __name__, url_prefix='/v1/exp')

# Request Format:
# /v1/photos?ingredient=apple redirects us to /v1/photos/?ingredient=apple
@bp.route('', methods=['GET'])
@jwt_required()
def fetch_expiration():
    ingredient = request.args.get("ingredient")

    if ingredient is None:
        return ({"error": "no ingredient was passed"}, 400)

    try:
        pass # Make request to expiration database
    
    except Exception as e:
        print(e)
        return ({"error": "Image could not be retrieved"}, 400)


# We want to parse the date strings and return them in the format needed
# by the frontend for parsing
# 
# IMP NOTE: I am opting for a conservative-estimate approach to the expiration
# data dataset. That is, If a given date supplied a range, I will be selecting
# and parsing based off the minimum value from that range (ie. 2-4 weeks => 2 weeks)
#
# Input Data Formats:
# 2 days/2 weeks/2 months/2 years
# 2-4 days/2-4 weeks/2-4 months/2-4 years
#
# Output Data Formats (calculated from current Date)
# 2021-04-30 (yyyy-mm-dd)
# 1619481600000 (seconds since epoch)
def parse_dates(date_string):
    if date_string == '':
        return None

    # Parse the string into day and time
    date_parsed = date_string.split(' ')

    number_string = date_parsed[0]
    duration = date_parsed[1]
    if '-' in number_string:
        my_split = number_string.split('-')
        number_string = my_split[0]
    
    number = int(number_string)
    today = dt.date.today()

    if duration == 'days' or duration == 'day':
        expiration = today + dt.timedelta(days=number)
    elif duration == 'weeks' or duration == 'week':
        expiration = today + dt.timedelta(weeks=number)
    elif duration == 'months' or duration == 'month':
        week_count = 4 * number
        expiration = today + dt.timedelta(weeks=week_count)
    elif duration == 'years' or duration == 'year':
        week_count = 52 * number
        expiration = today + dt.timedelta(weeks=week_count)
    elif duration == 'hours' or duration == 'hour':
        expiration = today + dt.timedelta(hours=number)
    

    # Value returned as: 2023-04-01
    return expiration
