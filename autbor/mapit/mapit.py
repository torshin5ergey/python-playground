#! python3
"""
mapit.py - Launches a map in the browser using an address
from the command line or clipboard.

Usage:
    mapit
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
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        address = " ".join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    mapit = Mapit(address)
    log.debug("%s", mapit.address)
