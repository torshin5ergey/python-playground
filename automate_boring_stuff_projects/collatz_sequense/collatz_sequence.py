'''Collatz Sequence
Written by Sergey Torshin @torshin5ergey
'''

def collatz(number: int) -> None:
	try:
		# Checking the number for inconsistency with int type
		if not isinstance(number, int):
			raise TypeError # Raise TypeError exception
		print(number)
		# When the number equals 1, the function ends
		if number == 1:
			return None
		# If the number is even
		elif number%2 == 0:
			number//=2
			return collatz(number) # Recursive function call with new number
		# If the number is odd
		else:
			number = 3*number + 1
			return collatz(number) # Recursive function call with new number
	# If there is a TypeError exception, output an error message
	except TypeError:
		print("The argument must be an integer")

def main():
	# Examples
	collatz(5) # 5 16 8 4 2 1
	collatz('25') # The argument must be an integer
	collatz(25.7) # The argument must be an integer

if __name__ == '__main__':
	main()