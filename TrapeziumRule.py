# trapezium rule (NUMERICAL INTEGRATION)
from __future__ import annotations
import numpy as np

def trapezium_rule(f:function, interval, deltax:float):
    a, b = interval[0], interval[1]
    yvalues = np.arange(a,b,deltax)
    s = 0
    for i in range(yvalues.size):
        if i == 0 or i == yvalues.size - 1:
            s += (deltax/2)*f(deltax*i)
        else:
            s += deltax*f(deltax*i)
    return s
    


