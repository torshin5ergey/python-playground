# Regex Search Tool

Opens all `.txt` files in a folder and searches for any line that matches a user-supplied regular expression.
It is inspired by a practice project [Regex Search](https://automatetheboringstuff.com/2e/chapter9/#calibre_link-322) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The **Regex Search Tool** is designed to search through text files within a specified directory for lines that match a given regular expression pattern. It offers flexibility with optional case-insensitive search and allows specifying a directory path for targeted file search.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/automate_boring_stuff_projects/regex_search
```
3. Run Python file with desired arguments (e.g.)
```
python regex_search.py -i <pattern>
```
4. *Compile into an executable (optional):
```
pyinstaller regex_search.spec
```

## Contents

- `regex_search.py`: Script for regex search.
- `regex_search.spec`: PyInstaller specification file for building executable.
- `test.txt`: Example text file for testing regex searches.
- `README.md`: This readme file.

## Usage

Basic regex search:
```
regex_search <pattern> 

python regex_search.py '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```
Case-insensitive search:
```
regex_search -i <pattern>

python regex_search.py -i '[a-z]{,10}'
```

Search in a specific directory:
```
regex_search <pattern> dir

python regex_search.py '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' C:\Users\User\Desktop
```

## Requirements

- [PyInstaller](https://pypi.org/project/pyinstaller/) (optional, for compiling into executable)

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
