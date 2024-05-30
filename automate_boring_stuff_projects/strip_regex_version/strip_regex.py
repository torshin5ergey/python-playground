"""
strip_regex.py - Regular expression version of Python's strip() method.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""


import re


def strip_regex(text: str, chars=" ") -> str:
    """
    Removes leading and trailing characters from a string using regular expression.

    Args:
        text (str) -- text to strip.
        chars (str, optional) -- characters to remove (default " " whitespace).

    Returns:
        str -- stripped text.
    """
    # re.escape() to handle any special characters in the 'chars' string
    return re.sub(f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$', '', text)


def main():
    text_to_strip = '***Regex Version of the strip() Method***'
    print(strip_regex(text_to_strip))

if __name__ == "__main__":
    main()