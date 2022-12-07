#!/usr/bin/python3
def add(a, b):
  a = 1
  b = 2
  while a < b:
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    
