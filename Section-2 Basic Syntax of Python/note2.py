# String Manipulation: "Anything that is enclosed in a double quotation mark is string"
# Strings are immutable. They cannot be changed

# String adding
m = "max"
n = 'nax'
v = m+n
print(v)

Max = "Mahito Warlord"
print(Max[0]) #M
print(Max[4]) #t
print(Max[1]) #a
print(Max[20]) #invalid 
print(Max[16]) #invalid
print(len(Max)) #15


print(Max[1])
Max[2] = "H" #invalid

print(Max.upper()) #output: MAHITO WARLORD
print(Max.lower()) #output: mahito warlord 

#strip() #removing leading spaces
text = "     M K L M M M     "
print(text.strip())

#replace(old, new): Replaces a substring with another.
sentence = "Hello World"
print(sentence.replace("World", "Python"))  # Output: Hello Python

# find(substring): Returns the lowest index of the substring if it is found, otherwise -1.
sentence = "Hello World"
print(sentence.find("World"))  # Output: 6






# Multiline String 
var_multiline = """"
This is called multiline string.
This is a speciality of multiline string.
max max max max
max max max max

max max max max
max max max max
Failed to kill the knight king with a dragon glass
"""


print(var_multiline.find("max"))



#input/output
name = input('Enter your name: ')
print("Hello, " + name + '!!! Welcome back')

age = input('Enter your age: ')
print('MISHKAT is ' + age + ' years old')

number = input('Enter your number: ')
print(number + 'is a number. '+ number + 'is your favourite number')



#Type casting and Type function type()
a = "1234.908"
b = "124"
c = 1233333
converted_a = float(a)
print(type(converted_a))
converted_b = type(b)
print(type(converted_b))
print(str(c))


# The format methods .format(args, args) and f-string [string addition not needed]
name = "Mishkat"
age = 30
info = "My name is {} and I am {} years old. {} is my favourite number".format(name, age, age)
orInfo = "My name is {name} and I am {age} years old. {age} is my favourite number}"

print(info)
print(orInfo)




