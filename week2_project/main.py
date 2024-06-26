import os 
import openai
import sqlite3
from openai import OpenAI
from tabulate import tabulate
from prompt import prompt
from food import getCalories
from colorama import Fore, Back, Style

# Set environment variables
my_api_key = os.getenv('OPENAI_KEY')
openai.api_key = my_api_key

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key=my_api_key,
)

def get_user_info(): 
    print("Please enter your information in the following questions:\n")
    user_input1 = input("What is your name? ")
    user_input2 = input("How old are you? ")
    user_input3 = input("Enter your current weight? (in lbs or kg): ")
    user_input4 = input("Enter your goal weight? (in lbs or kg): ")
    user_input5 = input("Provide an explaination on why you want to live a better and healthier lifestyle: \n")

    return {
        "name": user_input1,
        "age": user_input2,
        "weight": user_input3,
        "goal_weight": user_input4,
        "reason": user_input5
    }

#User data for the database
def input_userdata_into_db(user_data_for_db):
    #connects to db
    engine = sqlite3.connect('userdata.db')
    cursor = engine.cursor()

    # creates db table
    create_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            weight INTEGER,
            goal_weight INTEGER,
            reason TEXT
        );
    '''

    cursor.execute(create_table)

    #insert user data in db table
    insert_user_into_table = '''
    INSERT INTO users (name, age, weight, goal_weight,reason)
    VALUES(:name,:age,:weight,:goal_weight,:reason)
    '''

    cursor.execute(insert_user_into_table, user_data_for_db)
    engine.commit()
    engine.close()

#print db 
def print_database():
    engine = sqlite3.connect('userdata.db')
    cursor = engine.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    header= ["ID","NAME","AGE","WEIGHT","Goal WEIGHT","REASON"]
    print("User Data:\n")
    print(tabulate(rows,headers=header,tablefmt="grid"))
    engine.close()


def call_openai(user_message):
    # Specify the model to use and the messages to send
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{prompt}"},
        {"role": "user", "content": user_message}
    ]
)
    return completion.choices[0].message.content

def get_username(name):
    engine = sqlite3.connect('userdata.db')
    cursor = engine.cursor()

    cursor.execute("SELECT * FROM users WHERE name=?", (name,))
    user = cursor.fetchone()

    engine.close()
    return user
            

# parses the meals and calculates calories
def parse_options(options):
    response = ""

    for option in options:
        divider = option.find('|')
        name = option[2:divider-1]
        ingredients = (option[divider + 2:]).split(', ')
        response += f"- {name} ({Fore.CYAN}{getCalories(ingredients)[-1]}{Style.RESET_ALL} cals) | {' '.join(ingredients)}\n"
    
    return f"{response}\n"

# parses the chatgpt response
def parse_response(message):
    lines = message.split('\n')
    currMeal = 0
    response = """\nRecommended Meals with estimated calories:\n"""

    temp = []
    for line in lines:
        temp.append(line.strip())
    temp.append('')
    lines = temp

    for _ in range(3):
        for line in lines:
            line = line.strip()
            if line in ['Breakfast:', 'Lunch:', 'Dinner:']:
                response += f"{Fore.GREEN}{line.strip()}{Style.RESET_ALL}\n"
                curr = lines[currMeal+1:]
                end = curr.index('')
                response += parse_options(curr[:end])
                lines = curr[end+1:]
                currMeal = 0
                break
            currMeal += 1
    
    return response

def main(): 
    print("Welcome to A.I. Health Advisor!\n")
    user_starter = input("Have you used this application before? Please enter 'yes' or 'no': ").strip().lower()

    if user_starter == 'yes':
        user_name = input("Please enter your name that you have perivously entered: ").strip()
        user = get_username(user_name)

        if user: 
            print(f"Welcome Back {user[1]}!")
            print("Here is your current information that we have from you: \n")
            header= ["ID","NAME","AGE","WEIGHT","Goal WEIGHT","REASON"]
            user_data = [
                ["NAME",user[1]],
                ["AGE",user[2]],
                ["WEIGHT", user[3]],
                ["GOAL WEIGHT", user[4]],
                ["REASON",user[5]]
            ]
            print(tabulate(user_data, headers=header, tablefmt="grid"))

            more_recom = input("Would you like to get more health recommendations? Please enter(yes/no): \n")
            if more_recom == "yes": 
                user_message = (
                    f"My name is {user[1]}, I am {user[3]} years old. " 
                    f"I currently weigh {user[3]} and my goal weight is {user[4]}. " 
                    f"I want to live a better and healthier lifestyle because {user[5]}. "
                )
                print(parse_response(call_openai(user_message)))
            else: 
                print("Thank you for visiting!")
        else:
            print("Sorry! User is not in database")
    else:
        user_data_for_db = get_user_info()

        user_message = (
            f"My name is {user_data_for_db['name']}, I am {user_data_for_db['age']} years old. " 
            f"I currently weigh {user_data_for_db['weight']} and my goal weight is {user_data_for_db['goal_weight']}. " 
            f"I want to live a better and healthier lifestyle because {user_data_for_db['reason']}. "
        )
        print(parse_response(call_openai(user_message)))

        input_userdata_into_db(user_data_for_db)
        print_database()

# def test():
#     msg = """
# Breakfast:
# - Avocado Toast | whole grain bread, avocado, cherry tomatoes
# - Greek Yogurt Parfait | Greek yogurt, mixed berries, granola
# - Smoothie Bowl | spinach, banana, almond milk, chia seeds

# Lunch:
# - Grilled Chicken Salad | grilled chicken breast, mixed greens, cherry tomatoes, cucumbers, balsamic vinaigrette
# - Quinoa Veggie Bowl | quinoa, roasted vegetables, chickpeas, tahini dressing
# - Tuna Wrap | whole grain wrap, tuna, spinach, avocado, lemon juice

# Dinner:
# - Baked Salmon | salmon fillet, asparagus, lemon, olive oil
# - Stir-Fry | mixed vegetables, tofu or chicken, soy sauce, brown rice
# - Stuffed Bell Peppers | bell peppers, ground turkey, quinoa, black beans, diced tomatoes
# """
    # msg = """Breakfast:
    # - Berry Smoothie | mixed berries, banana, spinach
    # - Avocado Toast | whole grain bread, avocado, cherry tomatoes

    # Lunch:
    # - Quinoa Salad | quinoa, mixed vegetables, chickpeas
    # - Grilled Chicken Salad | mixed greens, grilled chicken, cucumbers

    # Dinner:
    # - Baked Salmon | salmon fillet, asparagus, quinoa
    # - Stir-Fried Tofu and Vegetables | tofu, bell peppers, broccoli
    # """
    # parse_response(msg)

if __name__ == "__main__":
    main()
    # test()

















'''
Sample response from API with the user message:
Welcome to A.I. Health Advisor!

