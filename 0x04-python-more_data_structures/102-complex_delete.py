#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary"""
    while value in a_dictionary.value():
        for i, j in a_dictionary.items():
            if j == value:
                del a_dictionary[i]
                break

    return (a_dictionary)
