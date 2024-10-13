# functions are reusable blocks of code that perform a specific task. 
# They allow you to structure your code efficiently by avoiding 
# repetition

# a function may or may not have parameter/return value

def Maximum(para1, para2):     #with para and return
    return max(para1, para2)

def Greet(name):    #with para no return
    print(f"Hello {name}")

def Print58():  #no para no return
    for i in range (1,59):
        print(f"{i},")

def Guilty():   #no para and only return
    return "Sad"



m = Maximum(20, 45)  
print(m)

Greet("Ben Tenison")
Greet("Bruce Wayne")
Greet("Arya Stark")
print(Guilty())

def galaxy(name="Mishkat"):
    return f"Hello, {name}!"

print(galaxy())          # Output: Hello, Mishkat!
print(galaxy("Alice"))   # Output: Hello, Alice!


# Lambda function
# Python also supports anonymous functions called lambda functions. 
# These are small one-line functions that don’t need a def keyword.
# lambda parameters: expression

multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12


# Variable Scope
# Local Scope: Variables declared inside a function are local 
# to that function and cannot be accessed outside.
# Global Scope: Variables declared outside of functions 
# are accessible globally.


g = 90 #global variable

def fun():
    v = 100 #local variable
    print (g) #correct 
    return "Sting like a bee"

# print(v)  will show error


# Passing Collection to a function [List, dictionary, sets]

p = [1,2,3,4,5]

def printer(p):
    for i in p:
        print(f'{i}, ')

printer(p)


map = {
    'id' : '1212',
    'name' : 'Mishkat',
    'age' : '31',
    'hero' : 'Batman',
    'number' : '01795549398'
}



def display(map):
    for key, value in map.items():
        print(f"{key}: {value}")
display(map)


def show_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person = {
    "name": "Slytherine", 
    "age": 30, 
    "city": "New York"
}

# Unpacking the dictionary into keyword arguments
show_info(**person)


# passing function to a function

# Define two simple functions
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

# A higher-order function that takes another function as an argument
def operate(fun, x, y):
    result = fun(x, y)
    print(f"Result: {result}")

# Passing the 'add' function as an argument
operate(add, 5, 3)       # Output: Result: 8

# Passing the 'mul' function as an argument
operate(mul, 5, 3)  # Output: Result: 15

# When operate(add, 5, 3) is called, the function add is 
# passed to operate as the func argument, and it is executed 
# inside operate.The same goes for multiply.


# A higher-order function
def op(func, x, y):
    result = func(x, y)
    print(f"Result: {result}")

# Passing a lambda function to op
op(lambda a, b: a - b, 10, 5)   # Output: Result: 5

# Instead of defining a separate function (like add or multiply), 
# we used an inline lambda function (lambda a, b: a - b), which 
# subtracts b from a. Lambda functions are useful when you want 
# to pass a small piece of functionality without defining a separate function.

