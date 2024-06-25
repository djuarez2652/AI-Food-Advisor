import requests
import json
import pandas as pd
import os

"""
Takes a list of strings of food items and returns
a list of INTs of their respective amount of calories 
for each item; if not found in API it returns None. 
Appends the total number of calories at the end
"""

def getCalories( lst_of_foods ):

    lst_of_cals = []
    cache = {}
    total = 0

    for food in lst_of_foods:
        if food in cache:
            total += cache[food]
            lst_of_cals.append(cache[food])
            continue

        url = "https://food-nutrition-information.p.rapidapi.com/foods/search"

        query = { 
                    "query": f"{food}",
                    "pageSize": "1",
                    "pageNumber": "1"
                }

        RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

        headers = {
                    "x-rapidapi-key": RAPIDAPI_KEY,
                    "x-rapidapi-host": "food-nutrition-information.p.rapidapi.com"
                }

        response = requests.get(url, headers=headers, params=query)
        data = response.json()
        try:
            foodNutrients = data['foods'][0]['foodNutrients']
        except:
            lst_of_cals.append(None)
            continue

        cals = None
        for nutrients in foodNutrients:
            if nutrients['nutrientId'] == 1008: # cal id is 1008
                cals = nutrients['value']
                cache[food] = cals
                total += cals
                break

        lst_of_cals.append(cals)
    
    lst_of_cals.append(total)

    return lst_of_cals


print(getCalories(["Apple", "Apple", "random"]))