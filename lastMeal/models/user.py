from mongoengine import *
# from mongoengine import signals
from Crypto.Hash import SHA256
import datetime
import calendar  
import re
from random import random

# connect to user db: Check path as needed
connect('user')

def make_salt():
    cur_date = calendar.timegm(time.gmtime())
    return round(cur_date * random()) + ""

# Check
def encrypt_password(salt, password):
    hash = SHA256.new(salt)
    hash.update(password)
    return hash.hexdigest() # Check if this is what should be returned from encryption
    
class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True)
    username = StringField(required=True)
    hash = StringField(required=True)
    salt = StringField(required=True)
    pantry = ObjectIdField(db_field='pantry') # Check syntax here; same as 'ref' for mongoose?

    def validate_username(self, username):
        if (username != "" and len(username) > 4 and len(username) < 20):
            return True
        else:
            return False
    
    def validate_email(self, email):
        if (re.match(r"[^@]+@[^@]+\.[^@]+", email)):
            return True
        else:
            return False
    
    def set_password(self, password):
        self.user_salt = make_salt()
        self.user_hash = encrypt_password(self.user_salt, password)

    def authenticate_user(self, user_input):
        return (encrypt_password(self.user_salt, user_input) == self.user_hash)

    @classmethod
    def pre_save(self, cls, sender, document, **kwargs):
        self.first_name = re.sub('/<(?:.|\n)*?>/gm', "", self.first_name)
        self.last_name = re.sub('/<(?:.|\n)*?>/gm', "", self.last_name)
        # Add any other pre-save validation that we want here

# # signals pre_save in mongoengine calls the pre_save function above upon saving a document
# signals.pre_save.connect(User.pre_save, sender=User)


