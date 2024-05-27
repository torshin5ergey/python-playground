# Date Validator

A Python script to detect and validate dates in the format DD/MM/YYYY.
It is inspired by a practice project [Date Detection](https://automatetheboringstuff.com/2e/chapter7/#calibre_link-274) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This script uses regular expression to find dates in a given text and validates them. The validation process ensures that:
- Days (01 to 31), months (01 to 12), and years (1000 to 2999) are within their valid ranges.
- February has 28 days in a non-leap year and 29 days in a leap year.
- April, June, September, and November have 30 days.
- January, March, May, July, August, October, and December have 31 days.

The valid dates found in the text are then copied back to the clipboard.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\automate_boring_stuff_projects\date_validator
```
3. Run Python file
```bash
python date_validator.py
```
Or you can import date validator functions into your project, for example
```python
from date_validator import date_detect_valid
```

## Usage Example

1. Copy to clipboard:
```
I have some important dates to remember this year. My friend's birthday is on 15/03/2024 (valid), and my anniversary is on 29/02/2023 (invalid, as 2023 is not a leap year). Our vacation starts on 30/04/2024 (valid), but I mistakenly wrote 31/04/2024 (invalid, as April has only 30 days). Another important date is 12/12/2024 (valid), and my cousin's graduation is on 32/01/2024 (invalid, as January has only 31 days). Finally, we have a family gathering on 29/02/2024 (valid, as 2024 is a leap year).
```
2. Run the `date_validator.py`
3. The sript output in the clipboard valid dates only:
```
15/03/2024
30/04/2024
12/12/2024
29/02/2024
```

## Requirements

- [pyperclip (1.8.2 used)](https://pypi.org/project/pyperclip/)

## *Notes*

- Date validation could also be achieved using `datetime` module with `strptime` for parsing and `strftime` for formatting.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
