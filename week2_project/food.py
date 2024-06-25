import requests
import json
import pandas as pd
import os


def getCalories( query ):
    base_url = "https://food-nutrition-information.p.rapidapi.com/foods/search"

    query = { "query":f"${query}", "pageSize":"1","pageNumber":"1" }

    api_key = os.getenv('RAPIDAPI_KEY')
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "food-nutrition-information.p.rapidapi.com"
    } 
        
    response = requests.get(base_url, headers=headers, params=query)
    data = response.json()
    foodNutrients = data['foods'][0]['foodNutrients']

    foundEnergy = False
    cals = None
    for nutrients in foodNutrients:
        if nutrients['nutrientId'] == 1008:
            foundEnergy = True
            cals = nutrients['value']
            print(nutrients)
            break
    return cals
    # json_data = json.loads(response)

    # df = pd.DataFrame.from_dict(data)
    

    # print(pd.DataFrame.from_dict(data=response.json()))
    # data = json.loads(response.json())

    # food = data[foods][0]
    # print(food)

print(getCalories("Cheese"))