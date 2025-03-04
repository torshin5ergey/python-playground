#! python3
# searchpypi.py - Opens several search results

import requests
import sys
import bs4
import webbrowser

# Get the command line arguments and request the search page
print("Searching...")
res = requests.get("https://google.com/search?q=" "https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links

# TODO: Open a browser tab for each result
