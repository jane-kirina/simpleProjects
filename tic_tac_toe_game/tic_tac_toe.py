r"""Simple implementation of Tic Tac Toe game with computer"""
import os
import random as r

board = [' ' for x in range(9)]


# HELPER FUNCS
def insert_symbol(symbol, position):
    board[position] = symbol


def is_space_free(position):
    return board[position] == ' '


def is_board_full():
    return False if (board.count(' ') > 1) else True


def select_random(moves):
    r.shuffle(moves)

    if len(moves[0]) > 0:
        return moves[0][r.randrange(0, len(moves[0]))]
    elif len(moves[1]) > 0:
        return moves[1][r.randrange(0, len(moves[1]))]
    else:
        return -1


def print_board():
    for i in range(len(board) // 3):
        sub_list = board[i * 3:(i + 1) * 3]
        print(' | '.join(map(str, sub_list)))


def is_winner(board_to_check, symbol):
    return (board_to_check[0] == board_to_check[1] == board_to_check[2] == symbol) \
        or (board_to_check[3] == board_to_check[4] == board_to_check[5] == symbol) \
        or (board_to_check[6] == board_to_check[7] == board_to_check[8] == symbol) \
        or (board_to_check[0] == board_to_check[3] == board_to_check[6] == symbol) \
        or (board_to_check[1] == board_to_check[4] == board_to_check[7] == symbol) \
        or (board_to_check[2] == board_to_check[5] == board_to_check[8] == symbol) \
        or (board_to_check[0] == board_to_check[4] == board_to_check[8] == symbol) \
        or (board_to_check[2] == board_to_check[4] == board_to_check[6] == symbol)


# PLAYERS' MOVES
def player_move():
    run = True
    while run:
        position = input("Select a position to place X (1-9): ")
        if not str.isdigit(position):
            print("Please enter number")
        elif 0 < int(position) < 10:
            if is_space_free(int(position) - 1):
                run = False
                insert_symbol('X', int(position) - 1)
            else:
                print("This place is taken")
        else:
            print("Number must be between 1-9")


def computer_move():
    possible_moves = [x for x, symbol in enumerate(board) if symbol == ' ']

    # check if player is winning
    for sym in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = sym
            if is_winner(board_copy, sym):
                return i

    # pick the optimal position
    if 4 in possible_moves:
        return 4

    corners_open = []
    for i in possible_moves:
        if i in [0, 2, 6, 8]:
            corners_open.append(i)

    edges_open = []
    for i in possible_moves:
        if i in [1, 3, 5, 7]:
            edges_open.append(i)

    position = select_random([corners_open, edges_open])

    return position


# MAIN
def main():
    print('Welcome to the Game!')
    flag = True

    while flag:
        os.system('cls')
        print()
        print_board()

        # Player's turn
        if not (is_winner(board, 'O')):
            player_move()
        else:
            print('Computer wins!')
            flag = False

        # Computer's turn
        if not (is_winner(board, 'X')):
            move = computer_move()
            if move != -1:
                insert_symbol('O', move)
        else:
            print('You win!')
            flag = False

        # Check, if board is full
        if is_board_full():
            os.system('cls')
            print()
            print_board()
            print("Draw")
            flag = False

    print("Thanks for playing!")


main()
