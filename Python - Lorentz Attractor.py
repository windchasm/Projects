'''
Chaotic systems are systems that are highly sensitive to initial conditions and perturbations.
Given specific initial conditions, the system might look predictable initially, but then
start to become chaotic, behaving unpredictably.
The Lorenz equations are a set of first-order ordinary differential equations,
which were initially developed to model the weather. The set of equations is given by:
y_1' = (sigma)(y_2 - y_1)
y_2' = (y_1)(rho - y-3) - y_2
y_3' = (y_1)(y_2) - (beta)(y_3)
where sigma, rho, and beta are systematic parameters.
It would be interesting to see a plot of this...
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

#Defining the Lorenz attractor

def lorenz(x, y, z, sigma=10, rho=28, beta=2.667):
    x_dot = sigma*(y - x)
    y_dot = x*(rho - z) - y
    z_dot = x*y - beta*z
    return x_dot, y_dot, z_dot

dt = 0.01 #The step size
num_steps = 5000
xs = np.empty((num_steps + 1,))
ys = np.empty((num_steps + 1,))
zs = np.empty((num_steps + 1,))

# The initial values
xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# Calculate the partial derivatives at the current point. Use them to approximate the sequential point.
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure(figsize=(12,10))
ax = fig.gca(projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("x-Axis")
ax.set_ylabel("y-Axis")
ax.set_zlabel("z-Axis")
ax.set_title("Lorenz Attractor")
plt.show()
