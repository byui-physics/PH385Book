from numpy import exp, array
from matplotlib import pyplot
forwardErrors = []
centeredErrors = []
h = [0.1]
while h[-1] > 1e-30:
    print h[-1], 'h'
    dfForward = (exp(1 + h[-1]) - exp(1)) / h[-1]
    dfCentered = (exp(1+h[-1]) - exp(1 - h[-1]))/(2 * h[-1])
    forwardErrors.append(abs(dfForward/exp(1) - 1))
    centeredErrors.append(abs(dfCentered/exp(1) - 1))
    print exp(1 + h[-1]), 'subtract 1'
    print exp(1 - h[-1]), 'subtract 2'
    print exp(1 + h[-1]) - exp(1 - h[-1]), 'DIFF'
    h.append(h[-1]/2.)

pyplot.loglog(array(h[:-1]),forwardErrors)
pyplot.loglog(array(h[:-1]),centeredErrors)
pyplot.show()
