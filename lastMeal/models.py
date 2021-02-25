from mongoengine import *

connect('tumblelog')

class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
