# Write a program that calculates and prints the mean of the command-line arguments of your
# program. Make sure your program can handle any number of arguments and ensure the filename
# is skipped when calculating the mean! Only use positional arguments for this exercise and make
# use of sys.argv.
#
# Example:
#   python myprog.py 10 20 30 40
#   25.0

import sys

print(sum([int(x) for x in sys.argv[1:]]) / (len(sys.argv) - 1))
