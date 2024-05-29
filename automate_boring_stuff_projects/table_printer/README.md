# Table Printer

This program is a Python script designed to print data as a formatted table. It is inspired by a practice project [Table Printer](https://automatetheboringstuff.com/2e/chapter6/#calibre_link-235) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The print_table() function takes a list of lists representing a table as input, along with optional parameters for the separator and table layout. Assume that all the inner lists will contain the same number of strings.
It then prints the table in a formatted manner, aligning the columns either horizontally or vertically based on the specified layout.

## How to Use

To use the Table Printer, simply import the print_table() function into your Python script and call it with the desired table data. Optionally, you can customize the separator and table layout by providing values for the separ and rev parameters, respectively.

## Usage Example

```python
from table_printer import print_table
# Define table data
table_data = [["Character", "Species", "Occupation"],
              ["Commander Shepard", "Human", "Spectre"],
              ["Garrus Vakarian", "Turian", "Former C-Sec Officer"],
              ["Liara T'Soni", "Asari", "Archaeologist"],
              ["Tali'Zorah vas Normandy", "Quarian", "Engineer"],
              ["Urdnot Wrex", "Krogan", "Mercenary"]]
# Print the table with '|' as the separator and normal layout
print_table(table_data, separ='|', rev=True)
```
Output:
```
              Character|Species|          Occupation|
      Commander Shepard|  Human|             Spectre|
        Garrus Vakarian| Turian|Former C-Sec Officer|
           Liara T'Soni|  Asari|       Archaeologist|
Tali'Zorah vas Normandy|Quarian|            Engineer|
            Urdnot Wrex| Krogan|           Mercenary|
```

## *Notes*

- **zip() function** is used in the print_table() to transpose the matrix (table).
- **Transposing the table** is using when the layout is reversed (`rev=True`).
- **Optional parameters** in the print_table() `separ` and `rev`. The `separ` specifies the separator between cells, default is space. The `rev` specifies the table layout, default is `False` for rows being horizontal and columns vertical.

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)