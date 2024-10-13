# Class: A blueprint for creating objects (a logical entity). 
# It defines a set of attributes (data) and methods (functions) that operate on the data.
# Object: An instance of a class, representing a real-world entity. 
# It is created from a class and holds actual data.


# Class Attributes and Methods
# Attributes (also called properties or fields): 
# Variables that belong to a class and represent the state of an object.
# Methods: Functions that belong to a class. 
# They define the behavior of the object.

# Types of Attributes:
# Instance attributes: Specific to each object and 
# defined inside the __init__() method.
# Class attributes: Shared by all objects of a class, 
# defined outside __init__().


# The __init__() Constructor
# The __init__() method is a special method in Python classes. It is automatically called when a new object is created and is used to initialize the object's attributes.



class Car:

    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Accelerating... ... ...")
    
    def stop(self):
        print("Stop... ... ...")

