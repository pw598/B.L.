from sympy import *

w, x, b = symbols("w x b")
y = tanh(w*x + b)
print(y)
print(diff(y, w))
print(diff(y, b))
