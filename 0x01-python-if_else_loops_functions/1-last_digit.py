#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
s = "Last digit of"
if last > 5:
    print("{} {} is {} and is greater than 5".format(s, number, last))
if last == 0:
    print("{} {} is {} and is 0".format(s, number, last))
if last < 6 and last != 0:
    print("{} {} is {} and is less than 6 and not 0".format(s, number, last))
