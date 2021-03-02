from mongoengine import *
from mongoengine.errors import ValidationError
from Crypto.Hash import SHA256
import datetime
import calendar
import time
import re
from random import random

# connect to user db: Check path as needed
connect('lastMeal')

def make_salt():
    cur_date = calendar.timegm(time.gmtime())
    return str(round(cur_date * random()))

# Check
def encrypt_password(salt, password):
    hash = SHA256.new(salt.encode('utf-8'))
    hash.update(password.encode('utf-8'))
    return hash.hexdigest() # Check if this is what should be returned from encryption

def validate_username(username):
    if (username == "" or len(username) < 6 or len(username) > 19):
        raise ValidationError("Invalid username")

def validate_email(email):
    if not (re.match(r"[^@]+@[^@]+\.[^@]+", email)):
        raise ValidationError("Invalid email")

class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True, validation=validate_email)
    username = StringField(required=True, validation=validate_username)
    hash = StringField(required=True)
    salt = StringField(required=True)
    pantry = ObjectIdField(db_field='pantry') # Check syntax here; same as 'ref' for mongoose?

    def set_password(self, password):
        if (len(password) < 8 or len(password) > 19):
            raise ValidationError("Invalid password")
        self.salt = make_salt()
        self.hash = encrypt_password(self.salt, password)

    def authenticate_user(self, user_input):
        return (encrypt_password(self.salt, user_input) == self.hash)

    @classmethod
    def pre_save(self, cls, sender, document, **kwargs):
        self.first_name = re.sub('/<(?:.|\n)*?>/gm', "", self.first_name)
        self.last_name = re.sub('/<(?:.|\n)*?>/gm', "", self.last_name)
        # Add any other pre-save validation that we want here

# # signals pre_save in mongoengine calls the pre_save function above upon saving a document
# signals.pre_save.connect(User.pre_save, sender=User)
