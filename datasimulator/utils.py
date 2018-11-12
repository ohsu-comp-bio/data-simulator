import random


def is_mixed_type(arr):
    if arr:
        return any(not isinstance(e, type(arr[0])) for e in arr)
    return False


def random_choice(arr):
    if arr:
        return random.choice(arr)
    return None


def is_primitive_type(data):
    return isinstance(data, (int, float, str))


def get_recursive_keys(dictionary):
    keys = []
    for key, value in dictionary.items():
        keys.append(key)
        if type(value) is dict:
            keys = keys + get_recursive_keys(value)

    return keys


def get_recursive_values(dictionary):
    values = []
    for _, value in dictionary.items():
        if type(value) is dict:
            values = values + get_recursive_values(value)
        else:
            values.append(value)
    return values
