#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        _max = 0
        key = ""
        for key, value in a_dictionary.items():
            if value > _max:
                _max = value
                name = key
        return name
