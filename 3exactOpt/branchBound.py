"""
created by : aek426rahmani
date : 29-12-2022
"""
"""
branch and bound is an optimization method that is used to find the global minimum of a function.
it is a very simple method that is used to find the global minimum of a function.
the way it works is that it starts from a random point and then it moves in the direction of the gradient.
it continues to move in the direction of the gradient until it reaches the global minimum.
"""

import numpy as np
import matplotlib.pyplot as plt

"""
the problem is to find the minimum of the function
f(x) = cos(x) + 2sin(x) + x^2 - 2x
while :
    x^2 <= 25
    x > 3
"""

# the function
def f(x):
    return np.cos(x) + 2*np.sin(x) + x**2 - 2*x

# the constraint
def g(x):
    return x**2 - 25


# solve the problem using branch and bound method
def solve(f,g):
    # the gradient of the function
    def gradient(x):
        return np.array([np.sin(x) + 2*np.cos(x) + 2*x - 2])

    # the step size of the gradient descent
    step_size = 0.01

    # the starting point
    x = np.random.uniform(0,5)

    # the number of iterations
    iterations = 100000

    # the minimum value
    min_value = f(x)

    # the minimum point
    min_point = np.array([x])

    # the number of iterations
    for i in range(iterations):
        # the gradient of the function
        grad = gradient(x)
        # the new point
        new_point = x - step_size*grad

        # check if the new point is feasible
        if g(new_point) <= 0 :
            # update the minimum point
            min_point = new_point
            print(new_point)

            # update the minimum value
            min_value = f(new_point)

            # update the point
            x = new_point

        # check if the new point is not feasible
        else:
            # update the point
            x = new_point

    # return the minimum value and the minimum point
    return min_value,min_point

def main():
    # solve the problem
    min_value,min_point = solve(f,g)

    # print the minimum value and the minimum point
    print("minimum value : ",min_value)
    print("minimum point : ",min_point)

    # create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # the x values
    x = np.linspace(-10,10,1000)

    # the y values
    y = f(x)

    # plot the function
    ax.plot(x,y)

    # plot the minimum point
    ax.scatter(min_point,min_value)

    # show the plot
    plt.show()

if __name__ == "__main__":
    main()