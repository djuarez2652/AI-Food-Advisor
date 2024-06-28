# Week 2: Project

## Set Up Instructions 

Be sure to have Python 3.6 installed onto your computer. 

1. First install the following libraries into your terminal: 

```bash
pip install openai sqlite3 tabulate colorama requests pandas
```

### Enviroment Variables

You need to set up the API keys in your system as environment variables. Which
can be set into your shell profile (.bashrc, .zshrc):
For Both the Openai and Rapid’s Food Nutrition Information API:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
export RAPIDAPI_KEY='your_rapid_api_key_here'
```
## How to run the code 
1. Clone the repository or download the script.
2. Ensure you have the necessary libraries installed (see Setup Instructions).
3. Set the OPENAI_API_KEY and RAPIDAPI_KEY as environment variable.

4. Run this command into your terminal: 
```bash
python3 main.py
```


## Project Overview 
1. Name of Project: A.I. Food Advisor

2. What problem are you solving?
Our project will help others by giving people advice on eating healthy meals and 
activities. This will be able to help our users to live a healthy lifestyle. 

3. Who / What does the project interface with?

a. people? Anyone that needs advice to live a healthy lifestyle


b. other systems? (APIs)
OPENAI API chatgpt 3.5 turbo
Rapid’s Food Nutrition Information API

c. Hardware?
Anything that can run python


2. What are the inputs?
Name, age, weight, weight goal, What is your goal and why? (stored in database)

3. What are the outputs?
Chatgpt advice(saved in database)


4. List 5 steps to go from input -> output
1. prompt user for input data
2. User inputs data/saves in database
3. call on api for response
4. Chatgpt api generates a response/ saves in database
5. prints output


5. What’s the biggest risk?
User can easily get leaked from the database if no protected correctly. Chatgpt api
could also give out misinformation on the healthy advice for the user as chatgpt is not always accurate.

6. How will you know you’re successful?
We know that the project is successful when we are able to help people live a healthy lifestyle. 
