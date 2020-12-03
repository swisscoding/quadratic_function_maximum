#!/usr/local/bin/python3

import colored

"""
It is important to say that:
    - you have to define the interval in which the function has to search
    - you have to make sure that the function has a maximum
    - (qfunction var: make sure to update after changing function)
"""

print(colored.stylize("\n---- | Find maximum of quadratic function | ----\n", colored.fg("red")))

def f(x):
    # function to find maximum of
    return -x*x+4*x-1.5

# print out the function
qfunction = colored.stylize("-x² + 4x - 1.5", colored.fg("red"))
print(f"Quadratic function: {qfunction}\n")

def maxFunction(a,b,f,t):

    storeVar = 0
    variableVar = a

    while variableVar <= b:

        if f(variableVar) < f(storeVar):
            pass
        else:
            storeVar = variableVar

        variableVar += t

    return "Maximum of quadratic function at: " + colored.stylize(f"x = {round(storeVar)}", colored.fg("red")) + " and " + colored.stylize(f"y = {f(storeVar)}\n", colored.fg("red"))

# a and b is the interval, here a = 1 and b = 3
print(maxFunction(1, 3, f, 0.0001))
