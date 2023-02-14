# Write a program that prints every command-line argument of your program, regardless of type
# (int, float, string, …). Only use positional arguments for this exercise and make use of sys.argv.
# Example:
#   python myprog.py test 20 5 apple
#   C:/Users/Johan/Documents/python4ai/exercises/myprog.py
#   test
#   20
#   5
#   apple

import sys

for arg in sys.argv:
    print(arg)
