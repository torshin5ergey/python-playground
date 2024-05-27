'''
date_validator.py - Detect and validate dates in DD/MM/YYYY format.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''
#! python3

import re
import pyperclip

# Detect and validate dates in the given text
def date_detect_valid(text: str) -> list[str]:
    # DD/MM/YYYY regex
    date_regex = re.compile(r'''
        \b
        (0[1-9]|[12]\d|3[01])   #  Day: 01-09, 10-29, 30-31
        \/                      #  Divider: /
        (0[1-9]|1[0-2])         #  Month: 01-09, 10-12
        \/                      #  Divider: /
        ([12]\d{3})             #  Year: 1000-2999
        \b
        ''', re.VERBOSE)
    
    valid_dates = []

    # Find all dates in the text with regex
    for match in date_regex.findall(text):
        day, month, year = match
        # February check
        # Leap year
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
            #  Feb can have up to 29 days
            if int(month) == 2 and int(day) > 29:
                continue
        # Non-leap year. Feb can have up to 29 days
        elif int(month) == 2 and int(day) > 28:
            continue
        # Validate months with 30 days
        if int(month) in (4, 6, 9, 11) and int(day) > 30:
            continue
        valid_dates.append('/'.join((day, month, year)))
    return valid_dates


def main():
    text = pyperclip.paste()
    dates = date_detect_valid(text)
    pyperclip.copy('\n'.join(dates))

if __name__ == "__main__":
    main()
