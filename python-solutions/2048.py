import sys


def make_moved_row(row):
    out_row = []
    for num in row:
        if int(num) != 0:
            out_row.append(int(num))
    return out_row


def make_moved_row_reverse(row):
    out_row = []
    for num in row:
        if int(num) != 0:
            out_row.insert(0, int(num))
    return out_row


def make_size(row):
    while len(row) < 4:
        row.append(0)
    return row


def make_size_reverse(row):
    while len(row) < 4:
        row.insert(0, 0)
    return row


def move_left(game_state):
    output = []
    for row in game_state:
        try:
            row = row.split()
        except AttributeError:
            row = row
        move_row = make_moved_row(row)
        move_row = make_size(move_row)
        for i in range(3):
            if move_row[i] == move_row[i + 1]:
                move_row[i] = move_row[i] * 2
                move_row[i+1] = 0
                move_row = make_moved_row(move_row)
                move_row = make_size(move_row)

        output.append(move_row)

    return output


def move_right(game_state):
    output = []
    for row in game_state:
        try:
            row = row.split()
        except AttributeError:
            row = row
        move_row = make_moved_row(row)
        move_row = make_size_reverse(move_row)
        for i in range(2, -1, -1):
            if move_row[i] == move_row[i + 1]:
                move_row[i] = move_row[i] * 2
                move_row[i+1] = 0
                move_row = make_moved_row(move_row)
                move_row = make_size_reverse(move_row)
        output.append(move_row)

    return output


def move_up(game_state):
    game_state = rotate_by_90_ccw(game_state)
    game_state = move_left(game_state)
    game_state = rotate_by_90_cw(game_state)
    return game_state


def move_down(game_state):
    game_state = rotate_by_90_ccw(game_state)
    game_state = move_right(game_state)
    game_state = rotate_by_90_cw(game_state)
    return game_state


def rotate_by_90_ccw(game_state):
    update_game_state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(game_state)):
        try:
            row = game_state[i].split()
        except AttributeError:
            row = game_state[i]
        for j in range(4):
            update_game_state[j][i] = row[abs(j-3)]
    return update_game_state


def rotate_by_90_cw(game_state):
    update_game_state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        try:
            row = game_state[i].split()
        except AttributeError:
            row = game_state[i]
        for j in range(4):
            update_game_state[j][abs(i-3)] = row[j]
    return update_game_state


def main():
    cin = sys.stdin.readlines()
    move = int(cin[4])
    if move == 0:
        out = move_left(cin[0:4])
    elif move == 1:
        out = move_up(cin[0:4])
    elif move == 2:
        out = move_right(cin[0:4])
    else:
        out = move_down(cin[0:4])
    output = ''
    for row in out:
        for item in row:
            output += str(item) + ' '
        output += '\n'
    print(output)


if __name__ == "__main__":
    main()
