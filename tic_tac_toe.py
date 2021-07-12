import sys
import random

def menu():
    menu =""""
         MENU
==================================
    1. Play with other player
    2. Play with AI
    3. Quit

    """
    print(menu)
    while True:
        game_option = input('Which mode do You prefer ? : ').lower()
        if game_option in {'1','2'}:
            return game_option
        elif game_option == 'quit':
            sys.exit(0) 
    

def init_board():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board
       
def print_board(board):
    print("   1   2   3 ")
    print("A  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  ---+---+---")
    print("B  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print("C  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def first_turn():
    who_has_move = random.randint(0,1)
    return who_has_move

def ai_move(board,game_option,sign,whose_move):
    if game_option == '2':
        while True:
            if whose_move%2 == 0:
                sign = 'O'
            else:
                sign = 'X'
            coordinates =(random.randint(0,2),random.randint(0,2))
            if board[coordinates[0]][coordinates[1]] =='.':
               board[coordinates[0]][coordinates[1]] = sign
               return False
        
def player_choice():
    flag = True
    while flag:
        player_choice = input("Input Your choice : ").lower()
        if len(player_choice)==2 and player_choice[0] in {'a','b','c'} and player_choice[1] in {'1','2','3'}:
            flag = False
        elif player_choice == 'quit':
            print("Thank You for playing game....Bye..Bye..")
            sys.exit(0)
    return player_choice

def converter(player_choice):
    if player_choice[0] == 'a':
        x = 0;
    elif player_choice[0] == 'b':
        x = 1;
    else:
        x = 2;
    y = int(player_choice[1])-1
    return x,y

def move_changer(whose_move):
    if whose_move%2 == 0:
       sign = 'X'
    else:
        sign = 'O'
    whose_move+=1
    return sign

def move_one_the_board(board,coordinates,sign):
        if board[coordinates[0]][coordinates[1]] =='.':
           board[coordinates[0]][coordinates[1]] = sign
           return False
        else:
            return True
 
def board_is_full(board):
    counter = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] != '.':
                counter+=1
    if counter == 9:
        return True

def end_game(draw,winner):
    if winner != None:
        print(f"Congratulation {winner}, You won the game !!!")
        print_board(board)
        sys.exit(0)
    if draw == True:
        print("Sorry no more space, We have draw !!!")
        print_board(board)
        sys.exit(0)

def who_won(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0]!='.':
       return board[0][0]
    elif board [1][0] == board[1][1] == board[1][2] and board[1][0]!='.':
        return board[1][0]
    elif board [2][0] == board[2][1] == board[2][2] and board[2][0]!='.' :
        return board[2][0]  
    elif board [0][0] == board[1][0] == board[2][0] and board[0][0]!='.':
        return board[0][0]
    elif board [0][1] == board[1][1] == board[2][1] and board[0][1]!='.':
        return  board[0][1]
    elif board [0][2] == board[1][2] == board[2][2] and board[0][2]!='.':
        return board[0][2]
    elif board [0][0] == board[1][1] == board[2][2] and board[0][0]!='.':
        return board[0][0]
    elif board [2][0] == board[1][1] == board[0][2] and board[2][0]!='.':
        return board[2][0]
           
if __name__ == '__main__':
    game_option = menu()
    board = []
    board = init_board()
    if game_option == '1':
        print_board(board)
    whose_move = first_turn()
    while True: 
        sign = move_changer(whose_move)
        check_if_empty = True
        ai_move(board,game_option,sign,whose_move)
        winner = who_won(board)
        draw = board_is_full(board)
        end_game(draw,winner)
        if game_option == '2':
            print_board(board)
        while check_if_empty:
            choice = player_choice()
            coordinates = converter(choice)
            check_if_empty = move_one_the_board(board,coordinates,sign)     
        if game_option =='1':
            print_board(board)     
        winner = who_won(board)
        draw = board_is_full(board)
        end_game(draw,winner)
        if game_option == '1':
            whose_move+=1

       