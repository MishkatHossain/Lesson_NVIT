# Abstraction is one of the four fundamental concepts of Object-Oriented Programming (OOP). 
# It is the process of hiding complex implementation details and showing only the necessary features of an object.
# Example: TV remote. Don't need to understand how it work. Just the button interface
# Example: Car. Don't need to understand how it work. Just the steering, gear, break

# Abstract Classes: These are classes that cannot be instantiated and are meant to be subclasses. 
# They may contain abstract methods (methods that have no implementation).



from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):
    @abstractmethod
    def revenue(self):
        return 500

# Subclass implementing the abstract method
class Cow(Animal):
    def revenue(self):
        return 100000

class Goat(Animal):
    def revenue(self):
        return 18000

# Using the classes
def animal_revenue(animal: Animal):
    print(animal.revenue())

# Create instances of Dog and Cat
cowA = Cow()
goatA = Goat()

animal_revenue(cowA)  
animal_revenue(goatA) 






