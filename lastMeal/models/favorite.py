from mongoengine import *
from mongoengine.errors import ValidationError
from lastMeal.models.user import User

connect('lastMeal')

class Favorite(Document):
    recipe_id = DecimalField(required=True, unique=True)
    recipe_name = StringField(max_length=100, required=True)
    picture = StringField(max_length=100, required=True)
    user = ReferenceField(User, required=True)
