"""
create_files.py - Test `spamXXX.txt` files creator with random gaps
"""

import random


for i in range(10):
    name = f"00{i}"
    if random.randint(0, 1) == 1:
        open(f"spam{name}.txt", "w")
