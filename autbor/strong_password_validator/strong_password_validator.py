"""
strong_password_validator.py - Strong password validator using regular expressions.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""


import re


def strong_password_validator(password: str) -> bool:
    # At least 8 characters
    length_regex = re.compile(r'\b.{8,}\b')
    # Upper and lower cases
    cases_regex = re.compile(r'(?=^.*[a-z])(?=.*[A-Z]).*$')
    # At least 1 digit
    digit_regex = re.compile(r'(?=^.*[0-9]).*$')

    is_strong = True

    if not length_regex.search(password):
        is_strong = False
    if not cases_regex.search(password):
        is_strong = False
    if not digit_regex.search(password):
        is_strong = False

    return is_strong


def main():
    password = input("Enter your password:\n")
    if strong_password_validator(password):
        print("Your password is strong!")
    else:
        print("Your password is weak(")

if __name__ == "__main__":
    main()



