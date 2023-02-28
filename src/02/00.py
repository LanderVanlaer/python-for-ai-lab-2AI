# Create vector of ones, size 10, but the third value has to be 3.
# Output: [1. 1. 3. 1. 1. 1. 1. 1. 1. 1.]

import numpy as np

a = np.ones(10)
a[2] = 3

print(a)
