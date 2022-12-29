"""
created by : aek426rahmani
date : 29-12-2022
"""
"""
naive approach is an optimization method that is used to find the global minimum of a function.
it is a very simple method that is used to find the global minimum of a function.
the way it works is that it starts from a random point and then it moves in the direction of the gradient.
it continues to move in the direction of the gradient until it reaches the global minimum.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
the problem is to find the minimum of the function 
f(x,y) = x^2 + exp(y) + 2xy + 2x - 2y + 9
while :
    x^2 + y^2 <= 25
    x - y <= 7
    x > 0
    y > 0
"""

# the function
def f(x,y):
    return x**2 + np.exp(y) + 2*x*y + 2*x - 2*y + 9

# the constraint
def g(x,y):
    return x**2 + y**2 - 25

# the constraint
def h(x,y):
    return x - y - 7


# solve the problem using naive approach method
def solve(f,g,h):
    # the gradient of the function
    def gradient(x,y):
        return np.array([2*x + 2*y + 2, np.exp(y) + 2*x - 2])

    # the step size of the gradient descent
    step_size = 0.01

    # the starting point
    x = np.random.uniform(0,5)
    y = np.random.uniform(0,5)

    # the number of iterations
    iterations = 100000

    # the minimum value
    min_value = f(x,y)

    # the minimum point
    min_point = np.array([x,y])

    # the values of the function at each iteration
    values = np.array([min_value])

    # the points of the function at each iteration
    points = np.array([min_point])

    # the number of iterations
    for i in range(iterations):
        # the gradient of the function
        grad = gradient(x,y)

        # the new point
        x = x - step_size*grad[0]
        y = y - step_size*grad[1]

        # the value of the function at the new point
        value = f(x,y)

        valueg = g(x,y)
        valueh = h(x,y)
        # check if the new point is feasible
        if valueg <= 0 and valueh <= 0 and x > 0 and y > 0.0:
            # check if the new point is better than the previous point
            if value < min_value:
                # update the minimum value
                min_value = value

                # update the minimum point
                min_point = np.array([x,y])

                # update the values of the function
                values = np.append(values,value)

                # update the points of the function
                points = np.append(points,min_point)

    # return the minimum value and the minimum point
    return min_value,min_point,values,points

def main():
    # solve the problem
    min_value,min_point,values,points = solve(f,g,h)

    # print the minimum value and the minimum point
    print("the minimum value is : ",min_value)
    print("the minimum point is : ",min_point)

    # the x and y values
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)

    # the x and y grids
    X,Y = np.meshgrid(x,y)

    # the z values
    Z = f(X,Y)

    # the figure
    fig = plt.figure()

    # the 3d axes
    ax = fig.add_subplot(111,projection='3d')

    # the surface
    ax.plot_surface(X,Y,Z,alpha=0.5)

    # the points
    ax.scatter(points[0::2],points[1::2],values,c='r',marker='o')

    # show the plot
    plt.show()

if __name__ == "__main__":
    main()