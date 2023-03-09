"""Name:Piyush Phuyal
   Student ID:2330536
   Class Group:L4CG2(2022/23)
   College ID:np03cs4a220258@heraldcollege.edu.np"""
import random
import json                 #JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
random.seed()
board = [[" " for x in range(3)] for y in range(3)]

def draw_board(board):
    print(" ----------")
    print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))   
     #.format method is used here to print tic-tac-toe board where values are inserted into the string
     # takes values from first row of the board and puts them into string between curly brackets
    print(" ----------")
    print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print(" ----------")
    print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print(" ----------")

def welcome(board):
    print("Welcome to Tic Tac Toe!")
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
         board[i][j] = " "
    return board

def get_player_move(board):
    print('''Putting 1 for row 
    and 1 for col represents 
    first row and first column 
    like of Matrix''')
    row = int(input("Enter row in matrix format for 'X'(1, 2, or 3): ")) - 1
    col = int(input("Enter col in matrix format for 'X' (1, 2, or 3): ")) - 1
    while row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
        print('''Hey! 
        You didn't get matrix! 
        Its your invalid move!!!''')
        print('''Putting 1 for row 
        and 1 for col represents 
        first row and first column 
        like of Matrix''')
        row = int(input("Enter row in matrix format for 'X'(1, 2, or 3): ")) - 1
        col = int(input("Enter col in matrix format for 'X' (1, 2, or 3): ")) - 1
    board[row][col] = "X"
    return row, col

def choose_computer_move(board):
    row = random.randint(0, 2)  #random.randint is a function in Python's random module that returns a random integer between two specified numbers
    col = random.randint(0, 2)
    while board[row][col] != " ":
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = "O"
    return row, col

def check_for_win(board, mark):
    # check rows
 while True:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You won! Hurray!!!") 
            return 1
        if check_for_draw(board):
            print("Draw!!!")
            return 0
        choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Opps! you lost!")
            return -1
        if check_for_draw(board):
            print("Draw!!!")
            return 0   
        
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt'")
    print("q - End the program")
    choice =input("Enter your choice: ")
    if (choice == "1" or choice == "2" or choice == "3" or choice == "q"):
     return choice
    else:
     print("Invalid input!!! please type 1,2,3 or q for getting respective results.") 

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    f=open("leaderboard.txt","r")
    leaders=f.read()
    return leaders

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name = input("Please enter your name: ")
    try:
        with open("leaderboard.txt", "r") as f:
            leader_board = json.load(f)    #json.load reads a JSON string from a file object and converts it into a Python object (such as a dictionary or a list).
    except FileNotFoundError:        # If the file doesn't exist we use the default filenotFoundError handler
        leader_board = {}
    leader_board[name] = score
    with open("leaderboard.txt", "w") as f:
        json.dump(leader_board, f)          #json.dump converts a Python object into a JSON string and writes it to a file object.

def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print(f"Leaderboard Scores:\n{leaders}")
