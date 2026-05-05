'''
Lists 
''' 

my_list = []
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

# mixed type lists 
mixed = ["hello", 42, True, 3.14] # Different types OK!

# Slicing 
names = ["Tom", "Jerry", "Mike", "Bob"]

print(names[0:2]) # start at index 0, stop before index 2 -> "Tom" "Jerry"
print(names[1:]) # start at index 1 and go until the end -> "Jerry", "Mike", "Bob"
print(names[:]) # full copy of list "Tom", "Jerry", "Mike", "Bob"

print(names[-1]) # get last item -> "Bob"
print(names[-2]) # get 2nd to last -> "Mike"
print(names[1:-2]) # start at index 1 until second up until last -> "Jerry",


# Mutating Lists 
colors = ["red", "blue", "green", "yellow", "orange", "black"]

colors[0] = "grey" # change first item 
colors.append("pink") # add new item 
colors.insert(1, "purple") # insert at index 1 
colors.remove("black") # remove value 
last_color = colors.pop() # remove and return last 
del colors[3] # remove by index 

print(colors) # ['grey', 'purple', 'blue', 'yellow', 'orange']

# Common List Methods 
numbers = [3, 1, 4, 1, 5, 9]

print(len(numbers)) # length of the list -> 6
print(numbers.count(1)) # counts the occurrence of an element -> 2 
print(numbers.index(4)) # finds index of element -> 2 

# sorting of list 
numbers.sort() # sort in place 
print(numbers)

numbers.reverse() # reverse list 
print(numbers)

# copy 
new_list = numbers.copy() 
print(new_list)

# Checking if an item exists 
fruits = ["apple", "banana", "orange"]
if "apple" in fruits: 
    print("Found apple!")

# check if list is empty 
if fruits: 
    print("List has fruits")
else: 
    print("List is empty")


# Wrong - changes list size during loop
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 2:
        numbers.remove(num)  # Dangerous!

print(numbers)