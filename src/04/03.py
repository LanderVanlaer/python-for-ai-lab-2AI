# Try to recreate the scatter plot from the Iris example in the slides. Use this code snippet to get
# the data:
#   from matplotlib.colors import ListedColormap
#   from sklearn.datasets import load_iris
#   iris = load_iris()
#   features = iris.data.T
#   sepal_length = features[0]
#   sepal_width = features[1]
#   petal_width = features[3]
# Create a scatter plot using:
#   - sepal length as x
#   - sepal width as y
#   - 100*petal width as size of each point
#   - class as color (the class is found in iris.target)
#   - transparency: alpha=0.2
#   - a ListedColorMap containing a list with ‘orangered’, ‘green’ and ‘blueviolet’
#
# Plot the x- and y-labels
# Add a colorbar with ticks [0, 1, 2] and tick labels [setosa, versicolor, virginica ]
# Set the colorbar limits from -0.5 to 2.5 to make sure that the labels are plotted in the vertical
# center of each color from the colorbar.

import matplotlib.colorbar
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T
sepal_length = features[0]
sepal_width = features[1]
petal_width = features[3]

cmap = ListedColormap(["orangered", "green", "blueviolet"])

plt.scatter(sepal_length, sepal_width, s=petal_width * 100, c=iris.target, alpha=.2, cmap=cmap)

plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")

plt.clim(-.5, 2.5)
cb: matplotlib.colorbar.Colorbar = plt.colorbar()
cb.set_ticks([0, 1, 2])
cb.set_ticklabels(["setosa", "versicolor", "virginica"])

plt.show()
