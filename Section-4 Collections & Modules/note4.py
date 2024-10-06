# unordered, mutable, and indexed collection of key-value pairs

# Empty dictionary
D = {}

# Dictionary with key-value pairs
D1 = {
    "name": "John", 
    "age": 25, 
    "city": "New York"
}

# Using dict() function
D2 = dict(name="John", age=25, city="New York")

my_dict = {
    "name": "John", 
    "age": 25, 
    "city": "New York"
}

# Accessing value by key
print(my_dict["name"])  # Output: John

# Using get()
print(my_dict.get("age"))  # Output: 25

# Add a new key-value pair
my_dict["continent"] = "US"

#update
my_dict['age'] = 26
print(my_dict)

# pop()
# Removes the specified key and returns its value.

dict = {
    "name": "Max", 
    "age": 18, 
    "city": "United Kingdom"
    }
age = dict.pop("age")
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# clear()
dict.clear()
print(dict)


tion = {
    "name": "Max", 
    "age": 18, 
    "city": "United Kingdom"
}

# keys(), values(), update()
print(tion.keys())
print(tion.values())
tion.update(
    {
        'number': 182776490,
        'framework': 'Django',
        'age': 28
    }
)

print("name" in tion)  # Output: True
print("salary" in tion)  # Output: False


myWork = {"name": "John", "age": 105, "Bank": "Central bank", 'framework':'Django'}

# Iterating over keys
for key in myWork:
    print(key)

# Iterating over values
for value in myWork.values():
    print(value)

# Iterating over key-value pairs
for key, value in myWork.items():
    print(f"{key}: {value}")


# Nested_dictionary

NEST = {

    1 : {
        'name': 'Mishkat',
        'age' : 25,
        'class': 10,
        'game' : 'Call of Duty'
    },

    2 : {
        'name': 'Tanbean',
        'age' : 25,
        'class': 11,
        'game' : 'Farcry'
    },

    3 : {
        'name': 'Guardian Knights',
        'age' : 25,
        'class': 10,
        'game' : 'Witcher 3'
    }    

}

print(NEST[1]['name'])








