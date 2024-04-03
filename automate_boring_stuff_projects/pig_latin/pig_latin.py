# pig_latin.py - Translate English to Pig Latin
# Written by Sergey Torshin @torshin5ergey
# Inspired by a practice project from Al Sweigart's book

# Get user message to translate
def get_message() -> str:
    message = input('Enter the English message to translate into Pig Latin:\n')
    return message

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
        
        return word, non_letters_prefix, non_letters_suffix

def translate_to_piglatin(word: str) -> str:
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants:
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    return word


def main():
    user_message = get_message()

    translated_message = [] # Words in Pig Latin
    for word in user_message.split():
        word, prefix, suffix = extract_non_letters(word)
        if word.isalpha():
            was_title = word.istitle()
            was_upper = word.isupper()
            word = translate_to_piglatin(word.lower())
            if was_title:
                word = word.title()
            elif was_upper:
                word = word.upper()
        #print(word, prefix, suffix, sep='-')
        translated_message.append(prefix + word + suffix)

    print(' '.join(translated_message))

if __name__ == '__main__':
    main()