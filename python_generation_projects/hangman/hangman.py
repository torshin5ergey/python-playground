# Command-line Hangman

import random

WORD_LIST_CODING = ("Variable", 
                    "Function", 
                    "Loop", 
                    "Algorithm", 
                    "Array", 
                    "Object", 
                    "Class", 
                    "Method", 
                    "Parameter", 
                    "Interface", 
                    "Exception", 
                    "Compiler", 
                    "Framework", 
                    "Debugging", 
                    "Database", 
                    "Pointer", 
                    "Recursion", 
                    "Syntax", 
                    "Boolean", 
                    "Library")

# Get a random word from word list
def get_word(word_list: list) -> str:
    return random.choice(word_list)

# Print hangman based on the remaining tries
def display_hangman(tries: int) -> None:
    stages = (
'''
--------
| /    |
|/
|      
|      
|     
-
''', 
'''
--------
| /    |
|/     O
|      
|      
|     
-
''', 
'''
--------
| /    |
|/     O
|      |
|      |
|     
-
''', 
'''
--------
| /    |
|/     O
|     \\|
|      |
|     
-
''', 
'''
--------
| /    |
|/     O
|     \\|/
|      |
|     
-
''', 
'''
--------
| /    |
|/     O
|     \\|/
|      |
|     / 
-
''', 
'''
--------
| /    |
|/     O
|     \\|/
|      |
|     / \\
-
'''
)
    print(stages[tries])

# Display the current state of the secret word with guessed letters revealed
def display_word_completion(secret_word: str, guessed_letters: set) -> None:
    # Creating a string with guessed letters revealed and underscores for unrevealed letters
    result = ''.join(char if char.lower() in guessed_letters else '_' for char in secret_word)
    print(f"Word: {result}")

# Prompt the user to guess a letter or the whole word
def get_user_input() -> str:
    guess = input("Guess a letter or the whole word: ").lower().strip()
    return guess

# Play the Hangman game with the given secret word
def play(secret_word: str) -> str:
    while True: # Main game loop
        guessed = False
        guessed_letters = set()
        tries = 6
        while tries > 0: # Current round loop
            display_hangman(tries)
            display_word_completion(secret_word, guessed_letters)
            
            while True: # User guess loop
                guess = get_user_input()
                if not guess.isalpha():
                    print("Invalid input! Please enter only letters.")
                else:
                    # Check if the input is a single letter or the whole word
                    if len(guess) > 1:
                        if guess == secret_word.lower():
                            guessed = True
                            break
                        else:
                            print("Invalid input! Please enter a letter or the whole word")
                    else:
                        guessed_letters.add(guess)
                        # Check if all letters in the secret word have been guessed
                        if ''.join(sorted(set(secret_word.lower()))) == ''.join(sorted(set(guessed_letters))):
                            guessed = True
                        break
            if guessed:
                guessed_words.append(secret_word)
                break
            else:
                tries -= 1
                continue
        if guessed:
            print(f'You have guessed the Secred word "{secret_word}" in {6-tries} guesses.')
            return secret_word
        else:
            display_hangman(tries)
            display_word_completion(secret_word, guessed_letters)
            print("GAME OVER! The Hangman got You!")
            print(f"The Secred word was: {secret_word}.")
            break

def main():
    print("\nWelcome to Hangman game!")
    guessed_words = [] # Guessed words
    while True:
        play(get_word(WORD_LIST_CODING))
        print(f"You guessed {len(guessed_words)} words.")   
        if input("Do you want to play again? (y/n): ").lower().strip() != "y":
            break


if __name__ == '__main__':
    main()