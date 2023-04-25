# Build on from previous assignment and only print the 2 most frequent values, in an ascending
# sorted way.
# Example:
#   0 h
#   1 b
#   2 b
#   3 h
#   4 a
#   5 c
#   6 c
#   7 c
#   dtype: object
#   b 2
#   c 3
#   dtype: int64

import numpy as np
import pandas as pd

alphabet = "abcdefgh"
rands = [int(x * 8) for x in np.random.random(len(alphabet))]
chars = [alphabet[x] for x in rands]
ser = pd.Series(chars)

print(ser)
print(ser.value_counts().sort_values(ascending=True).tail(2))
