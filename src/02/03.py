# Create a 3x3 array with random values from 0 to 9 and print the minimum and maximum value of that array.
# Example:
#   [0 1 1 3 9 2 8 7 8]
#   Xmin: 0
#   Xmax: 9
import numpy.random

a = numpy.random.randint(0, 9, (3, 3))

# noinspection PyArgumentList
print(a.flatten(), f"Xmin: {a.min()}", f"Xmax: {a.max()}", sep="\n")
