# Conditional Statements (if, elif, else) 

# For decision-making by 
# executing different blocks of code 
# based on certain conditions.

# comparision operator ==, !=, >, >=, <, <=,

x = 10
if x > 5:
    print("x is greater than 5")
if True:
    print(f"{x} will always print")
if 0:
    print(f"{x} will never be printed")

y = input('Enter a number: ')
if y==20 or y<10:
    print("Why so serious")
else:
    print("List is a Dynamic Array")

# else if used if no condition is met. Acts as a default

salary = int(input('Enter your salary: '))

# else, elif needed for conditional efficiency
# avoid unecessay checking for efficiency
if salary>12000:
    print("You will get bonus")
elif salary==12000:
    print('You will get 100 taka extra')
elif salary==11000:
    print('You will get free lunch and cab fair')
else:
    print('Sorry. No lunch/bonus')

a = True
b = False

# Logical AND
print(a and b) #False
# Logical OR
print(a or b)  #True
# Logical NOT
print(not a)  # Output: False

# Looping statement (for, while)

# for
for i in range(10): #0 to (10-1)
    print(i)

for i in range(2, 10): #range (inclusive, exclusive)
    print(i)

# while ()
count = 0
while count < 5:
    print(count)
    count += 1

# Control Flow Statements (break, continue, pass)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(6): #pass does nothing. used for future code
    if x > 10:
        pass  # Placeholder for future code



