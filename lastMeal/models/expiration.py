from mongoengine import *

connect('lastMeal')

class Expiration(Document):
    ingredient_name = StringField(max_length=100)
    pantry_expiration = StringField(max_length=100)
    freezer_expiration = StringField(max_length=100)
    fridge_expiration = StringField(max_length=100)
