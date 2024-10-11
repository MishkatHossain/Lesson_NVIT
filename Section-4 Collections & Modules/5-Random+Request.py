import random
import os

v = random.randint(1,9)
print(v)

list = ['Hi', 'Hello', 'Welcome back', 'Hey']
value = random.choice(list)

print(value)

n = random.randint(1,100)



if n % 2 == 0:
    print(str(n) + " number is even")
else:
    print(str(n) + " number is odd")


# help(os)
# help(random)

# monopoly
ice = random.randint(1, 6)
fire = random.randint(1, 6)

print(ice+fire)

x = random.random()
print(x)

