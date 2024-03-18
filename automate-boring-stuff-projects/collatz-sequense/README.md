# Collatz Sequence

This Python function generates a Collatz sequence for a given input integer. It is inspired by a practice project [Collatz Sequence](https://automatetheboringstuff.com/2e/chapter4/#calibre_link-150) from the book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart.

## Description

The [Collatz sequence](https://en.wikipedia.org/wiki/Collatz_conjecture) is a sequence of numbers where, for any positive integer 'n', if 'n' is even, divide it by 2, and if 'n' is odd, multiply it by 3 and add 1. This process is repeated until the sequence reaches the number 1.
This function takes an integer number as input and generates the Collatz sequence starting from that number. It recursively calls itself until the sequence reaches 1. If the input is not an integer, it raises a TypeError.

## Dependencies

Python 3.x

## Author 

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
