def read_field(filename):
    """
    (str) -> (data)

    Reads a field for the battleship game.

    """
    if type(filename) != str:
        print("Filename must be a string")
        return None
    result = {}
    status = {' ' : False, '*' : True, 'X': 'damaged'}
    with open(filename, 'r') as file:
        data = file.readlines()
    for line in range(1, 11):
        for element in range(1, 11):
            result[(element, line)] = status[data[line-1][element-1]]
    for i in range(-1, 12):
        result[(i, 0)] = None
        result[(i, 11)] = None
        result[(11, i)] = None
        result[(0, i)] = None
    return result


def generate_field():
    """
    () -> (data)

    Generates a field for the battleship game.
    """
    import random
