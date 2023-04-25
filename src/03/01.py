# Create a list mylist from the string ‘abcde’. Create a NumPy array myarr containing numbers
# from 0 to 5 (not included) using arange. Create a Series named ser1 from mylist. Create a
# Series named ser2 from myarr. Create a DataFrame from ser1 and ser2 and show the first 5
# lines using head.
# Output:
#     0 1
#   0 a 0
#   1 b 1
#   2 c 2
#   3 d 3
#   4 e 4
import numpy as np
import pandas as pd

mylist = list("abcde")
myarr = np.array(range(0, 5))
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
df = pd.DataFrame({0: ser1, 1: ser2})

print(df.head())
