# The dictionary below contains names and pseudo phone numbers of people. Create a
# DataFrame from this dictionary, using the names as index. Next, ask the user for a name and
# – if present - output the corresponding row from the DataFrame. If the name is not present in
# the DataFrame, print “Unknown name”. Keep asking for a name until the user enters q as a
# name.
#
# contacts = {‘name’: [‘Alice’, ‘Bob’, ‘Carol’, ‘Dave’, ‘Eve’], ‘nr’: [‘1234’, ‘4321’, ‘5678’, ‘8765’, 1010]}

import pandas as pd

contacts = {'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'], 'nr': ['1234', '4321', '5678', '8765', 1010]}
df = pd.DataFrame(contacts).set_index("name")

while (name := input("Enter your name: ")) != "q":
    if (row := df.T.get(name)) is not None:
        print(row)
    else:
        print("Unknown name")
