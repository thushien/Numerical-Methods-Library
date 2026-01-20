import numpy as np

def newton_raphson(func, dfunc, x0, tol=1e-6, max_iter=100):
    """
    Standard Newton-Raphson solver for finding roots of engineering equations.
    """
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        
        if abs(fx) < tol:
            return x, i
        
        x = x - fx/dfx
    return x, max_iter
