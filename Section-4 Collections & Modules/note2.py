# Tuple
# Ordered collection of items.
# Immutable (cannot change after creation).
# Allows duplicates.

# Tuple with values
my_tuple = (1, 2, 3, "apple", [5, 6])


# Accessing elements
print(my_tuple[0])  # Output: 1

# Tuples cannot be modified:
# my_tuple[1] = 5  # This will Error

# Slicing is same as List
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

# You can check whether an item exists in a tuple using the in keyword.
tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True
print(5 in my_tuple)  # Output: False


