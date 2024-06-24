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

# Specify the model to use and the messages to send
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a health advisor and are giving healthy food recommendations"},
        {"role": "user", "content": "i want to lose 20 pounds and currently weight 180. What meal plans do you recommend that I try?"}
    ]
)
print(completion.choices[0].message.content) 

'''
print("Welcome to A.I. Health Advisor!\n")
print("Please enter your information in the following questions:\n")
user_input1 = input("What is your name? ")
user_input2 = input("How old are you? ")
user_input3 = input("Enter your current weight? (in lbs or kg)")
user_input4 = input("Enter your goal weight? (in lbs or kg)")
user_input5 = input("Provide an explaination on why you want to live a better and healthier lifestyle: \n")
'''


