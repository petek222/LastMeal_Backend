import sys
sys.path.insert(0, '/home/ubuntu/last_meal')

import json
from lastMeal.api.v1.exp import parse_dates
from lastMeal.models.expiration import Expiration

f = open('./expirationData.json', 'r')
data = json.load(f)
for elem in data:
    my_expiration = Expiration(ingredient_name=elem['ingredient_name'], pantry_expiration=elem['pantry_expiration'], freezer_expiration=elem['freezer_expiration'], fridge_expiration=elem['fridge_expiration'])
    my_expiration.save()
f.close()
