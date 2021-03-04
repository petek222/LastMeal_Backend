from mongoengine import *
from mongoengine.errors import ValidationError

connect('lastMeal')

class Ingredient(Document):
    name = StringField(max_length=50)
    expiration_date = DateTimeField(required=True)
    quantity = DecimalField(required=True)
    #units = StringField(required=True)
    user = ObjectIdField(db_field='user')