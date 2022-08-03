from sympy import *

x = Symbol("x")
expression = x**2 * sin(cos(x))
print(expression)
print(diff(expression))
