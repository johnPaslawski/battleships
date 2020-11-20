# X - patrol boat
# XX - Destroyer
# XXX - Carrier
# O - empty cell


import sys
import random
import os
import string


def init_player_board(board_dimension):
    board = [['0'] * board_dimension for _ in range(board_dimension)]
    return board


def put_ship_on_board(board, valid_coordinates, ship_type_number):
    pass
    orient = valid_coordinates[0]
    row = valid_coordinates[1]
    col = valid_coordinates[2]

    if ship_type_number == 0 or ship_type_number == 1:
        board[row][col] = 'X'
    
    if ship_type_number == 2 or ship_type_number == 3:
        if orient == 'V':
            board[row][col] = 'X'
            board[row+1][col] = 'X'
        elif orient == 'H':
            board[row][col] = 'X'
            board[row][col+1] = 'X'

    if ship_type_number == 4:
        if orient == 'V':
            board[row][col] = 'X'
            board[row+1][col] = 'X'
            board[row+2][col] = 'X'
        elif orient == 'H':
            board[row][col] = 'X'
            board[row][col+1] = 'X'
            board[row][col+2]
        
''' ship_type_number :
1: Patrol Ship
2: Patrol Ship
3: Destroyer
4: Destroyer
5: Aircraft carrier
'''
def mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board, coordinates, ship_type_number, list_of_forbidden_coordinates):
    row = coordinates[1]
    col = coordinates[2]
    if ship_type_number == 0 or ship_type_number == 1:
        #postaw statek, wyklucz zabronione przezeń pola
        if (row, col) in list_of_forbidden_coordinates:
            return 'too_close'
        board[row][col] = 'X'
        list_of_forbidden_coordinates.append((row, col))
        list_of_forbidden_coordinates.append((abs(row -1), col))
        list_of_forbidden_coordinates.append((row +1, col))
        list_of_forbidden_coordinates.append((row, abs(col -1)))
        list_of_forbidden_coordinates.append((row, col +1))
    
    if ship_type_number == 2 or ship_type_number == 3:
        #postaw statek, zrób kropki, jeśli za blisko - error
        if coordinates[0] != 'H' and coordinates [0] != 'V':
            raise
        if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates or (row, col+1) in list_of_forbidden_coordinates:
            return 'too_close'
        if coordinates[0] == 'H':
            board[row][col] = 'X'
            board[row][col+1] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((abs(row-1), col+1))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+1, col+1))
        elif coordinates[0] == 'V':
            board[row][col] = 'X'
            board[row+1][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((row+1, abs(col-1)))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
        
    if ship_type_number == 4:
        #postaw statek, zrób kropki, jeśli za blisko - error
        if coordinates[0] != 'H' and coordinates [0] != 'V':
            raise
        if (row, col) in list_of_forbidden_coordinates or (row+1, col) in list_of_forbidden_coordinates or (row+2, col) in list_of_forbidden_coordinates or (row, col+1) in list_of_forbidden_coordinates or (row, col+2) in list_of_forbidden_coordinates:
            return 'too_close'
        if coordinates[0] == 'H':
            board[row][col] = 'X'
            board[row][col+1] = 'X'
            board[row][col+2] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row, col+2))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((abs(row-1), col+1))
            list_of_forbidden_coordinates.append((abs(row-1), col+2))
            list_of_forbidden_coordinates.append((row, col+3))
            list_of_forbidden_coordinates.append((row+1, col+2))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+1, col))
        elif coordinates[0] == 'V':
            board[row][col] = 'X'
            board[row+1][col] = 'X'
            board[row+2][col] = 'X'
            list_of_forbidden_coordinates.append((row, col))
            list_of_forbidden_coordinates.append((row+1, col))
            list_of_forbidden_coordinates.append((row+2, col))
            list_of_forbidden_coordinates.append((abs(row-1), col))
            list_of_forbidden_coordinates.append((row, col+1))
            list_of_forbidden_coordinates.append((row+1, col+1))
            list_of_forbidden_coordinates.append((row+2, col+1))
            list_of_forbidden_coordinates.append((row+3, col))
            list_of_forbidden_coordinates.append((row+2, abs(col-1)))
            list_of_forbidden_coordinates.append((row+1, abs(col-1)))
            list_of_forbidden_coordinates.append((row, abs(col-1)))
        


def make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters):
    coordinates_given_by_user = coordinates_given_by_user.upper()
    coordinates_given_by_user_list = []
    for i in coordinates_given_by_user:
        coordinates_given_by_user_list.append(i)
    #tu musi być warunek, żeby koordynaty nie przekraczały wielkości tablicy
    # jeśli przekraczają to raise error

    if len(coordinates_given_by_user_list) == 2:
        for rows_iteration_counter_2 in range(len(rows_letters)):
            if coordinates_given_by_user_list[0] == rows_letters[rows_iteration_counter_2]:
                row = int(rows_iteration_counter_2)
                break
        if int(coordinates_given_by_user_list[1]) > board_dimension or int(coordinates_given_by_user_list[1]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[1]) - 1
        orient = ''
        return (orient, row, col)

    elif len(coordinates_given_by_user_list) == 3:
        for rows_iteration_counter_3 in range(len(rows_letters)):
            if coordinates_given_by_user_list[1] == rows_letters[rows_iteration_counter_3]:
                row = int(rows_iteration_counter_3)
                break
        if int(coordinates_given_by_user_list[2]) > board_dimension or int(coordinates_given_by_user_list[2]) <= 0:
            raise
        col = int(coordinates_given_by_user_list[2]) - 1
        orient = coordinates_given_by_user_list[0]
        if orient != 'H' and orient != 'V':
            raise
        return (orient, row, col)

        
