#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    check = []
    for i in my_list:
        if i % 2 == 0:
            check.append(True)
        else:
            check.append(False)
    return check
