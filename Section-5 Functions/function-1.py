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


