
def thesum():
    n = 1.
    term = 1e9
    thesum = 0
    while term > 1e-12:
        term = 1/n**2
        thesum += term
        n += 1
    return thesum

print thesum()

from math import pi
print pi**2/6    
