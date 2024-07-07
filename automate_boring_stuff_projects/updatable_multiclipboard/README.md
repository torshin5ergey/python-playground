# Updatable Multi-Clipboard

This Python program is another implementation of [multi-clipboard tool](../multiclipboard_automatic_messages/). It is inspired by a practice project [Updatable Multi-Clipboard](https://automatetheboringstuff.com/2e/chapter9/#calibre_link-313) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

`mcb.pyw` is a Python program designed to save and load pieces of text to and from the clipboard, allowing users to manage and reuse multiple clipboard entries efficiently. The program uses the shelve module to store clipboard contents persistently and the pyperclip module to interact with the system clipboard.

## How to Run

### Manual Run

1. Clone this repository
```
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```
cd python-playground\automate_boring_stuff_projects\updatable_multiclipboard
```
3. Run Python file with desired arguments (e.g.)
```
python mcb.pyw save <keyword>
```

### Run with mcb.bat

1. Change path to `mcb.pyw` in `mcb.bat`.
2. Add `mcb.bat` to your PATH.
3. Press <Win+R>, type `mcb` followed by the desired argument (e.g., `mcb save <keyword>` or `mclip list`). 

## Contents

- `mcb.pyw`: The main Python script containing the multi-clipboard functionality. File extension `.pyw` allows to run the script without a terminal window.
- `mcb.bat`: A batch file for running `mcb.pyw` conveniently via the command line or Run (Win+R).

## Usage

Usage:
```
mcb save <keyword> - Saves clipboard to keyword.
mcb <keyword> - Loads keyword to clipboard.
mcb list - Loads all keywords to clipboard.
```

Examples:
```
mcb save email (with test@email.com in the clipboard)
mcb email (test@email.com copied to the the clipboard)
mcb list (['email'] copied to the the clipboard)
```

## Requirements

- Windows 10 or later
- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip) module

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
