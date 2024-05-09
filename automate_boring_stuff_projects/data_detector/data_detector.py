'''
data_detector.py - Finds data (phone number, email, URL, date etc.) on the clipboard.
Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''
#! python3

import re
import pyperclip


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
        return result
    else:
        print('No emails found.')

# URL regex
url_regex = re.compile(r'''(
    (https?:\/\/)?     # Scheme (protocol)
    (www\.)?           # Subdomain (www)
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
        return result
    else:
        print('No URLs found.')

# Date regex
date_regex = re.compile(r'''(
    \b
    (\d{1,2}[\/\-.]\d{1,2}[\/\-.](\d{4}|\d{2})) |   # DD/MM/YYYY separators (/-.)
    (\d{4}[\/\-.]\d{1,2}[\/\-.]\d{1,2})             # YYYY/MM/DD separators (/-.)
    \b
)''', re.VERBOSE)
def date_detect(text:str) -> str:
    matches = []
    # Find all dates in the text
    for group in date_regex.findall(text):
        matches.append(group[0])
    if matches:
        result = '\n'.join(matches)
        return result
    else:
        print('No dates found.')

def main():
    # Get the text off the clipboard
    text = pyperclip.paste()
    result = ''
    # Phones
    phones = phone_detect(text)
    if phones:
        result += 'Phones:\n' + phones
    # Emails
    emails = email_detect(text)
    if emails:
        result += '\n\nEmails:\n' + emails
    # URLs
    urls = url_detect(text)
    if urls:
        result += '\n\nURLs:\n' + urls
    # Dates
    dates = date_detect(text)
    if dates:
        result += '\n\nDates:\n' + dates
    pyperclip.copy(result)

if __name__ == "__main__":
    main()