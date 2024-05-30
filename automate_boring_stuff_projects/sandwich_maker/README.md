# Sandwich Maker

Python program for **making sandwiches**, along with a test suite to ensure its correctness.
It is inspired by a practice project [Sandwich Maker](https://automatetheboringstuff.com/2e/chapter8/#calibre_link-288) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

This Python program allows users to **create sandwiches** with various parameters such as bread type, protein, cheese, and additional extras. The program provides a **command line interface** for selecting these parameters and calculates the total cost of the sandwich.

To ensure the correctness of the program, the repository also includes **unit tests** that utilize the standard Python unittest framework.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\automate_boring_stuff_projects\sandwich_maker
```
3. Run Python file
```bash
python sandwich_maker.py
```
4. *Run unit tests file*
```bash
python test_sandwich_maker.py
```
or
```bash
python -m unittest test_sandwich_maker.py
```
This will run the unit tests and display the results.

## Contents

- `sandwich_maker.py`: Sandwich class, which allows users to customize their sandwiches by choosing the type of bread, protein, cheese, and additional extras.
- `test_sandwich_maker.py`: Unit tests for the Sandwich class using Python's unittest framework.
- `README.md`: This readme file.

### Sandwich class

**Attributes:**
- `bread_prices`: a dictionary with prices for various types of bread.
- `protein_prices`: a dictionary with prices for various types of protein.
- `cheese_prices`: a dictionary with prices for various types of cheese.
- `extra_prices`: a dictionary with prices for additional extras.
- `bread`: the chosen bread type.
- `protein`: the chosen protein type.
- `cheese`: the chosen cheese type.
- `extra`: a list of selected additional extras.
- `total_cost`: the total cost of the sandwich.

**Methods:**
- `choose_bread`: choose the bread type for the sandwich.
- `choose_protein`: choose the protein type for the sandwich.
- `choose_cheese`: choose the cheese type for the sandwich.
- `choose_extra`: choose additional extras for the sandwich.
- `alert_already_exists`: alert if the parameter is already chosen.
- `rechoose`: rechoose a parameter.
- `calculate_total`: calculate the total cost of the sandwich.

### Unit tests

**Test class**: `TestSandwich`

**Included tests:**
- `test_choose_bread`: test choosing bread for the sandwich.
- `test_choose_protein`: test choosing protein for the sandwich.
- `test_choose_cheese`: test choosing cheese for the sandwich.
- `test_choose_extra`: test choosing additional extras for the sandwich.
- `test_calculate_total`: test calculating the total cost of the sandwich.

## Usage example

```
What bread type would you prefer?
* wheat
* white
* sourdough
>>> wheat
What protein would you prefer?
* chicken
* turkey
* ham
* tofu
>>> turkey
Would you like to add cheese (y/n)? 
>>> y
What cheese would you prefer?
* cheddar
* Swiss
* mozarella
>>> Swiss
Would you like to add extras (y/n)?
>>> y
What extra would you prefer?
* mayo
* mustard
* lettuce
* tomato
>>> tomato
Would you like to add more extras (y/n)?
>>> y
What extra would you prefer?
* mayo
* mustard
* lettuce
>>> lettuce
Would you like to add more extras (y/n)?
>>> n
Total cost of your sandwich: 6.5€
```

## Requirements

- [PyInputPlus](https://pypi.org/project/PyInputPlus/)~=0.2.12

## *Notes*

- The Sandwich class serves as the core component of the project, exemplifying an **object-oriented** approach to programming. It encapsulates data about the sandwich (bread type, protein, cheese, extra ingredients) and methods to manipulate this data (parameter selection, total cost calculation).
- The **unittest** module is utilized to test the Sandwich class. Each method of the Sandwich class is tested for its correctness through corresponding unit tests. **Mocking** is utilized to simulate user inputs and external dependencies. **mock.side_effect** is used to specify sequence of return values when mocked function is called.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)