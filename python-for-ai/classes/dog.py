class Dog:
    # the __init__ runs when you create a new object
    # this is the "setup" method
    def __init__(self, name, breed):
        # "self" refers to the current object - its how an object keeps track of its own data
        self.name = name
        self.breed = breed

# Create dog object - using positional arguments
dog1 = Dog("Buddy", "Husky")
dog2 = Dog("Max", "Beagle")

# Using named argument (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)
print(dog3.name, dog3.breed)
