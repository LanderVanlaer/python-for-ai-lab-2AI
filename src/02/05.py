# Create a 3x3 matrix with values ranging from 1 to 9 and add a border
# filled with the edge values of the existing matrix around that array.
#
# Output:
#   [[1 2 3]
#    [4 5 6]
#    [7 8 9]]
#
#   [[1 1 2 3 3]
#    [1 1 2 3 3]
#    [4 4 5 6 6]
#    [7 7 8 9 9]
#    [7 7 8 9 9]]

import numpy
from numpy import ndarray

a: ndarray = numpy.array(range(1, 10)).reshape((3, 3))
print(a)

a = numpy.pad(a, 1, 'edge')
print(a)
