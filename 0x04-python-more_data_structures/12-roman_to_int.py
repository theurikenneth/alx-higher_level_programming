#!/usr/bin.python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    n = 0
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        n += roman.get(i, 0)
    subs = {'CM': -200, 'CD': -200, 'XC': -20, 'XL': -20, 'IX': -2, 'IV': -2}
    chars = ""
    for i in range(0, len(roman_string) - 1):
        chars = roman_string[i] + roman_string[i + 1]
        if chars in subs:
            n += subs[chars]
    return n
