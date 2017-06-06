def thesum(x):
    thesum = 0 #keep track of the sum
    term = 1e7 # to store the individual terms being added
    n = 1  # Index
    while term > 1e-10:
        term = n * x**n  # Calculate this term
        thesum += term   # Update the sum
        n = n + 1        # increment index variable
    return thesum

x = 0.5
print thesum(x)
print x/(1 - x)**2
