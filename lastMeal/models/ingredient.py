from mongoengine import *
from mongoengine.errors import ValidationError
from lastMeal.models.user import User

connect('lastMeal')

class Ingredient(Document):
    name = StringField(max_length=50)
    expiration_date = DateTimeField()
    quantity = DecimalField(required=True)
    #units = StringField(required=True)
    user = ReferenceField(User, required=True)