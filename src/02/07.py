# Create a 8x8 matrix and fill it with a chess board pattern using array slicing
# (start with 0 at the top left).
#
# Output:
#   [[0. 1. 0. 1. 0. 1. 0. 1.]
#    [1. 0. 1. 0. 1. 0. 1. 0.]
#    [0. 1. 0. 1. 0. 1. 0. 1.]
#    [1. 0. 1. 0. 1. 0. 1. 0.]
#    [0. 1. 0. 1. 0. 1. 0. 1.]
#    [1. 0. 1. 0. 1. 0. 1. 0.]
#    [0. 1. 0. 1. 0. 1. 0. 1.]
#    [1. 0. 1. 0. 1. 0. 1. 0.]]
import numpy

a = numpy.array([([(x + r) % 2 for x in range(8)]) for r in range(8)], dtype=float)

print(a)
