import time

def hex_to_rgb(value, formatted=True):
    if len(value) != 3 and len(value) != 6:
        raise NotImplemented("Invalid hex property passed")
    split_value = int(len(value) / 3)
    values = []
    while value != '':
        values.append(value[:split_value])
        value = value[split_value:]
    result = list()
    try:
        result = [int(i, 16) for i in values]
    except ValueError:
        raise NotImplemented("Invalid hex property passed")
    return f"rgb({result[0]}, {result[1]}, {result[2]})" if formatted else result

"""
def true_shader(value, ratio):
    result = []
    for i in range(3):
        result.append(
"""
#print(hex_to_rgb("222627", False))