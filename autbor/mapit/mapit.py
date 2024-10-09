#! python3
"""
mapit.py - Launches a map in the browser using an address
from the command line or clipboard.

Usage:
    mapit.py [ADDRESS]
Example addresses:
870 Valencia St, San Francisco, CA 94110

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import sys
import webbrowser
import logging

import pyperclip

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

class Mapit:
    def __init__(self, address:str) -> None:
        self.address = address
        
    def open_address(self):
        map_url = "https://www.google.com/maps/place/"
        webbrowser.open(map_url + self.address)

if __name__ == "__main__":
    # parse cli arguments
    if len(sys.argv) > 1:
        address = " ".join(sys.argv[1:])  # get args as a single string
    else:
        address = pyperclip.paste()  # get address from clipboard
    
    mapit = Mapit(address)
    log.debug("mapit address: %s", mapit.address)
    mapit.open_address()
