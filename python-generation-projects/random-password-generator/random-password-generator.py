# Random Password Generator

from random import choice
from string import digits, ascii_lowercase, ascii_uppercase, punctuation

# Remove ambiguous characters from the given string.
def remove_ambiguous(string):
	ambiguous = 'il1|0o8B3Evu![]{}.,`\'\"'
	return ''.join(i for i in string if i not in ambiguous)

# Prompt the user for a number input
def get_user_number(request):
	while True:
		try:
			num = int(input(f"{request} ").strip())
			if num < 1:
				print("Error! Number must be greater than 0")
			return num
		except ValueError:
			print("Error! Not an integer")

# Generate a password of the given length using the provided characters
def generate_password(length, chars):
	return ''.join(choice(chars) for _ in range(length))


print("\nWelcome to password generator.")
num_passwords = get_user_number("How many passwords to generate?")
password_len = get_user_number("How long should passwords be?")

password_chars = ""
if input("Include digits? (y/n): ").strip().lower() == "y":
	password_chars+=digits
if input("Include uppercase? (y/n): ").strip().lower() == "y":
	password_chars+=ascii_uppercase
if input("Include lowercase? (y/n): ").strip().lower() == "y":
	password_chars+=ascii_lowercase
if input("Include symbols (!#$ etc)? (y/n): ").strip().lower() == "y":
	password_chars+=punctuation
if input("Exclude ambiguous and similar symbols (il1 etc)? (y/n): ").strip().lower() == "y":
	password_chars = remove_ambiguous(password_chars)

for _ in range(num_passwords):
	print(generate_password(password_len, password_chars))