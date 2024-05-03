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
def phone_detect(text:str) -> None:
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
    ([a-zA-Z0-9._%+-]{1,})+ # Username
    (@)                     # @ symbol
    ([a-zA-Z0-9.-]{1,})+    # Domain name
    (\.[a-zA-Z]{2,4})       # Dot-something
    )''', re.VERBOSE)        
def email_detect(text:str) -> None:
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
    (http:\/\/|https:\/\/)?     # Scheme (protocol)
    (www\.)?                    # Subdomain (www)
    ([a-zA-Z]{2,}\.)?           # Subdomain
    ([a-zA-Z0-9]{2,})           # Domain
    (\.[a-zA-Z]{2,3})           # Top-level domain
    (\/[a-zA-Z0-9-]+)*          # Path
    (\?[a-zA-Z0-9=&]*)?         # Params
    (\#\w*)?                    # Section
    (\:\d{,4})?                 # Port
    )''', re.VERBOSE)
def url_detect(text:str) -> None:
    matches = []
    # Find all URLs in the text
    for group in url_regex.findall(text):
        matches.append(group[0])
    if matches:
        result = '\n'.join(matches)
        return result
    else:
        print('No URLs found.')

def main():
    # Get the text off the clipboard
    text = pyperclip.paste()
    result = ''
    result += 'Phones:\n' + phone_detect(text)
    result += '\n\nEmails:\n' + email_detect(text)
    result += '\n\nURLs:\n' + url_detect(text)
    pyperclip.copy(result)

if __name__ == "__main__":
    main()
