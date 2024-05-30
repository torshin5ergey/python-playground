# Strong Password Validator

A Python script for validating the **strength of a password** using regular expressions.
It is inspired by a practice project [Sandwich Maker](https://automatetheboringstuff.com/2e/chapter8/#calibre_link-288) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This Python script checks the strength of a password based on specific criteria using **regular expressions**.
Strong password criteria:
- The password must be at least 8 characters long.
- The password must contain both uppercase and lowercase letters.
- The password must include at least one digit.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\automate_boring_stuff_projects\strong_password_validator
```
3. Run Python file
```bash
python strong_password_validator.py
```
4. *Run unit tests file*
```bash
python test_strong_password_validator.py
```
or
```bash
python -m unittest test_strong_password_validator.py
```
This will run the unit tests and display the results.

## Contents

- `strong_password_validator.py`: 
- `test_strong_password_validator.py`: Unit tests for `strong_password_validator()` using unittest framework.
- `README.md`: This readme file.

### Unit tests

**Test class**: `TestStrongPasswordValidator`

**Included tests:**

- `test_strong()`: test for strong passwords.
- `test_weak()`: test for weak passwords.

## Usage example

```
Enter your password: 
>>> Adm1nAcc3ss
Your password is strong!
```

```
Enter your password: 
>>> password
Your password is weak(
```

## *Notes*

- The **unittest** module is utilized to test the `strong_password_validator()`. **`assertTrue`** and **`assertFalse`** is used to verify that a given expression evaluates to `True` or `False` respectively
## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)