# The dictionary below contains names and values of chess pieces. Create a DataFrame from
# this dictionary, using the names as index. Next, ask the user for a value and print the
# corresponding name column from the DataFrame as a Series.
# pieces = {‘name’: [‘pawn’, ‘rook’, ‘bishop’, ‘knight’, ‘queen’], ‘value’: [1, 5, 3, 3, 9]}

import pandas as pd

pieces = {'name': ['pawn', 'rook', 'bishop', 'knight', 'queen'], 'value': [1, 5, 3, 3, 9]}

df = pd.DataFrame(pieces).set_index("name")

value = int(input("Enter a value: "))

print(df.loc[df["value"] == value].index.to_series().reset_index(drop=True))
