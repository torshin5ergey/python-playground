# Chess Dictionary Validator

This Python function checks whether a given chessboard configuration is valid. It is inspired by a practice project [Chess Dictionary Validator](https://automatetheboringstuff.com/2e/chapter5/#calibre_link-204) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The function is_valid_chessboard() takes a dictionary representing a chessboard configuration as input and returns True if the configuration is valid, and False otherwise.

### Validation criteria
1. **Board Spaces**:
- Each key in the dictionary represents a chessboard space.
- Each space key consists of a digit (from 1 to 8) representing the row number and a lowercase character (from 'a' to 'h') representing the column letter.
- Example of a valid space: '1h', '6c'.
2. **Pieces**:
- The values in the dictionary represent the pieces placed on the board.
- Each piece is represented by a string with a specific name.
The function checks whether the number of each type of piece is within the allowed limits.
- Example of valid pieces: 'wking', 'bqueen'.
3. **Piece Counts**:
- The function ensures that the number of each type of piece does not exceed the allowed number of pieces on a standard chessboard.
- Example of allowed piece counts: 1 white king, 2 black rooks, 8 white pawns, etc.

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