# checks wheater coordinates input is correct, if its not out of range or if ships are not too close from eachother
# returns 'invalid_input' if coordinates out of range 
# returns 'too_close' if ships too close
# returns 'coord_valid' if coordinates valid
# else returns 'invalid_input'
def check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters):
    invalid_input = 'INVALID INPUT'
    too_close = 'SHIPS TOO CLOSE'
    coord_valid = 'coord_valid'
    
    #najpierw sprawdz czy jest 2 lub 3 charaktery
    if len(coordinates_given_by_user) != 2 and len(coordinates_given_by_user) != 3:
        return invalid_input
    
    #przerób na poprawne tuple z coordynatami odpowiadającymi wielkości tablicy itd, 
    # , wstaw nic w przypadku pierwszego znaku inputa przy patrol boat
    try:
        coordinates = make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters) 
    except:
        return invalid_input
    # już w zależności od h lub v sprawdź czy te coordynaty są wolne,mozliwe
    #w zależności od statku po prostu stawiaj na kopii tablicy
    try:
        is_not_too_close = mark_occupied_and_forbidden_fields_on_board_in_placement_phase(board, coordinates, ship_type_number, list_of_forbidden_coordinates)
    except:
        return invalid_input


    if is_not_too_close == 'too_close':
        return too_close
    
    return coord_valid
    

def get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, player_1_board):
    checking_result_of_user_input = ()
    board = player_1_board
    
    if ship_type_number == 0 or ship_type_number == 1:
        while not checking_result_of_user_input == 'coord_valid':      
            print(f'Provide coordinate for {(ship_type_number + 1)} {ship_types[0]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
    
    if ship_type_number == 2 or ship_type_number == 3:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation(h: horizontal, v: vertical) and coordinates for {(ship_type_number - 1)} {ship_types[1]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)
    
    if ship_type_number == 4:
        while not checking_result_of_user_input == 'coord_valid':
            print(f'Provide orientation(h: horizontal, v: vertical) and coordinates for {ship_types[2]}')
            coordinates_given_by_user = str(input())
            checking_result_of_user_input = check_if_coordinates_valid_implacement_phase(coordinates_given_by_user, player_1_board, board_dimension, ship_type_number, list_of_forbidden_coordinates, rows_letters)
            if not checking_result_of_user_input == 'coord_valid': print(checking_result_of_user_input)
        return make_coordinates_from_user_input(coordinates_given_by_user, board_dimension, rows_letters)   


def print_player_board(board_dimension, board, rows_letters):
    print('    ', end='')
    for k in range(0,board_dimension):
        print(str(k+1) + '  ', end='')
    print('\n')
    for i in range(0,board_dimension):
        print(rows_letters[i] + '  ', end=' ')
        for j in range(0,board_dimension):
            print(board[i][j] + ' ', end=' ')
        print('\n')
    pass


def implacement_phase_pl_vs_pl(board_dimension):
    ship_types = ['Patrol Ship (1 cell: < X >)', 'Destroyer (2 cells: < XX >):', 'Aircraft carrier (3 cells: < XXX >):']
    list_of_forbidden_coordinates = []
    rows_letters = list(string.ascii_uppercase)[:board_dimension]
    
    implacement_phase_player_1(ship_types, list_of_forbidden_coordinates, rows_letters)
    implacement_phase_player_2(ship_types, list_of_forbidden_coordinates, rows_letters)

def implacement_phase_player_1(ship_types, list_of_forbidden_coordinates, rows_letters):
    player_1_board = init_player_board(board_dimension)
    print_player_board(board_dimension, player_1_board, rows_letters)
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, player_1_board)
        put_ship_on_board(player_1_board, valid_coordinates, ship_type_number)
        print_player_board(board_dimension, player_1_board, rows_letters)

def implacement_phase_player_2(ship_types, list_of_forbidden_coordinates, rows_letters):
    player_2_board = init_player_board(board_dimension)
    print_player_board(board_dimension, player_2_board, rows_letters)
    for ship_type_number in range(0,5):
        valid_coordinates = get_placement_coordinates(ship_type_number, ship_types, list_of_forbidden_coordinates, rows_letters, player_2_board)
        put_ship_on_board(player_2_board, valid_coordinates, ship_type_number)
        print_player_board(board_dimension, player_2_board, rows_letters)

def implacement_phase_cpu():
    pass


def shooting_phase():
    pass


def print_both_boards(board_dimension, player_1_board, player_2_board):
    pass
    '''rows_letters = list(string.ascii_uppercase)[:board_dimension]
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
        print('\n')'''





# MAIN GAME LOOP
# implacement_phase()
board_dimension = 7
implacement_phase_pl_vs_pl(board_dimension)