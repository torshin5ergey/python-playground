# Multiplication Quiz

Simple quiz game where the user is asked multiplication questions and needs to provide the correct answers.
It is inspired by a practice project [Multiplication Quiz](https://automatetheboringstuff.com/2e/chapter8/#calibre_link-284) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The quiz randomly generates multiplication questions for the user to answer within a time limit.

### Quiz Rules

- The quiz consists of 10 multiplication questions.
- Each question presents two single-digit numbers to multiply.
- The user has a limited time (8 seconds) and attempts (3 attempts) to answer each question.
- If the user answers correctly, they score a point.
- At the end of the quiz, the user's score is displayed.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\automate_boring_stuff_projects\multiplication_quiz
```
3. Run Python file
```bash
python multiplication_quiz.py
```

## Usage Example

```
#1: 7 × 7 = 49
Correct!
#2: 4 × 7 = 28
Correct!
#3: 2 × 8 = 16
Correct!
#4: 8 × 8 = 64
Correct!
#5: 2 × 2 = 4
Correct!
#6: 7 × 2 = (blank input entered here)
Blank values are not allowed.
#6: 7 × 2 = 14
Correct!
#7: 6 × 4 = 24
Correct!
#8: 4 × 9 = 35
Incorrect!
#8: 4 × 9 = 36 (entered after 8 seconds of waiting)
Out of time! 
#9: 7 × 5 = 35
Correct!
#10: 6 × 9 = 54
Correct!
Score: 9 / 10
```

## Requirements

- [PyInputPlus](https://pypi.org/project/PyInputPlus/)~=0.2.12

## *Notes*

- The [PyInputPlus](https://pyinputplus.readthedocs.io/en/latest/) module provides methods for requesting input from the user, such as inputInt(), inputFloat(), inputChoice(), and inputMenu(). These methods allow you to request a specific type of data from the user (integer, floating point, list selection, etc.) and provide input validation by allowing you to set default values, limits on the number of attempts and range of valid values, and use regular expressions to allow or block certain input patterns.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
