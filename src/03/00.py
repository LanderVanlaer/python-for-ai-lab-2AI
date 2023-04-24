# Create a list mylist from the string ‘abcde’. Create a NumPy array myarr containing numbers
# from 0 to 5 (not included) using arange. Create a dictionary mydict from mylist and myarr
# using zip. Create a Series object from mydict and print the first 4 lines using head.
#
# Output:
#    a 0
#    b 1
#    c 2
#    d 3
#    e 4
#    dtype: int32

import numpy as np
import pandas as pd

mylist = list("abcde")
myarr = np.array(range(0, 5))

mydict = dict(zip(mylist, myarr))

myserie = pd.Series(mydict)

print(myserie.head())
