# Create a 3x3 matrix with values ranging from -3 to 5.
# Output:
#   [[-3 -2 -1]
#    [ 0  1  2]
#    [ 3  4  5]]
import numpy

a = numpy.array(range(-3, 6))  # [-3 -2 -1  0  1  2  3  4  5]
a = a.reshape((3, 3))

print(a)
