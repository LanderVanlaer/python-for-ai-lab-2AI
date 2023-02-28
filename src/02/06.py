# Create and print a 5x5 matrix with values 4,3,2,1 one above the main diagonal.
#
# Output:
#   [[0 4 0 0 0]
#    [0 0 3 0 0]
#    [0 0 0 2 0]
#    [0 0 0 0 1]
#    [0 0 0 0 0]]

import numpy

a = numpy.diag(range(4, 0, -1), 1)

print(a)
