#! python
# mclip.py - A multi-clipboard program
# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

import sys
import pyperclip

# keyphrase-text pairs
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'intro': """Hello there! My name is [Name].""",
        'debug': """I'm currently debugging the issue. It might take some time.""",
        'test+': """All test cases have passed successfully."""}

# Copies the text corresponding to the keyphrase to the clipboard.
def copy_top_clipboard(keyphrase: str) -> None:
    try:
        pyperclip.copy(TEXT[keyphrase])
        print(f'Text for {keyphrase} copied to clipborad.\n={TEXT[keyphrase]}=')
    except KeyError:
        print(f'There is no text for {keyphrase}. Use -list to see available keyphrases')

def print_commands_list():
    print('Available keyphrases and messages:')
    for k, v in TEXT.items():
        print(f'  {k}: {v}')

def add_keyphrase(new_key, new_value):
    TEXT[new_key] = new_value
    print(f'Keyphrase "{new_key}" with text "{new_value}" added successfully.')

def print_help():
    print('''Usage:
    mclip [keyphrase] - copy phrase text
    mclip -add [keyphrase] [text] - add a new keyphrase and its text
    mclip -list - available keyphrases and messages
    mclip -help - print this help message

Examples:
    mclip intro
    mclip -list
    mclip -add keyphrase TextInOneWord
    mclip -add keyphrase "Text In Multiple Words"''')

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit()
    if sys.argv[1] == '-help':
        print_help()
    elif sys.argv[1] == '-list':
        print_commands_list()
    elif sys.argv[1] == '-add':
        if len(sys.argv) != 4:
            print('Usage: mclip -add [keyphrase] [text]')
            sys.exit()
        add_keyphrase(sys.argv[2], sys.argv[3])
    else:
        copy_top_clipboard(sys.argv[1])


if __name__ == "__main__":
    main()