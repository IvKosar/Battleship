from ship.ship import *


def is_valid(data):
    """
    (dict) -> (bool)

    Checks if the field of the battleship game is valid.
    """
    if type(data) != dict:
        print('Wrong argument data')
        return None
    number_of_ship_types = 4
    ships_number_by_types = [0 for _ in range(number_of_ship_types)]
    abc = 'ABCDEFGHIJ'
    for i in range(1, 11):
        for j in range(1, 11):
            el = ship_size(data, (abc[i-1], j))
            if type(el) == tuple:
                coords = el[1]
                el = el[0]
                cur = ships_number_by_types[el-1]
                ships_number_by_types[el-1] = cur + 1
                for k in coords:
                    if data[(k[0]-1, k[1]+1)] or data[(k[0]-1, k[1]+1)] == 'damaged' or data[(k[0]-1, k[1]-1)] or data[(k[0]-1, k[1]-1)] == 'damaged' or data[(k[0]+1, k[1]+1)] or data[(k[0]+1, k[1]+1)] == 'damaged' or data[(k[0]+1, k[1]-1)] or data[(k[0]+1, k[1]-1)] == 'damaged':
                        return False
    
    ships_number_by_types = list(map(lambda x: x//(ships_number_by_types.index(x)+1),ships_number_by_types ))
    
    for i in range(len(ships_number_by_types)):
        if ships_number_by_types[i] != i+1:
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
