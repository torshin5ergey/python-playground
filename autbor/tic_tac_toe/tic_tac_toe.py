"""
tic_tac_toe.py - Tic Tac Toe Game

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""


from random import choice

# Game board
board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM':
' ', 'midR': ' ', 'botL': ' ', 'botM': ' ', 'botR': ' '}

# Print the contents of a board represented as a dictionary
def print_board(board: dict) -> None:
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['botL'] + '|' + board['botM'] + '|' + board['botR'])

# Print a formatted grid of coordinates
def print_coordinates_format():
    print(
'''topL|topM|topR
----+----+----
midL|midM|midR
----+----+----
botL|botM|botR''')

# Print "How to play" message
def how_to_play() -> None:
    print('''\nHow to play\n'''
          '''1. When it's your turn, simply specify the coordinate where you want to place your mark. For example, "topL" corresponds to the top-left corner, "midM" - the middle in the middle, and so on.\n'''
          '''Coordinates are in accordance with the field below:\n''')
    print_coordinates_format()
    print('''\n2. The first player plays as "O", and the second player plays as "X"\n'''
          '''3. The player who first fills a row, column, or diagonal with their marks wins.''')

# Choose game mode: one or two players
def choose_from_menu() -> int:
    print('Game menu:')
    while True:
        try:
            mode = int(input('0. How To Play?\n1. One Player (PvE)\n2. Two Players (PvP)\nChoose the option (0/1/2): '))
            if mode not in (0, 1, 2):
                raise ValueError
            break
        except ValueError:
            print('\nError! Choose 1 or 2')
    return mode

# Prompt the player for their move and return the formatted move
def player_turn() -> str:
    while True:
        move = input().strip()
        # Format user input according to coordinates values
        formatted_move = move[:-1].lower() + move[-1].upper()
        if (formatted_move) in board.keys():
            if board[formatted_move] == ' ':
                return formatted_move
            else:
                print("This space isn't empy.")
        else:
            print('Error! Coordinates must be entered in accordance with the field below:')
            print_coordinates_format()
        print(f'Try again. Move on which space?')

# Generate a random move for the computer from the available moves
def computer_random_move(moves: list) -> str:
    random_move = choice(moves) # random.choice()
    moves.remove(random_move)
    return random_move

# Single-player game versus the computer
def one_player() -> None:
    available_moves = ['topL', 'topM', 'topR', 'midL', 'midM', 'midR', 'botL', 'botM', 'botR']
    print()
    turn = 'O'
    for _ in range(9): # Game loop
        print_board(board)
        print()
        if turn == 'O':
            move = computer_random_move(available_moves)
            print(f"Computer's move is {move}")
        else: 
            print(f'Your turn. Move {turn} on which space?')
            move = player_turn()
            available_moves.remove(move)
        board[move] = turn
        
        if is_win():
            print_board(board)
            if turn == 'O':
                print(f'You beat the computer! Congratulation!')
            else:
                print(f'Computer beat you!')
            return
        
        # Change player
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'
    print_board(board)
    print('You tied.')
    return

# Check if there's a winner    
def is_win() -> bool:
    # Check win condition for rows
    for row in ['top', 'mid', 'bot']:
        if board[row+'L'] != ' ' and board[row+'L'] == board[row+'M'] == board[row+'R']:
            return True
    # Check win condition for cols
    for col in ['L', 'M', 'R']:
        if board['top'+col] != ' ' and board['top'+col] == board['mid'+col] == board['bot'+col]:
            return True   
    # Check win condition for diagonals
    if board['topL'] != ' ' and board['topL'] == board['midM'] == board['botR']:
        return True
    if board['topR'] != ' ' and board['topR'] == board['midM'] == board['botL']:
        return True
    return False

# Two-player game. PLayer versus player
def two_players() -> None:
    print()
    turn = 'O'
    for _ in range(9): # Game loop
        print_board(board)
        print()
        print(f'Turn for {turn}. Move on which space?')
        move = player_turn()
        board[move] = turn

        if is_win():
            print_board(board)
            print(f'Player "{turn}" win! Congratulation!')
            return
        
        # Change player
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'
    print_board(board)
    print('You tied.')
    return

def main():
    print('\nTic-Tac-Toe!\n')
    while True: # Menu loop
        user_input = choose_from_menu()
        if user_input == 0:
            how_to_play()
            continue
        elif user_input == 1:
            one_player()
        else:
            two_players()
        if input('Do you want to play again? (y/n): ').lower().strip() == 'y':
            break


if __name__ == '__main__':
    main()