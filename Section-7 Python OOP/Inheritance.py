# Basic Syntax:

class ParentClass:
    # Parent class code
    pass

class ChildClass(ParentClass):
    pass



class Car:
    def __init__(self, name, model, year, topspeed):
        self.name = name,
        self.model = model,
        self.year = year, 
        self.topspeed = topspeed


    def drive(self):
        print(f"{self.name} is accelerating")
    def stop(self):
        print(f"{self.name} Stop ... .. . .")


class Electric(Car):

    def __init__(self, name, model, year, topspeed, battery_capacity):
        super().__init__(name, model, year, topspeed)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.name} is Charging")

# Inheritance with super(): The Electric class uses the super() function to call the parent class (Car) constructor, allowing it to initialize name, model, year, and topspeed from the Car class.
# Additional Attributes: The Electric class has an additional attribute battery_capacity, which is specific to electric cars.
# Method Access: You can access methods from both the Car class (drive() and stop()) and any new methods in the Electric class (charge()).





