# Rabin-Karp Algorythm

This script implements the **Rabin-Karp algorithm** for substring search.

## Description

The [Rabin-Karp](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) algorithm is a string-searching algorithm that efficiently finds a pattern within a text. It works by **hashing** the pattern and sliding a window across the text, checking for matches based on hash values.

## Algorithm

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

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground/ungrouped/rabin_karp
```
3. Run Python file
```bash
python rabin_karp.py
```
4. *Run unit tests file*
```bash
python test_rabin_karp.py
```
or
```bash
python -m unittest test_rabin_karp.py
```
This will run the unit tests and display the results.

## Contents

- `rabinkarp.py`: The Rabin-Karp algorithm in `rabin_karp()` function.
- `test_rabinkarp.py`: Unit tests for the `rabin_karp()` function  using Python's `unittest` framework.

### Unit tests

**Test class**: `TestRabinKarp`

**Included tests:**
- `test_smoke_rabin_karp()`: basic functionality tests (smoke tests).
- `test_edge_rabin_karp()`: edge tests.

## Usage example

```
Enter a string:
>>> Rabin Karp
Enter a substring:
>>> Karp
6
```

## *Notes*

- [**Hashing**](https://en.wikipedia.org/wiki/Hash_function): The algorithm relies on hashing to efficiently compare substrings.
- [**Rabin-Karp**](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
    - **d** is used to ensure that the hash is unique for each substring. In the Rabin-Karp algorithm, each character of a string is treated as a digit in a number system with base d. With d=256, the characters of the string are treated as numbers in the 256-item number system.
    - **q** is used to reduce collisions (situations where different substrings produce identical hashes). Using a prime number in modular arithmetic helps to distribute hashes more evenly, which reduces the probability of matching hashes for different substrings. In addition, modular division prevents overflow of hash values.
- In the Rabin-Karp algorithm hashes are computed modulo a large prime number q. This avoids integer overflow and reduces the probability of hash collisions.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)