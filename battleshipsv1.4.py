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


def put_ship_on_board(board, valid_coordinates):
    pass

        
''' ship_type_number :
1: Patrol Ship
2: Patrol Ship
3: Destroyer
4: Destroyer
5: Aircraft carrier
'''
def mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board_copy, coordinates, ship_type_number, list_of_forbidden_coordinates):
    row = coordinates[1]
    col = coordinates[2]
    if ship_type_number == 0 or ship_type_number == 1:
        #postaw statek, wyklucz zabronione przezeń pola
        if (row, col) in list_of_forbidden_coordinates:
            return 'too_close'
        board_copy[coordinates[1]][coordinates[2]] = 'X'
        list_of_forbidden_coordinates.append((row, col))
        list_of_forbidden_coordinates.append((row -1, col))
        list_of_forbidden_coordinates.append((row +1, col))
        list_of_forbidden_coordinates.append((row, col -1))
        list_of_forbidden_coordinates.append((row, col +1))
    if ship_type_number == 2 or ship_type_number == 3:
        #postaw statek, zrób kropki, jeśli za blisko - error
        if coordinates[0] != 'h' and coordinates [0] != 'v':
            raise
        if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates or (row, col+1) in list_of_forbidden_coordinates:
            return 'too_close'
        if coordinates[0] == 'h':
            board_copy[row][col] = 'X'
            board_copy[row][col+1] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, col-1))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((row-1, col))
            list_of_forbidden_coordinates.append((row-1, col+1))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+1, col+1))
        elif coordinates[0] == 'v':
            board_copy[row][col] = 'X'
            board_copy[row+1][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row-1, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((row+1, col-1))
            list_of_forbidden_coordinates.append((row, col-1))
        
    if ship_type_number == 4:
        #postaw statek, zrób kropki, jeśli za blisko - error
        if coordinates[0] != 'h' and coordinates [0] != 'v':
            raise
        if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates or (row+2, col in list_of_forbidden_coordinates) or (row, col+1) in list_of_forbidden_coordinates or (row, col+2) in list_of_forbidden_coordinates:
            return 'too_close'
        if coordinates[0] == 'h':
            board_copy[row][col] = 'X'
            board_copy[row][col+1] = 'X'
            board_copy[row][col+2] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((row, col-1))
            list_of_forbidden_coordinates.append((row-1, col))
            list_of_forbidden_coordinates.append((row-1, col+1))
            list_of_forbidden_coordinates.append((row-1, col+2))
            list_of_forbidden_coordinates.append((row, col+3))
            list_of_forbidden_coordinates.append((row+1, col+2))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+1, col))
        elif coordinates[0] == 'v':
            board_copy[row][col] = 'X'
            board_copy[row+1][col] = 'X'
            board_copy[row+2][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((row-1, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col+1))
            list_of_forbidden_coordinates.append((row+3, col))
            list_of_forbidden_coordinates.append((row+2, col-1))
            list_of_forbidden_coordinates.append((row+1, col-1))
            list_of_forbidden_coordinates.append((row, col-1))
        


def make_coordinates_from_user_input(coordinates_given_by_user, board_dimension):
    rows_letters = list(string.ascii_lowercase)[:board_dimension]
    coordinates_given_by_user = coordinates_given_by_user.lower()
    coordinates_given_by_user_list = []
    for i in coordinates_given_by_user:
        coordinates_given_by_user_list.append(i)
    #tu musi być warunek, żeby koordynaty nie przekraczały wielkości tablicy
    # jeśli przekraczają to raise error

    if len(coordinates_given_by_user_list) == 2:
        for i in range(len(rows_letters)):
            if coordinates_given_by_user_list[0] == rows_letters[i]:
                row = int((i))
        if int(coordinates_given_by_user_list[1]) > board_dimension or int(coordinates_given_by_user_list[1]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[1]) - 1
        orient = ''
        return (orient, row, col)

    elif len(coordinates_given_by_user_list) == 3:
        for i in range(len(rows_letters)):
            if coordinates_given_by_user_list[1] == rows_letters[i]:
                row = int((i))
        if int(coordinates_given_by_user_list[2]) > board_dimension or int(coordinates_given_by_user_list[2]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[2]) - 1
        orient = coordinates_given_by_user_list[0]
        if orient != 'h' and orient != 'v':
            raise
        return (orient, row, col)

        
# checks wheater coordinates input is correct, if its not out of range or if ships are not too close from eachother
# returns 'invalid_input' if coordinates out of range 
# returns 'too_close' if ships too close
# returns 'coord_valid' if coordinates valid
# else returns 'invalid_input'
def check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board_copy, board_dimension, ship_type_number, list_of_forbidden_coordinates):
    invalid_input = 'INVALID INPUT'
    too_close = 'SHIPS TOO CLOSE'
    coord_valid = 'coord_valid'
    rows_letters = list(string.ascii_lowercase)[:board_dimension]
    board = board_copy


    #najpierw sprawdz czy jest 2 lub 3 charaktery
    if len(coordinates_given_by_user) != 2 and len(coordinates_given_by_user) != 3:
        return invalid_input
    
    #przerób na poprawne tuple z coordynatami odpowiadającymi wielkości tablicy itd, 
    # , wstaw nic w przypadku pierwszego znaku inputa przy patrol boat
    try:
        coordinates = make_coordinates_from_user_input(coordinates_given_by_user, board_dimension)
    except:
        return invalid_input
    
    # już w zależności od h lub v sprawdź czy te coordynaty są wolne,mozliwe
    #w zależności od statku po prostu stawiaj na kopii tablicy
    try:
        is_not_too_close = mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board_copy, coordinates, ship_type_number, list_of_forbidden_coordinates)
    except:
        return invalid_input
    if is_not_too_close == 'too_close':
        return too_close
    
    return coord_valid
    

