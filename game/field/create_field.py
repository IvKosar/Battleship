import random
from field.field_tools import *


def read_field(filename):
    """
    (str) -> (dict)

    Reads a field for the battleship game.
    Returns the dict of coords with values:
    ' ' if there is free cell,
    '*' if there is a ship,
    'X' if there is a damaged ship.
    """
    if type(filename) != str:
        print("Filename must be a string")
        return None
    result = {}
    status = {' ': False, '*': True, 'X': 'damaged'}
    with open(filename, 'r') as file:
        data = file.readlines()
    for line in range(1, 11):
        for element in range(1, 11):
            result[(element, line)] = status[data[line-1][element-1]]
    for i in range(-1, 13):
        result[(i, 0)] = None
        result[(i, 11)] = None
        result[(11, i)] = None
        result[(0, i)] = None
        result[(i, 12)] = None
        result[(12, i)] = None
        result[(-1, i)] = None
        result[(i, -1)] = None
    return result


def putShip(data, size, rotation):
    """
    (dict, int, int, int, int) -> (dict)
    Put a ship of given size on the position with rotation.
    """
    if type(data) != dict:
        print('Wrong first argument.')
        return None
    if type(size) != int:
        print('Wrong second argument.')
        return None
    if type(rotation) != int:
        print('Wrong third argument.')
        return None
    # freeCoords = []
    # for e in data:
    #    if e[0] > 0 and e[1] > 1 and e[0] < 11 and e[1] < 11:
    #        if data[e] == False:
    #            freeCoords.append(e)
    # tmp = random.choice(freeCoords)
    # x = tmp[0]
    # y = tmp[1]

    x = random.randint(1, 11)
    y = random.randint(1, 11)
    can = 0
    if rotation == 0:
        while can != size:
            can = 0
            while data[x, y]:
                # tmp = random.choice(freeCoords)
                # x = tmp[0]
                # y = tmp[1]
                x = random.randint(1, 11)
                y = random.randint(1, 11)
            for i in range(0, size):
                if not data[x + i, y] or not data[x + i + 1][y + 1] or not data[x + i + 1][y - 1] or \
                                not data[x + i - 1][y + 1] or not data[x + i - 1][y - 1]:
                    can += 1
                elif data[x + i, y] is None:
                    can = 0
                    # tmp = random.choice(freeCoords)
                    # x = tmp[0]
                    # y = tmp[1]
                    x = random.randint(1, 11)
                    y = random.randint(1, 11)
                    break
        for i in range(0, size):
            data[(x + i, y)] = True
    elif rotation == 1:
        while can != size:
            can = 0
            while data[x, y]:
                # tmp = random.choice(freeCoords)
                # x = tmp[0]
                # y = tmp[1]
                x = random.randint(1, 11)
                y = random.randint(1, 11)
            for i in range(0, size):
                if not data[x, y + 1] or not data[x + 1][y + 1 + i] or not data[x + 1][y - 1 + i] or \
                                not data[x - 1][y + 1 + i] or not data[x - 1][y - 1 + i]:
                    can += 1
                elif data[x, y + i] is None:
                    can = 0
                    # tmp = random.choice(freeCoords)
                    # x = tmp[0]
                    # y = tmp[1]
                    x = random.randint(1, 11)
                    y = random.randint(1, 11)
                    break
        for i in range(0, size):
            data[(x, y + i)] = True
    return data


def generate_field():
    """
    () -> (data)

    Generates a field (not always valid) for the battleship game.
    """
    done = 1
    while done:
        try:
            # print('start')
            result = {}

            for i in range(1, 11):
                for j in range(1, 11):
                    result[(i, j)] = False

            for i in range(-1, 13):
                result[(i, 0)] = None
                result[(i, 11)] = None
                result[(11, i)] = None
                result[(0, i)] = None
                result[(i, 12)] = None
                result[(12, i)] = None
                result[(-1, i)] = None
                result[(i, -1)] = None

            # print(' continue ')
            result = putShip(result, 4, random.randint(0, 1))
            result = putShip(result, 3, random.randint(0, 1))
            result = putShip(result, 3, random.randint(0, 1))
            result = putShip(result, 2, random.randint(0, 1))
            result = putShip(result, 2, random.randint(0, 1))
            result = putShip(result, 2, random.randint(0, 1))
            result = putShip(result, 1, random.randint(0, 1))
            result = putShip(result, 1, random.randint(0, 1))
            result = putShip(result, 1, random.randint(0, 1))
            result = putShip(result, 1, random.randint(0, 1))
            #print('   next   ')
            done = 0
        except KeyError:
            done = 1
    return result

def generate_valid_field():
    """
    () -> (dict)

    Generates valid field for the game.
    """
    field = generate_field()
    while not is_valid(field):
        field = generate_field()
    return field
