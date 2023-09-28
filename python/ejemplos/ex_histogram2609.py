import numpy as np
import matplotlib.pyplot as plt

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 50

# the histogram of the data
n, bins, patches = plt.hist(x, bins=num_bins, density=True, facecolor='green', alpha=0.5)

# add a 'best fit' line
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(bins - mu)**2 / (2 * sigma**2))
plt.plot(bins, y, 'r--')

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(f'Histogram of IQ: $\mu={mu}$, $\sigma={sigma}$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)

# Save the figure in EPS format
plt.savefig("hist.eps", format='eps')

# Show the plot (optional)
plt.show()
