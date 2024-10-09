# Selective Copy

A Python script that selectively copy files with specified extensions
from one directory to another.
It is inspired by a practice project [Selective Copy](https://automatetheboringstuff.com/2e/chapter10/#calibre_link-346) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This script allows users to search for files with specific extensions in a given source directory and copy them to a specified destination directory. It is useful for organizing files by type, backing up specific file types, or simply filtering files based on their extensions.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/autbor/selective_copy
```
3. Run Python file with desired arguments (e.g.)
```
python selectivecopy.py .jpg .pdf C:\User\Desktop 'C:\User\Desktop\New dir'
```

## Usage

```
selectivecopy.py .ext1 .ext2 .ext3 path/from/to path/where/to
```
options:
extensions  A list of file extensions to search for (e.g. `.txt .jpg`).
wherefrom   The path to the source directory where files will be searched.
whereto     The path to the destination directory where matching files will be copied.

### Example

To copy all `.txt` and `.jpg` files from the `~/Documents` directory to the `~/Backup` directory, you would run:
```
python selectivecopy.py .txt .jpg ~/Documents ~/Backup
```

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
