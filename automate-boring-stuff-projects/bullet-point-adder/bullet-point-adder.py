# #! python
# bullet-point-adder.py - Adds Wikipedia bullet points to the start
# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

import pyperclip

def main():
    lines = pyperclip.paste().split('\n')
    # Separate lines and add stars.
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i] 
    new_list = '\n'.join(lines)
    pyperclip.copy(new_list)


if __name__ == "__main__":
    main()