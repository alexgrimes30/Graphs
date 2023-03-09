import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

symbol_x = sp.Symbol('x')
symbol_y = sp.Symbol('y')


def get_vector(a, b):
    return np.arange(a, b + 0.1, 0.1)


def plot_2d_function(function, a, b):
    # Create the sympy function f(x)
    f_x = sp.sympify(function)

    # Create domain and image
    domain_x = get_vector(a, b)
    image = [f_x.subs(symbol_x, value) for value in domain_x]

    # Plot the 2D function graph
    fig = plt.figure(figsize=(10, 10))
    plt.plot(domain_x, image)
    plt.grid(True)
    plt.show()


def plot_3d_function(function, a, b):
    # Create sympy function f(x, y)
    f_xy = sp.lambdify((symbol_x, symbol_y), sp.sympify(function))

    # Create domains and image
    domain_x = get_vector(a, b)
    domain_y = get_vector(a, b)
    domain_x, domain_y = np.meshgrid(domain_x, domain_y)
    image = f_xy(domain_x, domain_y)

    # Plot the 3D function graph
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(domain_x, domain_y, image,
                    rstride=1, cstride=1, cmap='viridis')
    plt.show()


function = input('>> Enter the function: ')
a_value = float(input('>> Enter the [a, ] value: '))
b_value = float(input('>> Enter the [, b] value: '))
if "x" and not "y" in function:
    plot_2d_function(function, a_value, b_value)
elif "x" and "y" in function:
    plot_3d_function(function, a_value, b_value)

else:
    print("You must enter a function in terms of x and/or y")
