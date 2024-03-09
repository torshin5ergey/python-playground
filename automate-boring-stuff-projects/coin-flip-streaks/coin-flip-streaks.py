# Coin FLip Streaks

import random

# Single experiment. Generates 100 random coin flips list.
# Checks if there is a streak (more than 5) in it.
def experiment():
	flips = [random.choice(['H', 'T']) for _ in range(100)] # H for head, T for tail
	# Finding a streak
	cur_streak = 1
	for i in range(len(flips)-1):
		if flips[i] == flips[i+1]:
			cur_streak += 1
			if cur_streak > 5: return True
		else: cur_streak = 1
	return False

# Runs simulation {num_simulations} times
def simulations(num_simulations):
	streaks = sum(1 for _ in range(num_simulations) if experiment())
	return streaks/num_simulations


streak_chance = simulations(10000) # Run simulations 10k times
print(f'Chance of streak (more than 5): {round(streak_chance*100)}%')

