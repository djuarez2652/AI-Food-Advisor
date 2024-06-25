import requests
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

    print(response.json())

getCalories("Cheese")