# Comma code

# Function that takes a list value as an argument and returns a string with all
# the items separated by a comma and a space, with and inserted before the last
# item.
def comma_code(values):
	if not values:
		print('Error! Empty list was given.')
		return
	elif len(values) == 1:
		print(values[0] + '.')
		return
	items = ', '.join(values[:-1])
	print(f"{items}, and {values[-1]}.")


planets = [
			'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn',
			'Uranus', 'Neptune', 'Pluto', 'Earth'
			]
comma_code(planets)