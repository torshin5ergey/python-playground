# Updatable Multi-Clipboard

This program implements a word game called "Mad Libs" in CLI. Players fill in blanks in a story with various parts of speech, such as nouns, verbs, and adjectives, to create humorous or nonsensical stories.
It is inspired by a practice project [Mad Libs](https://automatetheboringstuff.com/2e/chapter9/#calibre_link-321) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

Mad Libs dynamically loads story files from a designated directory (`stories`), presents a menu for selecting a story, and allows users to choose specific versions of the story if multiple languages versions are available. Users are prompted to input words corresponding to blanks in the selected story, and the program replaces these blanks with user-provided words to generate a customized story.

## How to Run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground/autbor/mad_libs
```
3. Run Python file
```bash
python mad_libs.py
```

## Contents

- `mad_libs.py`: The main script.
- `./stories/`: Directory containing story text files in the format `story title-XX.txt`, where XX represents different versions of the story.
It must be in JSON format like the example below

## Usage

1. Select a Story (if there are more than one in the directory).
2. Choose Story Version (if there are more than one version e.g. en, ru, cn)
3. Fill in blanks (noun, verb, adjective)
4. Read your story:

## Example

```
--Mad Libs Game--

Select the story you want to play:
1. blumbing wizard
2. neon city
3. panda
>> 3

Let's play the Panda story!
>> Enter adjective: silly
>> Enter noun: chandelier
>> Enter verb: screamed
>> Enter noun: pickup truck

--Your text--

The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.
```

## Requirements

- [pyinputplus](https://pypi.org/project/PyInputPlus/)~=0.2.12

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
