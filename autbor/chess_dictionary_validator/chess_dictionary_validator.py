"""
chess_dictionary_validator.py - Chess dictionary validator

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

def is_valid_chessboard(board: dict) -> bool:
    # Checking board spaces
    for space in board.keys():
        # Digit validator
        if (len(space) != 2 or
            not (0 < int(space[0]) <= 8) or # Digit validator
            space[1] not in 'abcdefgh'): # Char validator
            return False

    # Checking pieces
    required_pieces = {'wking': 1, 'wqueen':1, 'wrook': 2, 'wbishop': 2, 'wknight': 2, 'wpawn': 8,
                       'bking': 1, 'bqueen':1, 'brook': 2, 'bbishop': 2, 'bknight': 2, 'bpawn': 8,}
    piece_count = {}
    for piece in board.values():
        if piece not in required_pieces.keys():
            return False
        else:
            # Count pieces
            piece_count.setdefault(piece, 0)
            piece_count[piece] = piece_count[piece]+1
    # Checking that the number of each figure does not exceed the allowed number of pieces
    for piece, count in piece_count.items():
        if count > required_pieces[piece]:
            return False
    
    return True

my_board = {'1h': 'bking',
            '6c': 'wqueen',
            '2g': 'bbishop',
            '8h': 'bqueen',
            '3e': 'wking', 
            '4f': 'brook'}
print(is_valid_chessboard(my_board)) # True