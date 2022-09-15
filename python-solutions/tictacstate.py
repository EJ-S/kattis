def octalTobinary(num):
    n = len(num)
    decimal = 0
    while n > 0:
        decimal += int(num[len(num)-n]) * (8**(n-1))
        n -= 1
    binary = ""
    q = decimal
    while q != 0:
        r = q%2
        q = q//2
        binary = str(r) + binary
    while len(binary) < 19:
        binary = "0" + binary
    return binary


def check_win(board):
    for i in board:
        if i[0] != -1 and i[0] == i[1] and i[1] == i[2]:
            if i[0] == '0':
                return 0
            else:
                return 1
    for j in range(3):
        if board[0][j] != -1 and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            if board[0][j] == '0':
                return 0
            else:
                return 1
    if board[0][0] != -1 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == '0':
                return 0
            else:
                return 1
    if board[0][2] != -1 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == '0':
                return 0
            else:
                return 1
    return -1



def main():
    N = int(input())
    for _ in range(N):
        number = input()
        binary_number = octalTobinary(number[1:])
        played_board = [ [0]*3 for i in range(3)]
        game_state = [ [-1]*3 for i in range(3)]
        for r in range(3):
            for c in range(3):
                if binary_number[10 + r*3 + c] == "1":
                    played_board[r][c] = 1
        for r in range(3):
            for c in range(3):
                if played_board[r][c] == 1:
                    game_state[r][c] = binary_number[1 + r*3 + c]
        result = check_win(game_state)
        in_progress = False
        if result == 1:
            print("X wins")
        elif result == 0:
            print("O wins")
        else:
            for r in range(3):
                for c in range(3):
                    if played_board[r][c] == 0:
                        in_progress = True
            if in_progress:
                print("In progress")
            else:
                print("Cat's")
        
        
        


if __name__ == "__main__":
    main()
