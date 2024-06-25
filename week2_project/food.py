import requests
import json
import pandas as pd
import os

"""
Takes a list of strings of a food items and returns
a list of INTs of the amount of calories otherwise
returns None. Appends the total number of calories at
the end
"""

def getCalories( query ):


    queried = {}
    calories = []
    total = 0

    # for food_item in query:
    #     if food_item in queried:
    #         calories.append(queried[food_item])
    #         continue
        
        
    base_url = "https://food-nutrition-information.p.rapidapi.com/foods/search"

    query = { "query":f"${query}", "pageSize":"1","pageNumber":"1" }

    api_key = os.getenv('RAPIDAPI_KEY')
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "food-nutrition-information.p.rapidapi.com"
    } 
            
    response = requests.get(base_url, headers=headers, params=query)
    print(response.json())
        # data = response.json()
        # print(data)

    #     foodNutrients = data['foods'][0]['foodNutrients']

    #     cals = None
    #     for nutrients in foodNutrients:
    #         if nutrients['nutrientId'] == 1008: # calorie id is 1008
    #             cals = nutrients['value']
    #             total += cals
    #             print(nutrients)
    #             break
        
    #     calories.append(cals)
    #     queried[food_item] = cals

    # calories.append(total)
    # return calories


print(getCalories(["Apple", "Carrots", "Oranges"]))