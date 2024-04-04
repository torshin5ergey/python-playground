# language_game.py - Translate message to one of the parody languages such as
# "Pig Latin" (eng) or "Salty (Blue) Language" (rus)

# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

# Get user message to translate
def get_message() -> str:
    message = input('Enter the message to translate:\n')
    return message

# Extract non-letter characters from the beginning and end of a word
def extract_non_letters(word: str) -> tuple:
        # Separate non-letters at the start of the current word
        non_letters_prefix = ''
        while len(word) > 0 and not word[0].isalpha():
            non_letters_prefix += word[0]
            word = word[1:]
        # Separate non-letters at the end of the current word:
        non_letters_suffix = ''
        while len(word) > 0 and not word[-1].isalpha():
            non_letters_suffix = word[-1] + non_letters_suffix
            word = word[:-1]
        # Return the cleaned word along with its prefix and suffix characters
        return word, non_letters_prefix, non_letters_suffix

# Translate a word into Pig Latin (eng)
def translate_to_piglatin(word: str) -> str:
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        # Append consonants to the prefix
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants:
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    # Return the word translated into Pig Latin
    return word

# Translate a word into Salty Language (rus)
def translate_to_salty(word: str) -> str:
    VOWELS = ('а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я')
    result = ''
    for char in word:
        result += char
        # Insert 'с' after the vowel
        if char in VOWELS:
            result += 'с' + char
    # Return the word translated into Salty Language
    return result

def main():
    user_message = get_message()

    # Translate message
    translated_message = [] # Translated words
    for word in user_message.split():
        # Extract non-letters and handle case
        word, prefix, suffix = extract_non_letters(word)
        if word.isalpha():
            was_title = word.istitle()
            was_upper = word.isupper()

            # Translate word to Pig Latin (Change to translate_to_salty if needed)
            word = translate_to_piglatin(word.lower())

            # Preserve original case
            if was_title:
                word = word.title()
            elif was_upper:
                word = word.upper()
        translated_message.append(prefix + word + suffix)

    # Output translated message
    print(' '.join(translated_message))

if __name__ == '__main__':
    main()