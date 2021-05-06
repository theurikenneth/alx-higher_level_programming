def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        idct([key, value])
    else:
        a_dictionary.update({key: value})
    return a_dictionary
