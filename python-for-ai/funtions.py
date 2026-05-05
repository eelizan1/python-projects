# defining 
def greet(): 
    print("Hello, world!")
    print("Welcome to python!")

# calling
greet() 


# functions with logic 
def check_weather(): 
    temp = 25 
    if temp > 30: 
        print("its hot")
    else: 
        print("its cold")

check_weather()

# Global variables 
discount_rate = 0.15 

def apply_discount(price): 
    discount = price * discount_rate
    return price - discount # returns def value 

new_price = apply_discount(100)
print(new_price)

# modifying global variabels via funtion 
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2


# avoid using global 
def add_amounts(current_total, amount): 
    return current_total + amount 

total = 0 
total = add_amounts(total, 10) # total is 10
total = add_amounts(total, 20) # total is 10 + 20 = 30 
print(total) # 30 

# Basic Paramters 
def introduce(name, age): 
    print(f"My name is {name}")
    print(f"I am {age} years old")

introduce("Alice", 25)

# default parameters 
def greet(name, greeting="Hello!"):
    return f"{greeting}, my name is {name}!"


print(greet("Bob")) # will use default greeting param 
print(greet("Alice", "Hey")) # will use passed in greeting param

# Returning Multple Values as a tuple 
def get_min_max(numbers): 
    return min(numbers), max(numbers)

# get both values and assign each to a variable 
minumum, maximum = get_min_max([5, 2, 8, 1, 9])
print(minumum) # 1
print(maximum) # 9

# gets values into a tuple 
min_max_tuple = get_min_max([5, 2, 8, 1, 9])
print(min_max_tuple) # (1, 9)