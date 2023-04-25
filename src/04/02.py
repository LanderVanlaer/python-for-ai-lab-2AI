# Expand the previous exercise by adding a new figure showing the histogram for the theory
# results. The bars corresponding to results <50 have to be colored in red. To do this, look up
# how the hist function’s return value ‘patches’ can help you. Tip: use set_facecolor

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({
    "theory": np.random.randint(0, 101, size=45),
})

fig = plt.figure(figsize=(10, 10))

_, _, bar_container = plt.hist(df["theory"], bins=100)
for r in bar_container.patches[:int(len(bar_container.patches) / 2)]:
    r.set_facecolor(color="red")

plt.show()
