# Large Files Finder

Python script that finds and prints large files in a specified directory.
It is inspired by a practice project [Deleting Unneeded Files](https://automatetheboringstuff.com/2e/chapter10/#calibre_link-347) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

Large Files Finder is a simple tool for finding large files in a specified directory. It allows you to specify a path to search for files, a size limit, and the number of files to print. The script then scans the directory and its subdirectories, finds files larger than the specified size limit, and prints their paths and sizes.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/automate_boring_stuff_projects/delete_unneeded_files
```
3. Run Python file with desired arguments (e.g.)
```
python largefiles.py C:\ 100MB -n 20
```

## Usage
```
largefiles.py [-h] [-n FILES_COUNT] path size_limit

positional arguments:
  path                  Path to search for files
  size_limit            Size lower limit (in KB, MB, GB, e.g. 100KB, 10MB, 1GB, 1TB)

optional arguments:
  -h, --help            show this help message and exit
  -n FILES_COUNT, --files-count FILES_COUNT
                        Number of files to print
```

### Examples

- Find large files in the current directory with a size limit of 100MB and print the first 20 files:
    ```
    python largefiles.py . 100MB -n 20
    ```
- Find large files in the C:\ directory with a size limit of 1GB and print all files:
    ```
    python largefiles.py C:\ 1GB
    ```

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
