# Caesar's Cipher

from string import punctuation

# Choose language for encryption/decryption
def choose_language():
    while True:
        language = input("Choose the language (rus/eng): ").strip().lower()
        if language == "rus":
            return 1072, 32 # utf-8 russian alphabet start, alphabet cardinality
        elif language == "eng":
            return 97, 26 # utf-8 english alphabet start, alphabet cardinality
        else:
            print("Error! Please enter 'rus' or 'eng'.")

# Get shit/key number from input
def get_shift():
    while True:
        try:
            shift = int(input("Enter a shift number (negative for left shift): "))
            return shift
        except ValueError:
            print("Error! Please enter an integer")

# Encrypt/decrypt with Caesar Cipher
def do_caesar_cipher(text, shift, ord_start, cardinality):
    result = "" # Result text
    for i in text:
        # Keep punctuation and spaces unchanged
        if i.lower() in punctuation or i == " ": 
            result += i
        else:
            is_upper = i.isupper()
            # Character's offset from the starting point
            char_offset = ord(i.lower()) - ord_start
            # New offset for left shift
            if shift < 0:
                new_char_offset = (char_offset + shift) % cardinality
            # New offset for right shift
            else:
                new_char_offset = (char_offset + shift) % cardinality
            new_char = chr(ord_start + new_char_offset)
            result += new_char.upper() if is_upper else new_char # Preserve original case
    return result

def main():
    print()
    ord_start, cardinality = choose_language()
    shift = get_shift()
    orig_text = input("Enter your text: ")
    encrypted_text = do_caesar_cipher(orig_text, shift, ord_start, cardinality)
    print(f"Encrypted/decrypted text: {encrypted_text}\n")

if __name__ == "__main__":
    main()