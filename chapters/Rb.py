def thesum(N):
    thesum = 0
    for i in range(N + 1):
        thesum += i

    return thesum
n = 50
print thesum(n)
print n * (n + 1)/2

