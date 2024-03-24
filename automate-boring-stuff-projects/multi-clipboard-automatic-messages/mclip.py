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
        print(f'There is no text for {keyphrase}')

def main():
    if len(sys.argv) < 2:
        print('Usage: python mclip.py [keyphrase] - copy phrase text')
        sys.exit()

    copy_top_clipboard(sys.argv[1])


if __name__ == "__main__":
    main()