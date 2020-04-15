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


size = 3
field = create_playing_field(size)
initial_state = input('Enter cells:')
initialize_playing_field(initial_state, size, field)
print_playing_field(field)

