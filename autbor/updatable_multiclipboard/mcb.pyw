"""
mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage: mcb.pyw save <keyword> - Saves clipboard to keyword.
       mcb.pyw delete <keyword> - Deletes keyword to clipboard.
       mcb.pyw <keyword> - Loads keyword to clipboard.
       mcb.pyw list - Loads all keywords to clipboard.
       mcb.pyw delete - Deletes all saved keywords.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import sys
import shelve
import pyperclip


def main():
    mcb_shelf = shelve.open('mcb')
    # Save or delete clipboard content
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]
    # List keywords, delete or load content
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1].lower() == 'delete':
            mcb_shelf.clear()
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
    mcb_shelf.close()

if __name__ == "__main__":
    main()
