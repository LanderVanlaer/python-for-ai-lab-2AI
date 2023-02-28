# Create a vector with values ranging from 10 to 20. Print that vector.
# Next, reverse it and print the reversed vector.
#
# Output:
#   [10 11 12 13 14 15 16 17 18 19 20]
#   [20 19 18 17 16 15 14 13 12 11 10]

import numpy

a = numpy.arange(10, 21, 1)
print(a)
print(a[::-1])
