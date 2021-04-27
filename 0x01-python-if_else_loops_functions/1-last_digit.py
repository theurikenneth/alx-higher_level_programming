#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = number % -10
else:
    last_number = number % 10

if last_number > 5:
    print("Last digit of {0:d} is {1:d}".format(number, last_number), end=' ')
    print("and is greater than 5")
elif last_number == 0:
    print("Last digit if {0:d} is {1:d} and is 0".format(number, last_number))
elif last_number < 6 and last_number != 0:
    print("Last digit of {0:d} is {1:d}".format(number, last_number), end=' ')
    print("and is less than 6 and not 0")
