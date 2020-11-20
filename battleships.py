# X - patrol boat
# XX - Destroyer
# XXX - Carrier
# O - empty cell

import sys
import random
import os
import string

def init_player_1_board(board_dimension):
    player_1_board = []
    row = []
    for columns_iteration_counter in range(0,board_dimension):
        row.append('O')
    for rows_iteration_counter in range(0,board_dimension):
        player_1_board.append(row)
    return player_1_board


def init_player_2_board(board_dimension):
    player_2_board = []
    row = []
    for columns_iteration_counter in range(0,board_dimension):
        row.append('O')
    for rows_iteration_counter in range(0,board_dimension):
        player_2_board.append(row)
    return player_2_board


''' ship_type_number :
1: Patrol Ship
2: Patrol Ship
3: Destroyer
4: Destroyer
5: Aircraft carrier
'''
def get_placement_coordinates(ship_type_number, ship_types):
    if ship_type_number == 0 or ship_type_number == 1:
        ship_type = ship_types[0]
    elif ship_type_number == 2 or ship_type_number == 3:
        ship_type = ship_types[1]
    elif ship_type_number == 4:
        ship_type = ship_types[2]

    if ship_type == ship_types[0]:
        print(f'Provide coordinate for {(ship_type_number + 1)} {ship_types[0]}')
        coordinates_given_by_user = input()
        return coordinates_given_by_user
    if ship_type == ship_types[1]:
        print(f'Provide orientation (h: horizontal, v: vertical) and first coordinate for {(ship_type_number - 1)} {ship_types[1]}')
        coordinates_given_by_user = input()
        return coordinates_given_by_user
    if ship_type == ship_types[2]:
        print(f'Provide orientation (h: horizontal, v: vertical) and first coordinate for {ship_types[2]}')
        coordinates_given_by_user = input()
        return coordinates_given_by_user


def mark_ship_on_board():
    pass


# checks wheater coordinates input is correct, if its not out of range or if ships are not too close from eachother
# returns 'coord_valid' if coordinates valid
# returns 'too_close' if ships too close
# returns 'out_of_range' if coordinates out of range 
# else returns 'invalid_input'
def check_if_coordinates_valid(coordinates_given_by_user, player_1_board, player_2_board):
    pass


def print_player_1_board(board_dimension, player_1_board):
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')
    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(player_1_board[i][j] + ' ', end=' ')
        print('\n')


def print_player_2_board(board_dimension, player_2_board):
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')
    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(player_2_board[i][j] + ' ', end=' ')
        print('\n')


def implacement_phase(board_dimension):
    ship_types = ['Patrol Ship (1 cell: < X >)"', 'Destroyer (2 cells: < XX >):', 'Aircraft carrier (3 cells: < XXX >):']

    player_1_board = init_player_1_board(board_dimension)
    player_2_board = init_player_2_board(board_dimension)
    implacement_phase_player_1(ship_types, board_dimension, player_1_board)
    implacement_phase_player_2(ship_types, board_dimension, player_2_board)

def implacement_phase_player_1(ship_types, board_dimension, player_1_board):
    print_player_1_board(board_dimension, player_1_board)
    for ship_type_number in range(0,5):
        get_placement_coordinates(ship_type_number, ship_types)

def implacement_phase_player_2(ship_types, board_dimension, player_2_board):
    print_player_2_board(board_dimension, player_2_board)
    for ship_type_number in range(0,5):
        get_placement_coordinates(ship_type_number, ship_types)


def shooting_phase():
    pass

def print_both_boards(board_dimension, player_1_board, player_2_board):
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('          ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')

    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(player_1_board[i][j] + ' ', end=' ')
        print('      ', end='')
        print(rows_letters[i] + '  ', end=' ')
        
        for j in range(0,board_dimension):
            print(player_2_board[i][j] + ' ', end=' ')
        print('\n')





# MAIN GAME LOOP
# implacement_phase()
board_dimension = 7
player_1_board = init_player_1_board(board_dimension)
player_2_board = init_player_2_board(board_dimension)
implacement_phase(board_dimension)