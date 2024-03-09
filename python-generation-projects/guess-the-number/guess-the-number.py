# Guess the number game

from random import randrange
from time import sleep

# Get user number for secret number range
def get_secret_ceil():
	while True:
		try:
			ceil = int(input("Enter the maximum natural number that can be guessed (at least 2): ").strip())
			if ceil < 2:
				print("Error! Number must be greater than 1")
			return ceil
		except ValueError:
			print("Error! Not an integer")

# Check user input
def is_valid(number, ceil):
	try:
		if 0 < int(number) < ceil+1:
			return True
		else:
			return False
	except ValueError:
		return False

# Print guessing animation
def animation(duration):
	FRAMES = ("|", "/", "-", "\\", "|", "/", "-", "\\")
	for _ in range(duration):
		for i in FRAMES:
			print(f"Guessing a number... {i}", end="", flush=True)
			print("\r", end="", flush=True)
			sleep(.125)


print("Welcome to Guess The Number game")
while True: # The main game loop
	user_secret_ceil = get_secret_ceil()

	animation(2) # animation for 3 seconds
	secret_number = randrange(1, user_secret_ceil+1)

	moves = 0
	print(f"Enter an integer from 1 to {user_secret_ceil}")
	while True: # The current game loop
		
		guess = input().strip()
		if not is_valid(guess, user_secret_ceil):
			print(f"Maybe you can enter an integer from 1 to {user_secret_ceil}?")
			continue
		
		else:
			moves+=1
			if int(guess) < secret_number:
				print("Your guess is too low, try again")
			elif int(guess) > secret_number:
				print("Your guess is too high, try again")
			else:
				print(f"You guess the number in {moves} guesses. Good job!")
				break
			
	if input("Would you like to try again? (y/n)\n").strip().lower() != "y":
		break

print("Thanks for playing the game. See you around...")