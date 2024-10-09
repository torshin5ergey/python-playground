"""
character_picture_grid.py - Character Picture Grid

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

# Print the image using the symbols grid.
def print_character(grid):
    for i in grid:
        print()
        for j in i:
            print(j, end='')  

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    print_character(grid)

if __name__ == '__main__':
    main()