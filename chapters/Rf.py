def theproduct():

    theproduct = 1.
    for n in range(1,100000000):
        theproduct *= 1. + 1./n**2
        if 1./n**2 < 1e-8:
            'exiting'
            break
    return theproduct

print theproduct()
from math import sinh,pi
print sinh(pi)/pi
