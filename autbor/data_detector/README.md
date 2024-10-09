# Data Detector

This directory contains a Python script for detecting various types of data in text copied to the clipboard. It is inspired by a practice project [Phone Number and Email Address Extractor](https://automatetheboringstuff.com/2e/chapter7/#calibre_link-264) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The script utilizes regular expressions to search for patterns corresponding to phone numbers, email addresses, and URLs in the copied text. Upon detection, the script copies the found data to the clipboard for easy access.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\autbor\data_detector
```
3. Run Python file
```bash
python data_detector.py
```
Or you can import data detection functions into your project, for example
```python
from data_detector import url_detector
```

## How to run tests

To run the unit tests for URL detection, execute the `test_url_detector.py` file using pytest.

## Usage Example
1. Copy to clipboard:
```
Phone: 8(777)345-11-23 or +7(451)451-41-14
Fax: +7 777 345-11-23
Please email support@example.com with your questions
Visit our website at http://example.com
Check out our website: www.example.org
Click here: https://shop.example.ru
Appointment dates: 3/14/2019, 03-14-2019, and 2015/3/19
```
2. Run the `data_detector.py`
3. The script output is:
```
Phone numbers found.
Emails found.
URLs found.
Dates found.
```
And the clipboard will have:
```
Phones:
8 (777) 345-11-23
+7 (451) 451-41-14
+7 (777) 345-11-23

Emails:
support@example.com

URLs:
example.com
http://example.com
www.example.org
https://shop.example.ru

Dates:
2019-03-14
2019-03-14
2015-03-19
```

## Contents

1. `data_detector.py`: Script with functions for detecting phone numbers, email addresses, URLs, dates (in different format DD/MM/YYYY, DD-MM-YYYY, YYYY/MM/DD) in copied text.
2. `test_data_detector.py`: Unit tests for data_datector.py functions

### Functions

- `phone_detect`: Find phone numbers (in Russian format) in the provided text.
- `email_detect`: Find email addresses in the provided text.
- `url_detect`: Find URLs in the provided text.
- `date_detect`: Find dates in formats in the provided text. Input formats:
    - MM/DD/YYYY
    - MM-DD-YYYY
    - YYYY/MM/DD
- `format_dates`: Convert dates from various formats to the format YYYY-MM-DD. Input formats:
    - MM/DD/YYYY
    - MM-DD-YYYY
    - YYYY/MM/DD
- `clean_text`: Remove accidentally repeated words, multiple spaces between words, and multiple exclamation marks at the end of sentences.

## Requirements

- [pyperclip (1.8.2 used)](https://pypi.org/project/pyperclip/)
- [pytest (7.3.1 used)](https://docs.pytest.org/en/latest/index.html)

## *Notes*

- The script utilizes regular expressions for pattern matching. The code comments has details on the regex patterns used.
- `format_dates()` uses iterative parsing of date in string. Each date is compared to date patterns.
- Regular expressions allows to use the groups marked inside  it by specifying its number like `\1` for first group in this regular expression.
- Unit tests for the script's functionality can be found in the test_url_detector.py file. The tests use the pytest framework and include parameterization and mock functions.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
