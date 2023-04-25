# Create a Series ser containing 35 random integers from 1 to 10. Create and print a DataFrame
# df of dimensions 7x5 from that Series.
import numpy.random
import pandas

ser = pandas.Series(numpy.random.randint(1, 10, 35))
df = pandas.DataFrame(ser.values.reshape(7, 5))

print(df)
