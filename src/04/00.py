# Create a figure of size 15x8 with two subplots, top and bottom.
# Create a NumPy array with 512 linear separated values from -2pi to +2pi.
# Using these values, draw a sine (in green, dotted) and a cosine (in orange, dash-dotted) in the
# top subplot.
# Add a legend for the top plot containing “sine” and “cosine”.
#
# In the bottom subplot, only draw the individual data points for the sine, marked by blue circles
# with a black border, but with no line connecting the points.
# Set the xticks and xticklabels for both subplots to display values as shown in the result

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 1, figsize=(15, 8))
arr512 = np.linspace(-2 * np.pi, 2 * np.pi, 512)

axs[0].plot(arr512, np.sin(arr512), "g:", linewidth=1, label="sine")
axs[0].plot(arr512, np.cos(arr512), "-.", color='orange', linewidth=1, label="cosine")
axs[0].legend()

arr64 = np.linspace(-2 * np.pi, 2 * np.pi, 64)
axs[1].scatter(arr64, np.sin(arr64), edgecolors="k", color="b")

for x in axs:
    x.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
                 [r"$-2\pi$", r"$-\pi$", r"0", r"$\pi$", r"$2\pi$"])
    x.set_yticks(np.linspace(-1, 1, 9))

plt.show()
