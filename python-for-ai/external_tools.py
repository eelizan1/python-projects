# Random module 
import random 

number = random.randint(1, 10) # for numbers 
print(number)

fruits = ["banana", "apple", "orange", "grapes", "pears"]
fruit_choice = random.choice(fruits)

print(fruit_choice)


##### 

# Date time 
import datetime 

today = datetime.date.today()
print(today) # 2026-04-20

# Operating System 
import os 

current_dir = os.getcwd()
print(current_dir) # /Users/enricoelizan/Personal Projects/Python Projects/python-for-ai

# JSON Data 
import json 
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

print(json_string) # {"name": "Alice", "age": 30}

from math import *

print(sqrt(4))
