import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x, y)