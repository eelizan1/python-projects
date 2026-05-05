# Tuples 
empty = () 
coord = (3, 5)
colors = ("red", "green", "blue")
single_tuple = (1,)

#Accessing  
print(coord[0]) # -> 3
print(coord[1]) # -> 5
print(colors[-1]) # last item -> blue

point = (7, 9)
x, y = point # x = 7, y = 9
print(x, y)
# swap 
x, y = y, x
print(x, y)

point[0] = 4

# multi assignment 
a, b, c = 1, 2, 3 # same as (1, 2, 3)
print(b) # -> 2 