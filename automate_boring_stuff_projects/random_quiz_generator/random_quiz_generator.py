"""
random_quiz_generator.py -- Create quizzes with questions and answers in random
order, along with the answer key.

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

from typing import Dict
import random
import json


def read_quizdata(file) -> Dict[str, str]:
    """
    Reads quiz data from a JSON file.

    Args:
        file (str) -- The path to the JSON file containing quiz data.

    Returns:
        Dict[str, str] -- A dictionary where keys are questions and values are answers.
    """
    # Quiz data {question: answer}
    with open(file, 'r', encoding='utf-8') as f:
        filedata = json.load(f)
        return filedata


def main():
    """
    Main function to generate quiz and answer key files.
    """
    quiz_name = 'country-capital'  # JSON dataset filename
    quiz_data = read_quizdata(f'{quiz_name}.json')
    quiz_num = 3  # Generate N quiz files (can be changed to any other number)
    questions_num = 55  # Generate N questions in every quiz (can be changed to any other number)
    options_num = 4  # Number of options in every question (can be changed to any other number, more than 1)

    for quiz in range(1, quiz_num+1):
        # Create quiz and answer key files.
        quiz_file = open(f"{quiz_name}-quiz-{quiz}.txt", 'w', encoding='utf-8')
        answer_file = open(f"{quiz_name}-answer-{quiz}.txt", 'w', encoding='utf-8')
        # Generate header
        quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
        quiz_file.write((' ' * 20) + f"{quiz_name.capitalize()} Quiz (Form {quiz})")
        quiz_file.write("\n\n")
        
        # Shuffle questions order
        questions = list(quiz_data.keys())
        random.shuffle(questions)

        # Handle IndexError
        if questions_num > len(questions):
            questions_num = len(questions)
        # Loop through all questions
        for q in range(1, questions_num):
            # Get right and wrong answers
            correct = quiz_data[questions[q]]
            wrong = list(quiz_data.values())
            del wrong[wrong.index(correct)]
            wrong = random.sample(wrong, options_num-1)
            options = wrong + [correct]
            random.shuffle(options)
            
            # Write content to the quiz file
            quiz_file.write(f"""{q}. What is the {quiz_name.split('-')[1]} of {correct}?\n""")
            for i in range(options_num):
                quiz_file.write(f"\t{'ABCD'[i]}. {options[i]}\n")
            quiz_file.write('\n')
            
            # Write the anser to the key file
            answer_file.write(f"{q}. {'ABCD'[options.index(correct)]} {correct}\n")
        
        quiz_file.close()
        answer_file.close()

if __name__ == "__main__":
    main()