def get_placement_coordinates(ship_type_number, ship_types, board_copy, list_of_forbidden_coordinates):
    checking_result_of_user_input = ()

    if ship_type_number == 0 or ship_type_number == 1:
        while not checking_result_of_user_input == 'coord_valid':      
            print(f'Provide coordinate for {(ship_type_number + 1)} {ship_types[0]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board_copy, board_dimension, ship_type_number, list_of_forbidden_coordinates)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension)
    if ship_type_number == 2 or ship_type_number == 3:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation (h: horizontal, v: vertical) and first coordinate for {(ship_type_number - 1)} {ship_types[1]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board_copy, board_dimension, ship_type_number, list_of_forbidden_coordinates)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension)
    if ship_type_number == 4:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation (h: horizontal, v: vertical) and first coordinate for {ship_types[2]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board_copy, board_dimension, ship_type_number, list_of_forbidden_coordinates)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension)   

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


def implacement_phase_pl_vs_pl(board_dimension):
    ship_types = ['Patrol Ship (1 cell: < X >)', 'Destroyer (2 cells: < XX >):', 'Aircraft carrier (3 cells: < XXX >):']

    player_1_board = init_player_1_board(board_dimension)
    player_2_board = init_player_2_board(board_dimension)
    implacement_phase_player_1(ship_types, board_dimension, player_1_board)
    implacement_phase_player_2(ship_types, board_dimension, player_2_board)

def implacement_phase_player_1(ship_types, board_dimension, player_1_board):
    print_player_1_board(board_dimension, player_1_board)
    list_of_forbidden_coordinates = []
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, player_1_board, list_of_forbidden_coordinates)
        put_ship_on_board(player_1_board, valid_coordinates)

def implacement_phase_player_2(ship_types, board_dimension, player_2_board):
    print_player_2_board(board_dimension, player_2_board)
    list_of_forbidden_coordinates = []
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, player_2_board, list_of_forbidden_coordinates)
        put_ship_on_board(player_2_board, valid_coordinates)

def implacement_phase_cpu():
    pass


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
implacement_phase_pl_vs_pl(board_dimension)