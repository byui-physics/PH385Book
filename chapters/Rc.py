def thesum(x):
    thesum = 0
    for i in range(1,1001):
        thesum += i * x**i
    return thesum

x = 0.5
print thesum(x)
print x/(1 - x)**2
print thesum(1.5)
