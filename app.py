from os import system
from art import logo
from icecream import ic

board = ["_","_","_","_","_","_"," "," "," "] # main board
positions = ["1","2","3","4","5","6","7","8","9"] # explaination board
player1 = ""
player2 = ""
current_player = "" 
replay_last_move = False

def welcome():
    """Prints wellcom screen."""
    print(logo)
    print("Let's play X-O! \nUse the squares numbers to choose which square you want: \n")
    print(positions[0] + "|" + positions[1] + "|" + positions[2] + "\n-----" + '\n' + positions[3] + "|" + positions[4] + "|" +
       positions[5] + "\n-----" + '\n' + positions[6] + "|" + positions[7] + "|" + positions[8])
    

def draw_board():
    """Draws the board."""
    print(board[0] + "|" + board[1] + "|" + board[2]+ '\n' + board[3] + "|" + board[4] + "|" +
       board[5] + '\n' + board[6] + "|" + board[7] + "|" + board[8])

def selection():
    """Sets which player playes with X and who playes with O"""
    global player1,player2
    selection = input("Player 1 choose X or O: ")
    if selection.lower() == "x":
        player1 = "X"
        player2 = "O"
    elif selection.lower() == "o":
        player1 = "O"
        player2 = "X"
    else: print("choose only 'x' or 'y' ")
           
def check_win():
    """Check if there's a win and returns the player who won."""
    winner = ""
    nothing = ""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != " " and board[i] != "_":
            if board[i] == "X": winner = "Player1"
            else: winner = "Player2"
            return True, winner

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != " " and board[i] != "_":
            if board[i] == "X": winner = "Player1"
            else: winner = "Player2"
            return True, winner

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " " and board[i] != "_":
        if board[i] == "X": winner = "Player1"
        else: winner = "Player2"
        return True, winner
    if board[2] == board[4] == board[6] and board[2] != " " and board[i] != "_":
                if board[i] == "X": winner = "Player1"
                else: winner = "Player2"
                return True, winner

    return False, nothing

def check_taken(square):
     """Check's if a square is taken, returns true/false."""
     if board[square] == "X" or board[square] == "O":
         return True
     else: return False
         
def set_square(player):
    """Checks whom's turn is it and adds player selection to board."""
    global current_player, replay_last_move
    
    if replay_last_move:
        replay_last_move = False
    else:
        if current_player == "Player1":
                current_player = "Player2"
        elif current_player == "":
            current_player = "Player1"
        else: current_player = "Player1"
    square = int(input(f"{current_player}'s turn. Choose a square: ")) - 1
    if 0 <= square <= 8:
        # Check if the square is not taken
        if not check_taken(square):
            board[square] = player
        else:
            print("Square is taken. Choose again.")
            # Keep the same player's turn if the square is taken
            replay_last_move = True
            set_square(player)
    else:
        print("Choose a square number from 1 to 9 starting from the top left to the right.")
        set_square(player)



def play_game(player1, player2, draw_board, check_win, set_square):
    """Main loop for the game."""
    moves_left = 9
    while True:
        system('clear')
        draw_board()
        set_square(player1)
        draw_board()
        win , winner = check_win()
        moves_left -=1
        if win:
            print(f'{winner} won!')
            break
        elif moves_left == 0:
            print("It's a draw!")
            break
        else:
            set_square(player2)
            draw_board()
            win , winner = check_win()
            moves_left -=1
            if win: 
                print(f'{winner} won!')
                break



keep_playing = True

while keep_playing:
     system('clear')
     current_player = ""
     welcome()
     selection() 
     play_game(player1, player2, draw_board, check_win, set_square)
     continue_playing = input('Play again? Type "y" or "n":  ').lower()
     board = ["_","_","_","_","_","_"," "," "," "]

     if continue_playing == "n":
          ic("Bye!")
          break






