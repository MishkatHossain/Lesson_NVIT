import os
import random

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


options = ('rock', 'paper', 'scissors')

option = random.choice(options)
print(option)


cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
]

random.shuffle(cards)
print(cards)


lo = 1
hi = 100

guessess = 0

number = random.randint(lo, hi)

while True:
    guess = int(input(f"Guess a number between ({lo} <--> {hi}): "))
    guessess += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f'{guess} is too high')
    else:
        print(f'Correct guess[{guess}]. You won. Thanks for playing.')
        print(f'This round took you {guessess} guesses')
        print('Exiting... ... ...')
        break
