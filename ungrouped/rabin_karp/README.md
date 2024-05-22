# Rabin-Karp Algorythm

This script implements the Rabin-Karp algorithm for substring search.

## Description

The Rabin-Karp algorithm is a string-searching algorithm that efficiently finds a pattern within a text. It works by hashing the pattern and sliding a window across the text, checking for matches based on hash values.

## Algorythm

0. **Initialization**:
    - `n`: string length
    - `m`: substring length
    - `q`: prime modulus
    - `d`: ASCII alphabet size
1. **Calculate Hashes**: Calculate hashes substring and first `m` string characters window.
2. **Compare Hashes**:
    1. If the hashes are equal, output the current index.
    2. If the hashes are not equal, recalculate the hash for the next `m`-character window of the string. Remove the hash of the first character and add the hash of the next character.
    3. If no matches are found, output -1.

## Contents

- `rabinkarp.py`: The Rabin-Karp algorithm in `rabin_karp()`.
- `test_rabinkarp.py`: Unit tests for the Rabin-Karp algorithm function.

## *Notes*

- [**Hashing**](https://en.wikipedia.org/wiki/Hash_function): The algorithm relies on hashing to efficiently compare substrings.
- [**Rabin-Karp**](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
    - **d** is used to ensure that the hash is unique for each substring. In the Rabin-Karp algorithm, each character of a string is treated as a digit in a number system with base d. With d=256, the characters of the string are treated as numbers in the 256-item number system.
    - **q** is used to reduce collisions (situations where different substrings produce identical hashes). Using a prime number in modular arithmetic helps to distribute hashes more evenly, which reduces the probability of matching hashes for different substrings. In addition, modular division prevents overflow of hash values.
- In the Rabin-Karp algorithm hashes are computed modulo a large prime number q. This avoids integer overflow and reduces the probability of hash collisions.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)