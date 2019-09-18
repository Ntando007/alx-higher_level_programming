#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copia = my_list[:]
    if idx < 0 and idx > len(my_list):
        return copia
    else:
        copia[idx] = element
        return copia
