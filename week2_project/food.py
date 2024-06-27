import requests
import sqlite3
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

    engine = sqlite3.connect("food.db")
    cursor = engine.cursor()
    create_table = """
        CREATE TABLE IF NOT EXISTS food (
            name VARCHAR(255) NOT NULL,
            calories INT NOT NULL,
            PRIMARY KEY(name)
        );
    """
    cursor.execute(create_table)
    engine.commit()


    lst_of_cals = []
    total = 0

    for food in lst_of_foods:

        db_query = "SELECT calories FROM food WHERE name = ?"
        cursor.execute(db_query, (food.lower(),))
        result = cursor.fetchone()

        if result:
            total += result[0]
            lst_of_cals.append(result[0])
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
                if cals > 400: # some serving sizes are too big
                    cals //= 5
                sql_insert = "INSERT INTO food (name, calories) VALUES (?,?)"
                cursor.execute(sql_insert, (food.lower(),cals))
                engine.commit()
                total += cals
                break

        lst_of_cals.append(cals)
    
    lst_of_cals.append(total)

    engine.commit()
    engine.close()

    return lst_of_cals