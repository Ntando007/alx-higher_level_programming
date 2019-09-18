#!/usr/bin/env python3
def no_c(my_string):
    badchar = ['C', 'c']
    my_string = ''.join(i for i in my_string if i not in badchar)
    return my_string
