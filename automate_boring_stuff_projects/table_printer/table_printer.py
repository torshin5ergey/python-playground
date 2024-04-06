# table_printer.py - Print formatted table from list of lists
# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

def print_table(table: list[list[str]], separ: str = ' ', rev: bool = False) -> None:
    """
    Prints the given table in a formatted manner.
    Parameters:
    - table (list[list[str]]): The table to be printed.
    - separ (str, optional): The separator to be used between cells.
    - rev (bool, optional): Table layout. False (default): rows - horizontally,
    columns - vertically. True: columns - horizontally, rows - vertically.
    """
    # Inner lists length (same for all)
    line_length = len(table[0])
    # Name every column width
    column_widths = [0] * len(table)
    # Find longest cell in every row
    for row in range(len(table)):
        column_widths[row] = max(len(cell) for cell in table[row])
    widest_column = max(column_widths)

    # Print table data 
    if rev: # normal layout
        for col in range(line_length):
            for cell in range(len(table)):
                print(table[cell][col].rjust(column_widths[cell]), end=separ)
            print()
    else: # reverse layout
        for row in table:
            for cell in row:
                print(cell.rjust(widest_column), end=separ)
            print()
    return


def main():
    table_data = [["Character", "Species", "Occupation"],
                 ["Commander Shepard", "Human", "Spectre"],
                 ["Garrus Vakarian", "Turian", "Former C-Sec Officer"],
                 ["Liara T'Soni", "Asari", "Archaeologist"],
                 ["Tali'Zorah vas Normandy", "Quarian", "Engineer"],
                 ["Urdnot Wrex", "Krogan", "Mercenary"]]
    print_table(table_data, separ='|')

if __name__ == "__main__":
    main()