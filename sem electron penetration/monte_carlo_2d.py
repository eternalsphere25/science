import numpy as np
import math
import matplotlib.pyplot as plt


def monte_carlo_2d(number_of_steps):

    #Set number of steps
    num_steps = number_of_steps

    #Step size
    step = 1

    #Set starting parameters
    x = np.zeros((1, num_steps+1))[0]
    y = np.zeros((1, num_steps+1))[0]
    cos_x = np.zeros((1, num_steps+1))[0]
    cos_y = np.zeros((1, num_steps+1))[0]

    cos_x[1] = 1.0

    #Set random numbers for each step
    r = np.random.rand(1, num_steps)
    theta = np.multiply(r, 2*np.pi)[0]

    #Simulate the random walk for num_steps
    for i in range(2,num_steps+1):
        cos_x[i] = cos_x[i-1]*math.cos(theta[i-1]) - cos_y[i-1]*math.sin(theta[i-1])
        cos_y[i] = cos_y[i-1]*math.cos(theta[i-1]) + cos_x[i-1]*math.sin(theta[i-1])
        x[i] = x[i-1] + step*cos_x[i]
        y[i] = y[i-1] + step*cos_y[i]

    #Distance from starting point
    s = math.sqrt(((x[num_steps] - x[1])**2) + ((y[num_steps] - y[1])**2))

    return x, y, s

def monte_carlo_2d_plot(xy_data):

    #2D plot of simulation
    fig, ax = plt.subplots()
    ax.plot(xy_data[0], xy_data[1])
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_axisbelow(True)
    plt.show()

"""
#Sample driver code
#Input number of steps
num_steps = int(input('\nInput number of steps:'))
data = monte_carlo_2d(num_steps)
monte_carlo_2d_plot(data)
"""