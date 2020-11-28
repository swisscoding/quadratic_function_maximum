#!/usr/local/bin/python3

import colored

print(colored.stylize("\n---- | Find maximum of quadratic function | ----\n", colored.fg("red")))

def f(x):
    return -x*x-6*x-8

qfunction = colored.stylize("-x² - 6x - 8", colored.fg("red"))
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

print(maxFunction(-4, -2, f, 0.0001))
