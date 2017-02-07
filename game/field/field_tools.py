from ship.ship import *


def is_valid(data):
    """
    (dict) -> (bool)

    Checks if the field of the battleship game is valid.
    """
    if type(data) != dict:
        print('Wrong argument data')
        return None
    four = 0
    three = 0
    two = 0
    one = 0
    abc = 'ABCDEFGHIJ'
    for i in range(1, 11):
        for j in range(1, 11):
            el = ship_size(data, (abc[i-1], j))
            if type(el) == tuple:
                coords = el[1]
                el = el[0]
                if el == 1:
                    one += 1
                elif el == 2:
                    two += 1
                elif el == 3:
                    three += 1
                elif el == 4:
                    four += 1
                for k in coords:
                    if data[(k[0]-1, k[1]+1)] or data[(k[0]-1, k[1]+1)] == 'damaged' or data[(k[0]-1, k[1]-1)] or data[(k[0]-1, k[1]-1)] == 'damaged' or data[(k[0]+1, k[1]+1)] or data[(k[0]+1, k[1]+1)] == 'damaged' or data[(k[0]+1, k[1]-1)] or data[(k[0]+1, k[1]-1)] == 'damaged':
                        return False
    two = two // 2
    three = three // 3
    four = four // 4
    if one != 4 or two != 3 or three != 2 or four != 1:
        return False
    return True


def field_to_str(data):
    """
    (dict) -> (str)

    Converts a field into string,
    so it can be written to the file or printed on the display.
    """
    if type(data) != dict:
        print('Wrong argument type')
        return None
    field = ''

    for x in range(1, 11):
        for y in range(1, 11):
            el = data[(y, x)]
            if el:
                field += '*'
            elif not el:
                field += ' '
            elif el == 'damaged':
                field += 'X'
        field += '\n'
    return field
