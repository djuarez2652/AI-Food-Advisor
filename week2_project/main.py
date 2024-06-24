import os 
import openai
from openai import OpenAI

# Set environment variables
my_api_key = os.getenv('OPENAI_KEY')

openai.api_key = my_api_key

from openai import OpenAI

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key=my_api_key,
)
print("Welcome to A.I. Health Advisor!\n")
print("Please enter your information in the following questions:\n")
user_input1 = input("What is your name? ")
user_input2 = input("How old are you? ")
user_input3 = input("Enter your current weight? (in lbs or kg)")
user_input4 = input("Enter your goal weight? (in lbs or kg)")
user_input5 = input("Provide an explaination on why you want to live a better and healthier lifestyle: \n")

#User message
user_message = (
    f"My name is {user_input1}, I am {user_input2} years old. " 
    f"I currently weigh {user_input3} and my goal weight is {user_input4}. " 
    f"I want to live a better and healthier lifestyle because {user_input5}. "
)


# Specify the model to use and the messages to send
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a health advisor and are giving healthy food recommendations"},
        {"role": "user", "content": user_message}
    ]
)
print(completion.choices[0].message.content) 

#User data for the database
user_data_for_db= {
    "name": user_input1
    "age": user_input2
    "weight": user_input3 
    "goal_weight": user_input4
    "reason": user_input5
}

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
'''