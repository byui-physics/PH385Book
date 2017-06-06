def iterative(type):
    from math import exp,cos,sin
    lookup = {"exp": lambda x: exp(-x), "cos": lambda x: cos(x), "sin2": lambda x: sin(2 * x), "sin3": lambda x: sin(3 * x)}
    x =10
    xNew = 1e10
    while abs(x- xNew) > 1e-8:
        x = xNew
        xNew = lookup[type](x)
        print x, xNew


iterative("sin2")
