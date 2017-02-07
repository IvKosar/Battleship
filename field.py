def read_field(filename):
    """
    (str) -> (data)

    Reads a field for the battleship game.
    Returns with numeration A..J horizontally
    and 1..10 vertically as list of lists.
    """
    if type(filename) != str:
        print("Filename must be a string")
        return None
    with open(filename, 'r') as file:
        data = file.readlines()
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = [letters]
    for line in range(0, 10):
        result.append(list(data[line].strip('\n').upper()))
        if line == 0:
            result[line].insert(0, '%')
        elif line < 10:
            result[line].insert(0, line)
            result[line].append('|')
    result[10].insert(0, 10)
    result[10].insert(11, '|')
    result.append(['-'] * 12)
    return result

for i in read_field('field.txt'):
    print(i)


def has_ship(data, cell):
    """
    (data, tuple) -> (bool)

    Checks if there is a ship on the cell (e.g (A,1)) in the table.
    """
    if type(data) != list:
        print('Wrong argument data')
        return None
    if type(cell) != tuple:
        print("Second argument must be a tuple")
        return None
    if type(cell[0]) != str:
        print("First element of the second argument must be a str - A..J")
        return None
    if type(cell[1]) != int:
        print("Second element of the second argument must be a numeber - 1..10")
        return None
    x = ord(cell[0].upper())-64
    y = cell[1]
    if x < 1 or x > 10:
        print('Wrong coordinate. Must be from A to J.')
        return None
    if y < 1 or y > 10:
        print('Wrong coordinate. Must be from 1 to 10.')
        return None
    if data[y][x] in '*X':
        return True
    elif data[y][x] == ' ':
        return False


def ship_size(data, cell):
    """
    (data, tuple) -> (tuple)

    Checks the ship size on the cell.
    """
    if type(data) != list:
        print('Wrong argument data')
        return None
    if type(cell) != tuple:
        print("Second argument must be a tuple")
        return None
    if type(cell[0]) != str:
        print("First element of the second argument must be a str - A..J")
        return None
    if type(cell[1]) != int:
        print("Second element of the second argument must be a numeber - 1..10")
        return None
    x = ord(cell[0].upper()) - 64
    y = cell[1]
    if x < 1 or x > 10:
        print('Wrong coordinate. Must be from A to J.')
        return None
    if y < 1 or y > 10:
        print('Wrong coordinate. Must be from 1 to 10.')
        return None
    size = 0

    if str(data[y][x+1]) in 'X*':
        for i in range(x, 11):
            if str(data[y][i]) in 'X*':
                size += 1
            elif data[y][i] == ' ':
                break
    elif str(data[y][x-1]) in 'X*':
        if size == 0:
            x = x
        else:
            x = x - 1
        for i in range(x, 1, -1):
            if str(data[y][i]) in 'X*':
                size += 1
            elif str(data[y][i]) == ' ':
                break
    elif str(data[y+1][x]) in 'X*':
        for j in range(y, 11):
            if str(data[j][x]) in 'X*':
                size += 1
            elif data[j][x] == ' ':
                break
    elif str(data[y-1][x]) in 'X*':
        if size == 0:
            y = y
        else:
            y = y - 1
        for j in range(y, 1, -1):
            if str(data[j][x]) in 'X*':
                size += 1
            elif str(data[j][x]) in 'X*':
                break
    if str(data[y][x]) in '*X':
        size+=1
    return size


def is_valid(data):
    """
    (data) -> (bool)

    Checks if the field of the battleship game is valid.
    """
    if type(data) != list:
        print('Wrong argument data')
        return None
    four = 0
    three = 0
    two = 0
    one = 0
    letres = 'ABCDEFGHIJ'
    for i in range(1, 11):
        for j in range(1, 11):
            if str(data[i][j]) == '*' and str(data[i+1][j+1]) in 'X*' and str(data[i+1][j-1]) in 'X*' and str(data[i-1][j+1]) in 'X*' and str(data[i-1][j-1]) in 'X*':
                print('i =', i, 'j = ', j)
                print('data[', i+1, '][', j+1, '] = ', data[i+1][j+1], '|', data[i+1][j+1] not in 'X*')
                print('data[', i + 1, '][', j - 1, '] = ', data[i + 1][j - 1], '|', data[i+1][j-1] not in 'X*')
                print('data[', i - 1, '][', j + 1, '] = ', data[i - 1][j + 1], '|', data[i-1][j+1] not in 'X*')
                print('data[', i - 1, '][', j - 1, '] = ', data[i - 1][j - 1], '|', data[i-1][j-1] not in 'X*')
                return False
    for i in range(1, 11):
        for j in range(1, 11):
            s = ship_size(data, (letres[i-1], j-1))
            if s == 4:
                four += 1
            elif s == 3:
                three += 1
            elif s == 2:
                two += 1
            elif s == 1:
                one += 1
    '''
    def horizontal_check(one, two, three, four):
        """
        (int, int, int, int) -> ()

        Horizontally counts ships on the field.
        """
        for i in range(1, 11):
            for j in range(1, 11):
                if str(data[i][j]) == '*' and str(data[i+1][j]) not in '*X' and str(data[i-1][j]) not in '*X' and str(data[i][j+1]) not in '*X' and str(data[i][j-1]) not in '*X':
                    one += 1
            for j in range(1, 8):
                ship = ''.join(data[i][j:j + 4])
                if ship == ' ** ' and '*' not in  ''.join(str(data[i - 1][j:j + 4])) and '*' not in ''.join(str(data[i + 1][j:j + 4])):
                    two += 1
            for j in range(1, 7):
                ship = ''.join(data[i][j:j + 5])
                if ship == ' *** ' and '*' not in ''.join(str(data[i - 1][j:j + 5])) and '*' not in  ''.join(str(data[i + 1][j:j + 5])):
                    three += 1
            for j in range(1, 6):
                ship = ''.join(data[i][j:j + 6])
                if ship == ' **** ' and '*' not in  ''.join(str(data[i - 1][j:j + 6])) and '*' not in ''.join(str(data[i + 1][j:j + 6])):
                    four += 1
        return one, two, three, four


    one, two, three, four = horizontal_check(one, two, three, four)
    data = list(map(list, zip(*data))) # Transpose list of lists
    data.append([' '] * 12)
    one, two, three, four = horizontal_check(one, two, three, four)
    one = one // 2
    '''
    if four == 4 and three == 6 and two == 6 and one == 4:
        return True
    else:
        print(one, two, three, four)
        return False


