empty_set = set() 

numbers = {1, 2, 3, 4, 5}
numbers_2 = set([1, 2, 3, 4, 5])

print(numbers)
print(numbers_2)

# list to set 
scores = [85, 90, 85, 92, 90]
score_set = set(scores) # removes dups - 85 and 90 
print(score_set)

# Basic Operations 
colors_set = {
    "red", 
    "blue"
}

# adding items 
colors_set.add("green")

# removing 
colors_set.remove("red")
colors_set.discard("purple") # use discard if you dont want an not found error thrown

if "red" in colors_set: 
    print("Red is available")
else:
    print("Red is not available")


# Common use case - Removing Duplicates 
names_list = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names_set = set(names_list)

print(unique_names_set)