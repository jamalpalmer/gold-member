import random

numbers = list(range(0,5))

print(numbers)

for number in numbers:
    print(number*2)

for i in range(0,5): #do somehting fixed number of times
    print("This is from a for loop",str(i))

number = random.randint(0,100)

counter = 0
while number != 52: # do until condition is false
    number = random.randint(0,100)
    counter += 1
print(counter, number)

for i in range(1000):
    number = random.randint(0,100)
    if (number ==52):
        break
    
print(1, number)