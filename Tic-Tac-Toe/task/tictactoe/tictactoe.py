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
    if abs(O_number - X_number) > 1:
        impossible = True
    if 'XXX' in words:
        x_victory = True
    if 'OOO' in words:
        o_victory = True
    if x_victory and o_victory:
        impossible = True

    if impossible:
        print("Impossible")
    elif o_victory:
        print("O wins")
    elif x_victory:
        print("X wins")
    elif empty_cells == 0:
        print("Draw")
    else:
        print("Game not finished")


size = 3
field = create_playing_field(size)
initial_state = input('Enter cells:')
initialize_playing_field(initial_state, size, field)
print_playing_field(field)
check_state(field)


