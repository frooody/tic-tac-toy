from cgi import test
from IPython.display import clear_output
import random

print('Dear SOKOL! Welcome to Tic Tac Toe!')
print('The first turn is by X! Have a good game boyz and girlz...\n')

test_board = [' '] * 10

def display_nums_board():
    clear_output()
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('—————————')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('—————————')
    print('7' + ' | ' + '8' + ' | ' + '9')

def display_board(board):
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('—————————')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('—————————')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if (board[1] + board[2] + board[3]) == mark * 3:
        return True
    elif (board[4] + board[5] + board[6]) == mark * 3:
        return True
    elif (board[7] + board[8] + board[9]) == mark * 3:
        return True
    elif (board[1] + board[4] + board[7]) == mark * 3:
        return True
    elif (board[2] + board[5] + board[8]) == mark * 3:
        return True
    elif (board[3] + board[6] + board[9]) == mark * 3:
        return True
    elif (board[1] + board[5] + board[9]) == mark * 3:
        return True
    elif (board[3] + board[5] + board[7]) == mark * 3:
        return True

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False
def full_board_check(board):
    count = 0
    for i in range(len(board)):
        if board[i] == 'X' or board[i] == 'O':
            count += 1
        else:
            continue
    if count == 9:
        return True
    else: 
        return False

def x_move(board):
    while True:
        position = int(input('Type the number where should be X is: '))
        if space_check(board, position):
            board[position] = 'X'
            break
        else:
            print('The cell is already busy! Try another!')
def o_move(board):
    while True:
        position = int(input('Type the number where should be O is: '))
        if space_check(board, position):
            board[position] = 'O'
            break
        else:
            print('The cell is already busy! Try another!')
def replay():
    question = input('If you want to continue play press Y else press N: ')
    if question == 'Y':
        global test_board
        test_board = [' '] * 10
        return True
    else:
        return False

while True:
    print('There is what cell is what number! \n')
    display_nums_board()
    print()
    for i in range(0, 4):
        x_move(test_board)
        print()
        display_board(test_board)
        if win_check(test_board, 'X'):
            print('X is WON!!!')
            break
        print()
        o_move(test_board)
        print()
        display_board(test_board)
        if win_check(test_board, 'O'):
            print('The winner - O!!!')
            break
        print()
    if not win_check(test_board, 'X') and not win_check(test_board, 'O'):
        x_move(test_board)
        print()
        display_board(test_board)
        win_check(test_board, 'X')
        print()
    if not replay():
        break