# Bullet Point Adder

This Python program automates the process of adding bullet points or numbers to lists copied to the clipboard, facilitating quick formatting for various documents or presentations. It is inspired by a practice project [Adding Bullets to Wiki Markup](https://automatetheboringstuff.com/2e/chapter6/#calibre_link-227) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The Bullet Point Adder (`bpadder.py`) is a Python script that adds bullet points or numbers to the list from the clipboard. It takes the text from the clipboard, adds bullet points or numbers to each item, and then copies the modified list back to the clipboard.

## How to Run

- **Manual Run:** Open a command prompt or terminal, navigate to the directory containing `bpadder.py`, and run the script with the desired argument (e.g., `python bpadder.py` or `python bpadder.py 1`).
- **Run with bpadder.bat:** If you've added `bpadder.bat` to your PATH, you can simply press Win+R, type `bpadder` followed by the desired argument (e.g., `bpadder` or `bpadder --help`). But first you need to change path to `bpadder.py` in `bpadder.bat`.

## Contents
- `bpadder.py`: The main Python script containing the multi-clipboard functionality.
- `bpadder.bat`: A batch file for running `bpadder.py` conveniently via the command line or Run (Win+R).

## Usage
Usage:
    `bpadder` - Add bullet '*' to the list from clipboard. Then copy formatted list to clipboard.
    `bpadder 1` - Add numbers to the list from clipboard. Then copy formatted list to clipboard.
    `bpadder -h, --help`  - show help message and exit.

## Requirements

- Windows 10 or later
- Python 3.x

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)