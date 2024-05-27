'''
multiplication_quiz.py - 

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''
#! python3

import random
import time
import pyinputplus as pyip


QUESTIONS_NUMBER = 10
SECS_PER_QUESTION = 8
ATTEMPT_LIMIT = 3

def main():  #  Main game loop
    correct_answers = 0
    for question in range(1, QUESTIONS_NUMBER+1):
        # Pick two random numbers
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)

        prompt = f'#{question}: {num1} × {num2} = '
        try:
            pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],  # Right answers
                                  blockRegexes=[('.*', 'Incorrect!')],  # Wrong answers
                                  timeout=SECS_PER_QUESTION, limit=ATTEMPT_LIMIT)  
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            print('Correct!')
            correct_answers += 1

        time.sleep(1)  # Brief pause to let user see the result

    print(f'Score: {correct_answers} / {QUESTIONS_NUMBER}')

if __name__ == "__main__":
    main()