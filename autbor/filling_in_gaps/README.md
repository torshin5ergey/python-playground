# Filling In Gaps

A Python script to find and fill gaps in a sequence of files with a given prefix.
It is inspired by a practice project [Filling in the Gaps](https://automatetheboringstuff.com/2e/chapter10/#calibre_link-348) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This script finds and fills gaps in a sequence of files with a given prefix. It searches for files with the specified prefix in a given directory, identifies gaps in the sequence, and renames the files to fill in the gaps.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/autbor/filling_in_gaps
```
3. *(*Optional)* Create test files with create_files.py
```
python create_files.py
```
4. Run Python file with desired arguments (e.g.)
```
python fillinggaps.py spam .
```

## Contents

- `create_files.py`: Test `spamXXX.txt` files creator with random gaps
- `fillinggaps.py.py`: Main script
- `README.md`: This readme file

## Usage
```
fillinggaps.py [-h] prefix path

Large files finder

positional arguments:
  prefix
  path        Path to search for files with the prefix

optional arguments:
  -h, --help  show this help message and exit
```

### Examples

- Fill gaps in files with the prefix "spam" in the current directory:
    ```
    python fillinggaps.py spam .
    ```
- Fill gaps in files with the prefix "example" in the "/path/to/directory" directory:
    ```
    python fillinggaps.py example /path/to/directory
    ```

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
