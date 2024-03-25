# Multi-Clipboard Automatic Messages

This Python program is a multi-clipboard tool designed to store and retrieve commonly used phrases or texts. It is inspired by a practice project [Multi-Clipboard Automatic Messages](https://automatetheboringstuff.com/2e/chapter6/#calibre_link-223) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The Multi-Clipboard Program (`mclip.py`) is a Python script designed to enhance productivity by providing a convenient way to store and retrieve commonly used phrases or texts. Whether you're a programmer, writer, or anyone who frequently uses repetitive text snippets, this tool can save you time and effort by eliminating the need to retype or copy-paste text from various sources.

## How to Run

- **Manual Run:** Open a command prompt or terminal, navigate to the directory containing `mclip.py`, and run the script with the desired argument (e.g., `python mclip.py agree` or `python mclip.py list`).
- **Run with mclip.bat:** If you've added `mclip.bat` to your PATH, you can simply press Win+R, type `mclip` followed by the desired argument (e.g., `mclip agree` or `mclip -list`). But first you need to change path to `mclip.py` in `mclip.bat`.

## Contents

- `mclip.py`: The main Python script containing the multi-clipboard functionality.
- `mclip.bat`: A batch file for running `mclip.py` conveniently via the command line or Run (Win+R).
- `data.json`: JSON file containing keyphrase-text pairs for the answers.

## Usage
Usage:
    mclip [keyphrase] - copy phrase text
    mclip -add [keyphrase] [text] - add a new keyphrase and its text
    mclip -list - available keyphrases and messages
    mclip -help - print this help message

Examples:
    mclip intro
    mclip -list
    mclip -add keyphrase TextInOneWord
    mclip -add keyphrase "Text In Multiple Words"

## Customization:
You can customize the keyphrases and corresponding texts by editing the `data.json` file.

## Requirements

- Windows 10 or later
- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip) module

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
