# Strip Regular Expressions Version

Regular expression version of Python's **strip()** method.
It is inspired by a practice project [Regex Version of the strip() Method](https://automatetheboringstuff.com/2e/chapter7/#calibre_link-276) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

strip_regex.py is a script designed to provide a regular expression-based alternative to Python's built-in strip() method. The function utilizes regular expressions to identify and remove specified leading and trailing characters from input string. By default, it removes whitespace characters. 

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\autbor\strip_regex_version
```
3. Run Python file
```bash
python strip_regex.py
```

## Usage examples

### Usage example for strip_regex.py

```
>>> ***Regex Version of the strip() Method***
Regex Version of the strip() Method
```

### Usage example for strip_regex() function

1. Stripping whitespaces
```python
strip_regex('  Hello world  ') # Output: Hello world
```
2. Stripping multiple specific characters
```python
strip_regex('!!!Hello world!!!', '!') # Output: Hello world
```

## *Notes*

- **`re.sub()`** is used to replace parts of a string that match a given regular expression pattern.
- **`re.escape()`** is used for escaping all non-alphanumeric characters (e.g., *, +, ?, etc.) in a string so that they are treated as literal characters in the regular expression.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)