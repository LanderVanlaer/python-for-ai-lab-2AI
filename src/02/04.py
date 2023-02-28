# Create a 3x3 matrix with values ranging from 1 to 9 and add a border filled with 0’s around that array.
# Output:
#   [[1 2 3]
#    [4 5 6]
#    [7 8 9]]
#
#   [[0 0 0 0 0]
#    [0 1 2 3 0]
#    [0 4 5 6 0]
#    [0 7 8 9 0]
#    [0 0 0 0 0]]
import numpy
from numpy import ndarray

a: ndarray = numpy.array(range(1, 10)).reshape((3, 3))
print(a)

a = numpy.pad(a, 1, 'constant')
print(a)
