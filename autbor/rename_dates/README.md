# Rename Dates

This script searches all the filenames in the current working directory for American-style dates.
When one is found, it renames the file with the month and day swapped to make it European-style.
It is inspired by a practice project [Renaming Files with American-Style Dates to European-Style Dates](https://automatetheboringstuff.com/2e/chapter10/#calibre_link-333) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This script renames files in a directory by converting dates from the American format (MM-DD-YYYY) to the European format (DD-MM-YYYY). It processes filenames and uses a regular expression to identify and transform the date formats.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/autbor/rename_dates
```
3. Run Python file with desired arguments (e.g.)
```
python rename_dates.py -s /
```

## Usage

Rename files with American-style dates in the current directory to European-style dates:
```
python rename_dates.py
```

Specify a directory to rename files with American-style dates to European-style dates:
```
python rename_dates.py /path/to/directory
```

Use a different separator (e.g., slash / ) instead of the default hyphen - :
```
python rename_dates.py -s /
```

Or if the files are in a specified directory and use a slash:
```
python rename_dates.py /path/to/directory -s /
```

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
