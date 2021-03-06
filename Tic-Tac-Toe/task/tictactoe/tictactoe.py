# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)

# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)


def create_playing_field(size):
    tmp_field = []
    for i in range(size):
        tmp = []
        for j in range(size):
            tmp.append(' ')
        tmp_field.append(tmp)
    return tmp_field


def print_playing_field(field):
    print('---------')
    for i in range(len(field)):
        line = '| '
        for j in range(len(field)):
            line += field[i][j]
            line += ' '
        line += '|'
        print(line)
    print('---------')


def initialize_playing_field(initial_state, size, field):
    for i in range(size):
        for j in range(size):
            field[i][j] = initial_state[3 * i + j]


def check_state(field):
    #True = game finished
    size = 3
    O_number = 0
    X_number = 0
    empty_cells = 0
    words = []
    o_victory = False
    x_victory = False
    impossible = False
    for i in range(size):
        for j in range(size):
            if field[i][j] == 'O':
                O_number += 1
            if field[i][j] == 'X':
                X_number += 1
            if field[i][j] == "_":
                empty_cells += 1

    for i in range(size):
        tmp_hor = field[i][0] + field[i][1] + field[i][2]
        tmp_ver = field[0][i] + field[1][i] + field[2][i]
        words.append(tmp_hor)
        words.append(tmp_ver)
    word_diag_1 = field[0][0] + field[1][1] + field[2][2]
    word_diag_2 = field[0][2] + field[1][1] + field[2][0]
    words.append(word_diag_1)
    words.append(word_diag_2)
    if 'XXX' in words:
        x_victory = True
        print("X wins")
    elif 'OOO' in words:
        o_victory = True
        print("O wins")
    elif empty_cells == 0:
        print("Draw")
    return x_victory or o_victory or empty_cells == 0






def convert_coordinates(x, y):
    if x == 1 and y == 1:
        return 2, 0
    if x == 2 and y == 1:
        return 2, 1
    if x == 3 and y == 1:
        return 2, 2
    if x == 1 and y == 2:
        return 1, 0
    if x == 2 and y == 2:
        return 1, 1
    if x == 3 and y == 2:
        return 1, 2
    if x == 1 and y == 3:
        return 0, 0
    if x == 2 and y == 3:
        return 0, 1
    if x == 3 and y == 3:
        return 0, 2


def is_input_correct(coordinates):
    coordinates = coordinates.split()
    if (len(coordinates) != 2):
        print("You should enter numbers!")
        return False
    x = coordinates[0]
    y = coordinates[1]
    allowed_digits = '0123456789'
    if str(x) not in allowed_digits or str(y) not in allowed_digits:
        print("You should enter numbers!")
        return False
    if int(x) not in range(1, 4) or int(y) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    x, y = convert_coordinates(int(x), int(y))
    if field[x][y] != '_':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def make_move(x, y, sign):
    field[x][y] = sign


size = 3
field = create_playing_field(size)

initial_state = "_________"
initialize_playing_field(initial_state, size, field)
print_playing_field(field)

moves = 0
while not check_state(field):
    sign = ''
    if moves % 2 == 0:
        sign = 'X'
    else:
        sign = 'O'
    coordinates = input("Enter the coordinates:")
    while not is_input_correct(coordinates):
        coordinates = input("Enter the coordinates:")
    coordinates = coordinates.split()
    x, y = convert_coordinates(int(coordinates[0]), int(coordinates[1]))
    make_move(x, y, sign)
    print_playing_field(field)
    moves += 1


