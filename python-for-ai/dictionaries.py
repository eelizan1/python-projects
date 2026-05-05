
# empty 
my_dict = {}

# creating with values 
alice = {
    "name" : "Alice", 
    "age" : 30, 
    "city" : "New York"
}

# Accessing values 
person = {
    "name": "Alice", 
    "age": 30, 
    "city": "New York"
}

# get values by key 
print(person["name"]) # get value of name -> Alice 
print(person["age"]) # get value of age -> 30  

# safer way to get values from key
print(person.get("city")) # using get() to get value by key
print(person.get("name"))

# if doesnt exist then return a default value - DOESNT ADD TO DICT 
print(person.get("job", "Engineer")) # -> Engineer 

# Changing or Updating 
person["email"] = "alice@gmail.com" # adds new key value 
person["age"] = 32 # updates age 

# remove items 
del person["email"] # removes email 
age = person.pop("age") # removes and returns value of key 
person.remove() # clears all items from map

# Dictionary Methods 
print(person.keys())

# print keys 
for key in person.keys(): 
    print(key)

# print values 
for value in person.values(): 
    print(value)

# print entries 
for item in person.items(): 
    print(item)

# Check if key exists 
if "name" in person: 
    print(person.get("name"))

# updating multiple values 
person.update({"age" : 34, "city" : "Atlanta"})
print(person.items())


# nested Dictionaries 
# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}


print(students.get("alice").get("grade")) # gets alice's grade => A