#! python3
"""
rename_dates.py - Renames filenames with American MM-DD-YYYY date format to
European DD-MM-YYYY.

Usage:
    rename_dates.py [-h] [-s SEPARATOR] [path]

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import shutil
import os
import re
import sys
import argparse

def rename_files(path: str, sep: str):
    """Renames filenames in the specified directory from American date format
    (MM-DD-YYYY) to European date format (DD-MM-YYYY).

    Args:
        path (str): The path to the directory containing the files to rename.
        sep (str): The separator used in the date format.
    """
    # American date *simple* regex
    american_date_regex = re.compile(rf'''
        ^(.*?)              # All text before the date
        ((0|1)?\d){sep}     # Month
        ((0|1|2|3)?\d){sep} # Day
        ((19|20)\d\d)       # Year
        (.*?)$              # All text after the date
        ''', re.VERBOSE)

    for filename in os.listdir(path):
        mo = american_date_regex.search(filename)  # Mathced Object
        # Skip files without date
        if mo is None:
            continue

        # Regex parts
        before = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        after = mo.group(8)

        # Form euro-style filename
        new_filename = before + day + sep + month + sep + year + after

        # Get the absolute filepath
        abs_workdir = os.path.abspath('.')
        filename = os.path.join(abs_workdir, filename)
        new_filename = os.path.join(abs_workdir, new_filename)

        # Rename the files
        print(f"Renaming {filename} to {new_filename}...")
        shutil.move(filename, new_filename)


def main():
    """Main."""
    parser = argparse.ArgumentParser(description=("Renames filenames with "
                                     "American MM-DD-YYYY date format to "
                                     "European DD-MM-YYYY."))
    # Arguments
    parser.add_argument('path', nargs='?', default='.',
                        help=("Optional path to directory with files "
                              "(default is current directory)."))
    parser.add_argument('-s', '--separator', nargs='?', default='-',
                        help="Separator used in the date format "
                        "(default is '-').")
    args = parser.parse_args()

    if args.path:
        path = os.path.abspath(args.path)
    else:
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
    if not os.path.isdir(path):
        parser.error(f"The path {path} is not a valid directory.")

    rename_files(path, args.separator)

if __name__ == "__main__":
    main()
