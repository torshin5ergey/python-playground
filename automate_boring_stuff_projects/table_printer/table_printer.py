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
    # Table transpose
    if rev:
        table = list(zip(*table))
    # Find column width for every column
    column_widths = [max(map(len, cell)) for cell in zip(*table)]
    # Print table data 
    for row in table:
        for col_x, cell in enumerate(row):
            print(cell.rjust(column_widths[col_x]), end=separ)
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