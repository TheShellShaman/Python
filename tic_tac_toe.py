import random
from random import randrange

board = [
    [1,2,3],
    [4,"X",6],
    [7,8,9]
]

def display_board(board):
    for i in range(len(board)):
        row = board[i]
        print("+-------+-------+-------+\n")
        print("|       |       |       |\n")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |\n")
        print("|       |       |       |\n")
    print("+-------+-------+-------+\n")




def enter_move(board):
    
    while True:
        try: move = int(input(("What is your move?:  ")))

        except ValueError:
            print("Please enter a number thats available on the board")
            continue
        
        for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = 'O'
                        return
        print("That square is already taken or doesn't exist. Try again")

def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
    global free_squares
    free_squares = []
    for row in range(3):
        for col in range(3):
            square = board[row][col]
            if square not in ("X", "O"):
                free_squares.append((row, col))

    print(f"The free squares are \n{free_squares}\n")

def victory_for(board):
#     # The function analyzes the board's status 
    global square 
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
            
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
        
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def draw_move(board):
# The function draws the computer's move and updates the board.
    row, col = random.choice(free_squares)
    board[row][col] = 'X'

while True:
    display_board(board)
    enter_move(board)
    make_list_of_free_fields(board)
    draw_move(board)
    winner = victory_for(board)
    make_list_of_free_fields(board)
    if winner:
        print(f"{winner} has won the match!")
        break
    if not free_squares:
        print("Cats game xD")
        break


