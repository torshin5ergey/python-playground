#! python
# bpadder.py - Adds bullet points to the list
# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

import pyperclip
import argparse

# Separate lines and add bullets
def make_bulleted_list(lines: list) -> str:
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i] 
    bulleted_list = '\n'.join(lines)
    return bulleted_list

# Separate lines and add numbers
def make_numbered_list(lines: list) -> str:
    for i in range(len(lines)):
        lines[i] = str(i+1) + ' ' + lines[i] 
    numbered_list = '\n'.join(lines)
    return numbered_list

def main():
    parser = argparse.ArgumentParser(description='Add bullet points or numbers to the list from the clipboard.')
    parser.add_argument('bullet', nargs='?', default='*', help='Specify "1" for numbered list or any other character for bulleted list. Default is "*".')
    args = parser.parse_args()

    clipboard_text = pyperclip.paste()
    if not clipboard_text:
        print('The clipboard is empty.')
        return

    lines = clipboard_text.split('\n')
    if args.bullet == '--help':
        parser.print_help()
    if args.bullet == '1':
        result_list = make_numbered_list(lines)
    else:
        result_list = make_bulleted_list(lines)
    print('The formatted list copied to clipboard.')
    pyperclip.copy(result_list)

if __name__ == "__main__":
    main()