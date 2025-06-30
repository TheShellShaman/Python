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

print(display_board(board))


def enter_move(board):
    move = input(("What is your move?"))
    for row in board:
        for cell in row:
            if move == cell:
                board[cell] = move


def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
    free_squares = []
    for row in range(3):
        for col in range(3):
            square = board[row][col]
    if square not in ("X", "O"):
        free_squares.append(row, col)

    print(free_squares)

def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
    for row in range(3):
        for col in range(3):
            square = board[row][col]
        
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.
