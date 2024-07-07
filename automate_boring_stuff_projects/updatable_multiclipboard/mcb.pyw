"""
mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
       py.exe mcb.pyw list - Loads all keywords to clipboard.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import sys
import shelve
import pyperclip


def main():
    mcb_shelf = shelve.open('mcb')
    # Save clipboard content
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # List keywords and load content
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
        else:
            pyperclip.copy(mcb_shelf[sys.argv[1]])

    mcb_shelf.close()

if __name__ == "__main__":
    main()
