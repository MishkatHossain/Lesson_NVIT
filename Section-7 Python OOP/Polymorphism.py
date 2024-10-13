# You are already using Polymorphism
print(len("Hello"))  # Output: 5 (works on strings)
print(len([1, 2, 3, 4]))  # Output: 4 (works on lists)


class Laptop:
    def operate(self):
        print("Operating Laptop")

class Smartphone:
    def operate(self):
        print("Operating Smartphone")

def device_operation(device):
    device.operate()

laptop = Laptop()
phone = Smartphone()

device_operation(laptop)  # Output: Operating Laptop
device_operation(phone)   # Output: Operating Smartphone


class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

square1 = Square(4)
circle1 = Circle(6)

print(square1.area())
print(circle1.area())





























