# Simulated exam results:
# Create a DataFrame containing 3 columns (‘theory’, ‘lab’ and ‘project’) and fill each of them
# with 45 random values from 0 to 100 (included), using a random seed of 42.
#
# Create a figure with four subplots, aligned in a 2x2 grid.
#
# Create a bar graph for ‘lab’, ‘project’ and ‘theory’ in the first three subplots (which one goes
# where: see result), and draw half of the values of ‘lab’ and ‘project’ on top of each other
# (‘project’ has to go on top of ‘lab’) in the last subplot to obtain a total percentage for the
# practical part (use the ‘bottom’ argument to do this)
#
# Make sure the color for lab, project and theory remain the same in all subplots.
# Write the value of each bar on top of it. In the last subplot, make sure the value is shown on a
# white transparent bounding box.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "lab": np.random.randint(0, 101, size=45),
    "theory": np.random.randint(0, 101, size=45),
    "project": np.random.randint(0, 101, size=45),
})

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
colors = ["orange", "b", "g"]

for i in range(0, 2):
    for j in range(0, 2):
        if i == 1 and j == 1:
            break
        index = i * 2 + j
        column = df.columns[index]
        ser = df[column]

        axs[i, j].set_ylim(0, 110)

        bar = axs[i, j].bar(ser.index, ser.values, color=colors[index])
        axs[i, j].bar_label(bar,
                            label_type="edge",
                            fontsize=9)
        axs[i, j].title.set_text(column)

axs[1, 1].set_ylim(0, 110)

axs[1, 1].bar(df.index, df["lab"].values / 2, color=colors[0])
bar = axs[1, 1].bar(df.index, df["project"].values / 2, bottom=df["lab"].values / 2, color=colors[2])
axs[1, 1].title.set_text("lab+project")
for t in axs[1, 1].bar_label(bar,
                             labels=(df["lab"].values + df["project"].values) / 2,
                             label_type="edge",
                             fontsize=9):
    t.set_bbox({'facecolor': 'white', "alpha": .5, "edgecolor": "None"})

plt.show()
