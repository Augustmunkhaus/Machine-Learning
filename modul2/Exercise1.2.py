# This program creates random data, finds a good line that fits the data by checking different line equations,
# and then shows the data points with the best line on a plot. It's not using gradient descent, just brute-force search.


import matplotlib.pyplot as plt
import numpy as np
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

def cost(a, b, X, y):
    ## Evaluate half MSE (Mean Squared Error)
    m = len(y)
    error = a + b * X - y
    J = np.sum(error ** 2) / (2 * m)
    return J

ainterval = np.arange(1, 10, 0.05)
binterval = np.arange(0.5, 5, 0.05)

best_a, best_b = None, None
min_cost = float("inf")

for atheta in ainterval:
    for btheta in binterval:
        cost_value = cost(atheta, btheta, X, y)
        if cost_value < min_cost:
            min_cost = cost_value
            best_a, best_b = atheta, btheta

print(f"Best theta0: {best_a}, Best theta1: {best_b}, Min Cost: {min_cost}")

plt.plot(X, y, "b.")  # Scatter plot of data
plt.plot(X, 4.35 + 2.85 * X, "r-", linewidth=2, label="Best Fit Line")
plt.legend()
plt.show()

#plt.plot(X,y, "b.")
#plt.axis([0,2,0,15])

#plt.plot()
#plt.show()

