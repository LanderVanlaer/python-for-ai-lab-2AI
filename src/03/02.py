# Create a string alphabet containing ‘abcdefgh’. Create a list rands containing 8 random
# integers from 0 to 8 using list comprehension. Create a list chars containing the characters
# from alphabet using the values from rands as indexes. Create a Series ser from chars and
# print the different unique values with their number of occurences.
# Example:
#   0 e
#   1 g
#   2 b
#   3 e
#   4 e
#   5 d
#   6 b
#   7 e
#   dtype: object
#   e 4
#   b 2
#   g 1
#   d 1
#   dtype: int64
import numpy as np
import pandas as pd

alphabet = "abcdefgh"
rands = [int(x * 8) for x in np.random.random(len(alphabet))]
chars = [alphabet[x] for x in rands]
ser = pd.Series(chars)

print(ser)
print(ser.value_counts())
