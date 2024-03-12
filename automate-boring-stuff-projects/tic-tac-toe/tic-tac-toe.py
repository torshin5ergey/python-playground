# Tic Tac Toe Game

# Game board
board = {'topL': ' ', 'topM': ' ', 'topR': ' ', 'midL': ' ', 'midM':
' ', 'midR': ' ', 'botL': ' ', 'botM': ' ', 'botR': ' '}

def print_board(board: dict) -> None:
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['botL'] + '|' + board['botM'] + '|' + board['botR'])

# Print "How to play" message
def how_to_play() -> None:
    print('''\nHow to play\n'''
          '''1. When it's your turn, simply specify the coordinate where you want to place your mark. For example, "topL" corresponds to the top-left corner, "midM" - the middle in the middle, and so on.\n'''
          '''Coordinates are in accordance with the field below:\n''')
    print('topL' + '|' + 'topM' + '|' + 'topR')
    print('----+----+----')
    print('midL' + '|' + 'midM' + '|' + 'midR')
    print('----+----+----')
    print('botL' + '|' + 'botM' + '|' + 'botR')
    print('''\n2. The first player plays as "X", and the second player plays as "O"\n'''
          '''3. The player who first fills a row, column, or diagonal with their marks wins.''')

# Choose game mode: one or two players
def choose_game_mode() -> int:
    while True:
        try:
            mode = int(input('\nGame modes:\n1. One player\n2. Two players\nChoose mode (1/2): '))
            if mode not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print('\nError! Choose 1 or 2')
    return mode

def check_turn():
    pass

def one_player():
    pass
    
def is_win():
    pass

def two_players():
    turn = 'X'
    for _ in range(9):
        print_board(board)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        check_turn()########################
        board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print_board(board)
    is_win()##########################

def main():
    print('\nWelcome to Tic-Tac-Toe Game!')
    how_to_play()
    if choose_game_mode() == 1:
        one_player()
    else:
        two_players()


if __name__ == '__main__':
    main()