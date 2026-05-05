# parent class 
class Animal: 
    def __init__(self, name): 
        self.name = name 
    
    def eat(self): 
        return f"{self.name} is eating"
    
    def sleep(self): 
        return f"{self.name} is sleeping"
    
    def make_sound(self): 
        return f"{self.name} makes a sound"
    

# child class of Animal 
class Dog(Animal): 

    # overriding parent's make_sound with own implementation 
    def make_sound(self): 
        return f"{self.name} is barking"
    

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.make_sound())   # Buddy says woof!