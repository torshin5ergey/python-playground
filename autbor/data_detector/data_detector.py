"""
data_detector.py - Finds data (phone number, email, URL, date) on the clipboard.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

#! python3

import re
import pyperclip
from datetime import datetime


# Phone regex (RU)
phone_regex = re.compile(r'''(
    (\+\d{1,3} | \d{1,3})   # International area code
    (\s | -)?               # Separator
    (\d{3} | \(\d{3}\))     # Mobile operator/city code
    (\s | -)?               # Separator 
    # User number                      
    (\d{3})                 # Second 3 digits
    (\s | -)?               # Separator  
    (\d{2})                 # Last group first 2 digits
    (\s | -)?               # Separator 
    (\d{2})                 # Last group second 2 digits                                              
    )''', re.VERBOSE)
def phone_detect(text:str) -> str:
    matches = []
    # Find all phone numbers in the text
    for group in phone_regex.findall(text):
        code_group = '(' + group[3].replace('(', '').replace(')', '') + ')'
        user_group = '-'.join((group[5], group[7], group[9]))
        phone_num = ' '.join((group[1], code_group, user_group))
        matches.append(phone_num)
    if matches:
        result = '\n'.join(matches)
        print('Phone numbers found.')
        return result
    else:
        print('No phone numbers found.')

# Email regex
email_regex = re.compile(r'''(
    ([a-z0-9._%+-]{1,})+    # Username
    (@)                     # @ symbol
    ([a-z0-9.-]{1,})+       # Domain name
    (\.[a-z]{2,4})          # Dot-something
    )''', re.VERBOSE | re.I)        
def email_detect(text:str) -> str:
    matches = []
    # Find all email addresses in the text 
    for group in email_regex.findall(text):
        matches.append(group[0])
    # Copy results to the clipboard
    if matches:
        result = '\n'.join(matches)
        print('Emails found.')
        return result
    else:
        print('No emails found.')

# URL regex
url_regex = re.compile(r'''(
    (https?:\/\/)?      # Scheme (protocol)
    (www\.)?            # Subdomain (www)
    ([a-z]{2,}\.)?      # Subdomain
    ([a-z0-9]{2,})      # Domain
    (\.[a-z]{2,3})      # Top-level domain
    (\/[a-z0-9-]+)*     # Path
    (\?[a-z0-9=&]*)?    # Params
    (\#\w*)?            # Section
    (\:\d{,4})?         # Port
    )''', re.VERBOSE | re.I)
def url_detect(text:str) -> str:
    matches = []
    # Find all URLs in the text
    for group in url_regex.findall(text):
        matches.append(group[0])
    if matches:
        result = '\n'.join(matches)
        print('URLs found.')
        return result
    else:
        print('No URLs found.')

# Date regex
date_regex = re.compile(r'''(
    \b
    ((\d{1,2})[\/\-.](\d{1,2})[\/\-.](\d{4}|\d{2})) |   # MM/DD/YYYY separators (/-.)
    (\d{4}[\/\-.](\d{1,2})[\/\-.](\d{1,2}))             # YYYY/MM/DD separators (/-.)
    \b
    )''', re.VERBOSE)
def date_detect(text:str) -> str:
    matches = []
    # Find all dates in the text
    for group in date_regex.findall(text):
        matches.append(group[0])
    if matches:
        result = '\n'.join(matches)
        print('Dates found.')
        return result
    else:
        print('No dates found.')

# Format date into YYYY-MM-DD
def format_dates(dates:str) -> str:
    input_formats = ('%m/%d/%Y', '%m-%d-%Y', '%Y/%m/%d')
    output_format = '%Y-%m-%d'
    output = []
    for date in dates.split('\n'):
        is_finded = False
        for format in input_formats:
            # Parse a string into a datetime object given a corresponding format
            try:
                date_object = datetime.strptime(date, format)
                output.append(date_object.strftime(output_format))
                is_finded = True
                break
            except ValueError:
                continue
        if not is_finded:
            output.append(date)
    return '\n'.join(output)

# DONE: multiple spaces between words
# DONE: accidentally accidentally repeated words
# DONE: multiple exclamation marks at the end of sentences
repeated_word_regex = re.compile(r'''
    \b
    (\w+)   # Catch a word (1st group)
    \s+     # One or more spaces
    \1      # The word from 1st group
    \b
    ''', re.VERBOSE | re.I)
# Clean text
def clean_text(text: str) -> str:
    text = text.strip()
    # Delete multiple spaces between words
    text = re.sub(r'\s+', ' ', text)
    # Delete accidentally repeated words
    text = re.sub(repeated_word_regex, r'\1', text)
    # Delete multiple exclamation marks at the end of sentences
    text = re.sub(r'(.)\1+$', r'\1', text)
    return text

# Run all functions
def main():
    # Get the text off the clipboard
    text = pyperclip.paste()
    result = ''
    # Find phones
    phones = phone_detect(text)
    if phones:
        result += 'Phones:\n' + phones
    # Find emails
    emails = email_detect(text)
    if emails:
        result += '\n\nEmails:\n' + emails
    # Find URLs
    urls = url_detect(text)
    if urls:
        result += '\n\nURLs:\n' + urls
    # Find dates
    dates = date_detect(text)
    if dates:
        result += '\n\nDates:\n'
        # Format dates
        result += format_dates(dates)
    pyperclip.copy(result)

if __name__ == "__main__":
    main()
