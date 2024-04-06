# Table Printer

This program is a Python script designed to print data as a formatted table.

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
              Character|                Species|             Occupation|
      Commander Shepard|                  Human|                Spectre|
        Garrus Vakarian|                 Turian|   Former C-Sec Officer|
           Liara T'Soni|                  Asari|          Archaeologist|
Tali'Zorah vas Normandy|                Quarian|               Engineer|
            Urdnot Wrex|                 Krogan|              Mercenary|
```

## Requirements

- Python 3.x

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)