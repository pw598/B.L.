from sympy import *
from sympy.abc import w, x, b

y = tanh(w*x + b)
pprint(y)
pprint(diff(y, w))
pprint(diff(y, b))
