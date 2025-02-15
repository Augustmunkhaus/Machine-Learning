# This program generates random data that follows a quadratic pattern (y = 0.5 * x^2 + x + 2),
# fits a polynomial regression model of degree 2 to the data, and then plots both the data points
# and the best-fit quadratic curve.


import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X * X + X + 2 + np.random.randn(100, 1)
plt.plot(X,y, "g.")
plt.axis([-3,3,0,10])
poly_features = PolynomialFeatures(2, include_bias=False)
X_poly = poly_features.fit_transform(X)
lm = LinearRegression()
lm.fit(X_poly, y)
#fit function
f = lambda x: lm.coef_[0][1]*x*x + lm.coef_[0][0]*x + lm.intercept_
plt.plot(X,f(X), "b.")
plt.show()