def field_to_str(data):
    """
    (data) -> (str)

    Converts a field into string,
    so it can be written to the file or printed on the display.
    """
    if type(data) != list:
        print('Wrong argument data')
        return None
    result = ''
    for i in data:
        result += ''.join(i[1:-1]) + '\n'
    return result[10:-12]


def generate_field():
    """
    () -> (data)

    Generates a field for the battleship game.
    """
    import random
    top = ['%' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    field = [top]
    for i in range(1, 11):
        field.append([' '] * 10)
        field[i].insert(0, i)
        field[i].insert(11, '|')
    field.append(['-'] * 12)

        

    '''
    def putHorizontally(field, size):
        """
        (list(list), int) -> (field)

        Puts a ship of given size onto the game field.
        """
        if type(size) != int:
            print('Give a proper size (int).')
            return None
        y = random.randint(1, 10)
        x = random.randint(1, 11 - size)
        k = 0
        while (k != size):
            k = 0
            while (field[y][x] == '*' or field[y][x] == '#'):
                x = random.randint(1, 11 - size)
                y = random.randint(1, 10)
            for i in range(x, x + size):
                if field[y][i] == '*':
                    k=0
                    break
                else:
                    k += 1
        field[y][x - 1] = '#'
        if field[y-1][x - 1] != '*':
            field[y-1][x - 1] = '#'
        if field[y + 1][x - 1] != '*':
            field[y + 1][x - 1] = '#'
        for i in range(x, x + size):
            field[y+1][i] = '#'
            field[y - 1][i] = '#'
            field[y][i] = '*'
        field[y][x + size] = '#'
        #if field[y-1][x + size] != '*':
        #    field[y-1][x + size] = '#'
        #if field[y+1][x + size]  != '*':
        #    field[y+1][x + size] = '#'
        return field


    def putVertically(field, size):
        """
        (list(list), int) -> (field)

        Puts a ship of given size onto the game field.
        """
        if type(size) != int:
            print('Give a proper size (int).')
            return None
        y = random.randint(1, 11-size)
        x = random.randint(1, 10)
        k = 0
        while(k != size):
            k = 0
            while (field[y][x] == '*' or field[y][x] == '#'):
                y = random.randint(1, 11 - size)
                x = random.randint(1, 10)
            for i in range(y, y + size):
                if field[i][x] == '*':
                    k=0
                    break
                else:
                    k += 1
        field[y-1][x] = '#'
        #if field[y-1][x-1] != '*':
        #    field[y-1][x-1] = '#'
        #if field[y - 1][x + 1] != '*':
        #    field[y - 1][x + 1] = '#'
        for i in range(y, y + size):
            field[i][x - 1] = '#'
            field[i][x + 1] = '#'
            field[i][x] = '*'
        field[y+size][x] = '#'
        if field[y + size][x+1] != '*':
            field[y + size][x+1] = '#'
        if field[y + size][x-1] != '*':
            field[y + size][x-1] = '#'
        return field

    for i in range(1):
        rotate = random.randint(0,1)
        if rotate == 0:
            field = putHorizontally(field, 4)
        elif rotate == 1:
            field = putVertically(field, 4)
    for i in range(2):
        rotate = random.randint(0,1)
        if rotate == 0:
            field = putHorizontally(field, 3)
        elif rotate == 1:
            field = putVertically(field, 3)
    for i in range(3):
        rotate = random.randint(0,1)
        if rotate == 0:
            field = putHorizontally(field, 2)
        elif rotate == 1:
            field = putVertically(field, 2)
    for i in range(4):
        rotate = random.randint(0,1)
        if rotate == 0:
            field = putHorizontally(field, 1)
        elif rotate == 1:
            field = putVertically(field, 1)
    for i in field:
        for j in range(1, 11):
            if i[j] == '#':
                i[j] = ' '
    '''
    field[0] = top
    for j in range(1, 11):
        field[j][0] = j
        field[j][11] = '|'
    for j in range(12):
        field[11][j] = '-'
    return field

print()
table = generate_field()
#print(is_valid(table))
#while(not is_valid(table)):
#    print()
#    table = generate_field()
#    for i in table:
#        print(i)

#for i in table:
#    print(i)
print('info')
print(is_valid(read_field('field.txt')))
print(ship_size(read_field('field.txt'), ('B', 4)))

#print(field_to_str(table))
