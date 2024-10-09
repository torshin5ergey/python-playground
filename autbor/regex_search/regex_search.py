"""
regex_search.py - Opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression.

Usage:
    regex_search.py [-h] [-i] PATTERN [path]

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import os
import sys
import re
import argparse
import pprint


def list_files(path: str):
    """List all .txt files in the given directory path."""
    files = os.listdir(path)
    # Filter only txt
    files = [file for file in files if file.endswith(".txt")]
    return [os.path.join(path, file) for file in files]


def parse_file(regex: str, file: str, mode=None):
    """Parse a file and find all matches of the given regex."""
    mode = re.IGNORECASE if mode else 0
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(regex, text, flags=mode)
    return matches


def main():
    """Main."""
    parser = argparse.ArgumentParser(description=("Search for lines matching a "
                                     "regex in all .txt files in a directory."))
    # Arguments
    parser.add_argument('-i', '--ignore-case', action='store_true',
                        help="Ignore case sensitivity in search.")
    parser.add_argument('pattern', metavar='PATTERN', type=str,
                        help="Regular expression to search for in files.")
    parser.add_argument('path', nargs='?', default='.',
                        help=("Optional path to directory with files"
                              "(default is current directory)."))
    args = parser.parse_args()

    if args.path:
        path = os.path.abspath(args.path)
    else:
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
    if not os.path.isdir(path):
        parser.error(f"The path {path} is not a valid directory.")

    text_files = list_files(path)
    matches = []
    for f in text_files:
        cur_match = parse_file(args.pattern, f, args.ignore_case)
        if cur_match:
            matches.append(cur_match)

    # Print results
    pprint.pprint(matches)
    # Wait to exit
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
