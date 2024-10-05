# Collections[List, Tuple, Sets, Dictionary] and Modules

# List is an Ordered collections of items
# Mutable
# Allows duplicates

words = ['list', 'max', '1234', 'xiaopang']

nums = [123,444,555,636,777,900, 0 ,90]

random = [1,2,3,'text', nums, 'did', 'not', [-1,2,-3,-5,-9], 'hisenberg']
print(random)

for item in random:
    print(f'This is {item}')

#  Modify
random[1] = "USSR"

# Slicing  List [start:end] 
L = [1,2,3,4,5,67,89,0,1,2,3]
#    0 1 2 3 4 5  6  7 8 9 10
print(L[2:5])
print(L[:5])
print(L[1:9])

# append(), insert(), extend(), remove(), pop(), clear(), index(), count(), sort(), reverse(), reverse()


my_list = [1, 2, 3, 4, "apple", [5, 6, 7]]


my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

my_list.insert(1, 'banana') 
print(my_list)  # Output: [10, 'banana', 2, 3, 4, 5, 6]

my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)  # Output: 2

my_list.extend([7, 8])
print(my_list)  # Output: [10, 'banana', 2, 3, 4, 5, 6, 7, 8]


my_list = [1, 2, 3, 4, 5, 'banana']
my_list.remove('banana')
print(my_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8]


last_element = my_list.pop()
print(last_element)  # Output: 8
print(my_list)  # Output: [10, 2, 3, 4, 5, 6, 7]

my_list.clear()
print(my_list)  # Output: []

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]


my_list = [5, 2, 9, 1]
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 9]


my_list = [2,3,4,5,7,4,6]
count = my_list.count(2)
print(count)  # Output: 1



