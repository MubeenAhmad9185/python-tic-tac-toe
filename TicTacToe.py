def make_board():
    return [[' ' for _ in range(3)]for _ in range(3)]
board = make_board()

def display_board(board):

    for row in board:
        print('|'.join(row))
        print('_' * 5)


def make_move(board, player):
    try:
        while True:
            row = int(input(f"Player {player} enter row (0, 1, 2): "))
            col = int(input(f"Player {player} enter column (0, 1, 2): "))

            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("The spot is already taken. ")
    except (ValueError, IndexError):
        print("Invalid character")



def check_winner(board,player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[col][row] == player for row in range (3)]):
            return True


    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    else:
        return False


def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    else:
        return True

def switch_move(current_player):
    return 'O' if current_player == 'X' else 'X'


def play_game():
    board = make_board()
    current_player = "X"

    while True:
        display_board(board)

        make_move(board,current_player)
        if check_winner(board,current_player):
            display_board(board)
            print(f"player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("it's a tie!")
            break

        current_player = switch_move(current_player)

play_game()
