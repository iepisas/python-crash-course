class Dog:
    """A simple attempt to model a god."""
    
    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

'''
The __init__() method
A function that's part of a class is a method
Everything you learned about functions applies to methods as well
The self parameter is required in the method definition
and it must come first before the other parameters
'''

my_dog = Dog('willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#To access the attributes of an instance,you use dot notation.
#To call a method,give the name of the instance and the method you want to call,separated by a dot.

my_dog.sit()
my_dog.roll_over()

#You can create as many instances from a class as you need

your_dog = Dog('Lucy',3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()