Please enter your information in the following questions:

What is your name? Charlize
How old are you? 20
Enter your current weight? (in lbs or kg)180
Enter your goal weight? (in lbs or kg)165
Provide an explaination on why you want to live a better and healthier lifestyle: 
I would get better at eating healthier foods as i life to eat junk food and struggle to healthy foods. I also dont like to work out alot and what to be more active.
Hi Charlize! It's great to hear that you're motivated to live a healthier lifestyle. Making small, sustainable changes to your diet and activity level can have a big impact on your overall well-being. Here are some recommendations to help you achieve your goals:

1. **Healthy Eating Habits**:
   - Start by incorporating more fruits and vegetables into your meals. Aim to fill half your plate with fruits and veggies at each meal.
   - Choose whole grains like brown rice, quinoa, and whole wheat bread over refined grains.
   - Opt for lean protein sources such as chicken, fish, beans, and tofu.
   - Limit your intake of processed foods, sugary drinks, and high-fat foods.
   - Practice mindful eating by paying attention to your hunger cues and eating slowly.

2. **Healthy Snack Ideas**:
   - Greek yogurt with fresh berries and a sprinkle of nuts
   - Hummus with veggie sticks
   - Apple slices with almond butter
   - Air-popped popcorn
   - Homemade trail mix with nuts, seeds, and dried fruit

3. **Physical Activity**:
   - Find activities you enjoy, whether it's walking, dancing, swimming, or yoga. Aim for at least 150 minutes of moderate-intensity exercise per week.
   - Take short breaks throughout the day to move around and stretch. Even a 10-minute walk can boost your energy levels.
   - Consider incorporating strength training exercises to build muscle and improve your metabolism.

4. **Meal Planning**:
   - Plan your meals and snacks ahead of time to ensure you have healthy options readily available.
   - Prepare nutritious meals in advance to avoid the temptation of convenient but unhealthy fast food options.

Remember, it's important to focus on progress, not perfection. Making small changes consistently over time will help you develop healthier habits. If you need further guidance or support, consider consulting a nutritionist or health coach. Good luck on your journey to a healthier lifestyle, Charlize!


Breakfast:
- Option 1: Greek Yogurt with Berries and Honey (250 calories)
- Option 2: Oatmeal with Fresh Fruits and Nuts (300 calories)
- Option 3: Scrambled Eggs with Spinach and Whole Wheat Toast (280 calories)

Lunch:
- Option 1: Grilled Chicken Salad with Mixed Vegetables and Vinaigrette (350 calories)
- Option 2: Quinoa Bowl with Roasted Vegetables and Chickpeas (400 calories)
- Option 3: Turkey and Avocado Wrap with a Side Salad (380 calories)

Dinner:
- Option 1: Baked Salmon with Steamed Broccoli and Brown Rice (450 calories)
- Option 2: Stir-Fried Tofu with Mixed Vegetables and Cauliflower Rice (400 calories)
- Option 3: Grilled Shrimp Tacos with Cabbage Slaw and Lime Crema (420 calories)



'''


