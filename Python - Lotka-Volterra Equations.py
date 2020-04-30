'''
The Lotka-Volterra equations
(also called the Predator-Prey equations) are a set of differential equations that
depict the population dynamics of an ecosystem of a predator and a prey.
Denote by y1 and y2 the populations of
the prey and predator, respectively, at time t. The set of equations are then:
y_1'(t) = (a)(y_1) - (alpha)(y_1)(y_2)   AND
y_2'(t) = (-c)(y_2) + (gamma)(y_1)(y_2)
where a and c are the growth rate of the prey and the death
rate of the predator, respectively, and alpha and gamma are measures
of the effect of the interaction between the two species.
It would be interesting to see the plot, if we fix certain conditions on the parameters
and define various intial conditions...
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
%matplotlib inline

# The Lotka-Volterra Equation parameters.
# a = prey growth rate ; alph = prey decay rate (interaction) ; c = predator death rate ;
# gamm = predator growth rate (interation)
a = 1.0
alph = 0.5
c = 0.75
gamm = 0.25

#The Lotka-Volterra ODE system
def dydt(y, t=0.0):
    return np.array([a*y[0] - alph*y[0]*y[1],
                    -c*y[1] + gamm*y[0]*y[1]])

t = np.linspace(0 , 15, 1000)  #the time

# Below are the initial conditions

y0 = np.array([2.0,2.0])

y = integrate.odeint(dydt, y0, t)

prey, predator = y.T

#Plotting the figure (in this case, y0 = (2,2))

fig1 = plt.figure()
plt.plot(t, prey, color = 'red', label = 'Prey')
plt.plot(t, predator, color = 'blue', label = 'Predator')
plt.legend(loc='best')
plt.xlabel('Time [units]')
plt.ylabel('Count')
plt.title('Lotka-Volterra Equation Plot')
plt.grid(linestyle='dotted')
plt.show()
