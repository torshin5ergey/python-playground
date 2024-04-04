# Language Translation Game

This script allows users to translate messages into parody languages such as Pig Latin (English) or Salty Language (Russian). It is inspired by a practice project [A Short Program: Pig Latin](https://automatetheboringstuff.com/2e/chapter6/#calibre_link-231) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

[Parody languages](https://en.wikipedia.org/wiki/Language_game) are constructed languages that humorously alter existing languages. They often involve playful transformations of words and syntax.
The program prompts the user to enter a message they wish to translate. Then the script splits the message into individual words and processes each word separately. The script preserves the original case (title case or uppercase) of words during translation.

### Translation

The words are translated into the desired parody language using specific translation functions:
- Pig Latin Translation: The translate_to_piglatin() function converts words into [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin). In Pig Latin, the first consonant or consonant cluster of each word is moved to the end of the word, followed by "ay" or "yay" if the word starts with a vowel.
- Salty Language Translation: The translate_to_salty() function transforms words into [Salty Language](https://ru.wikipedia.org/wiki/Поросячья_латынь#.D0.A0.D1.83.D1.81.D1.81.D0.BA.D0.B8.D0.B9_.D1.8F.D0.B7.D1.8B.D0.BA). Salty Language, a humorous parody of Russian, involves inserting the letter 'с' and vowel after each vowel in the word.

### Changing Translation Language

To use a different parody language for translation, simply replace the translation function in the line mentioned below.
```python
# Translate word to Pig Latin (Change to translate_to_salty if needed)
word = translate_to_piglatin(word.lower())
```
For example:
- Replace translate_to_piglatin with translate_to_salty to translate into Salty Language (Russian).
- Add your own translation function for another parody language and replace it accordingly.

## How to Run
1. Run the script `language_game.py`.
2. Enter the message you want to translate when prompted.

## Usage Example
```
$ python language_game.py
Enter the message to translate:
Hello world!
```
Output:
`Ellohay orldway!`

## Requirements

- Python 3.x

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)