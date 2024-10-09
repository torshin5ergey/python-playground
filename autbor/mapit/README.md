# MapIt

A simple Python script that launches a map in the browser using an address
from the command line or clipboard.
It is inspired by a practice project [mapIt.py with the webbrowser Module](https://automatetheboringstuff.com/2e/chapter12/#calibre_link-373) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

MapIt allows users to quickly open Google Maps with a specified address. The address can be provided directly as a command-line argument or copied to the clipboard. This tool is useful for anyone who frequently needs to look up locations without manually entering them into a web browser.

## How to run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground/autbor/mapit
```
3. Run Python file with desired arguments (e.g.)
```
python mapit.py 870 Valencia St, San Francisco, CA 94110
```

## Usage
```
mapit.py [ADDRESS]

optional arguments:
  -h, --help            show this help message and exit
  ADDRESS
                        Address to open on Google Maps. If no address is provided, the script will attempt to retrieve the address from the clipboard.
```

### Examples

- Open a specific address:
```
python mapit.py 870 Valencia St, San Francisco, CA 94110
```
- Open a specific address (with the specific address stored in the clipboard). 
```
python mapit.py
```

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
