# This program generates random data, computes the cost (MSE) for different values of theta0 and theta1,
# and visualizes the cost surface in 3D to show how the cost changes with different parameter values.


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def cost(a, b):
    # Evaluate half MSE (Mean Square Error)
    m = len(Ydots)
    error = a + b * Xdots - Ydots
    J = np.sum(error ** 2) / (2 * m)
    return J

Xdots = 2 * np.random.rand(100, 1)
Ydots = -5 + 7 * Xdots + np.random.randn(100, 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ainterval = np.arange(-10, 10, 0.05)
binterval = np.arange(-10, 10, 0.05)

X, Y = np.meshgrid(ainterval, binterval)
zs = np.array([cost(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
ax.set_xlabel('Theta0')
ax.set_ylabel('Theta1')
ax.set_zlabel('Cost')

plt.show()