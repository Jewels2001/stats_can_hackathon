"""
This module queries the recipe API
currently using API Ninja's recipe API

"""

import os
import requests
import json
from dotenv import load_dotenv

# Retrieve the env variables - contains API key!
load_dotenv()
API_KEY = os.environ["JULIE_APININJAS_API_KEY"]


query = "spaghetti bolognese"
api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)

all_ingredient_list = ""
ingredients = set()
instructions = []
servings = []

response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    for option in response.json():
        all_ingredient_list = all_ingredient_list + option['ingredients']
        servings.append(option['servings'])
        instructions.append(option['instructions'])
else:
    print("Error:", response.status_code, response.text)
    
    
if all_ingredient_list:
    all_str = all_ingredient_list.split("|")
    for item in all_str:
        ingredients.add(item)


print(ingredients)
    
