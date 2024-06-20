# Random Quiz Generator

A program to generate multiple-choice quizzes and corresponding answer keys based on a given dataset of questions and answers.
It is inspired by a practice project [Generating Random Quiz Files](https://automatetheboringstuff.com/2e/chapter9/#calibre_link-308) from the book [“Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The Random Quiz Generator reads quiz data from a JSON file and generates a specified number of quiz files, each containing a specified number of questions. Each question has multiple-choice answers, with one correct answer and a few wrong answers chosen randomly from the dataset.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground\automate_boring_stuff_projects\random_quiz_generator
```
3. *Change program options*
```python
# Change this to use a different dataset
quiz_name = 'country-capital'
# Change this to generate a different number of quiz files
quiz_num = 3
# Change this to include a different number of questions in each quiz
questions_num = 55  
# Change this to have a different number of answer options for each question
options_num = 4  
```
4. Run Python file
```bash
python random_quiz_generator.py
```

## Contents

- `random_quiz_generator.py`: The main script
- `country-capital.json`: A sample dataset containing country-capital pairs. You can use different datasets. It must be in JSON format like the example below
```json
{
    "question": "answer",
    "Greece": "Athens",
    "Russia": "Moscow",
    "Thailand": "Bangkok"
}
```
The name of the file must be `question-answer.json` only. It allows generate names of quizzes, questions, files regardless of the quiz subject. 
- `README.md`: This readme file.

## Example of generated files

### Quiz file (country-capital-quiz-1.txt)

```
Name:

Date:

Period:

                    Country-capital Quiz (Form 1)

1. What is the capital of Argentina?
    A. Paris
    B. Berlin
    C. Buenos Aires
    D. Tokyo

2. What is the capital of France?
    A. Rome
    B. Madrid
    C. Paris
    D. Lisbon
...
```

### Answer key file (country-capital-answer-1.txt)

```
1. C Buenos Aires
2. C Paris
...
```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)