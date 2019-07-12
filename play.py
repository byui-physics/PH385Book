#!/usr/bin/python

#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from random import randint,random,sample,uniform,choice
from numpy import array,linalg,where,sum,exp,sin,abs,pi,arctan, arange,sqrt,cos,linspace,cross,mod,floor,dot,zeros,amax,copy,meshgrid
from numpy.linalg import norm



class spectral:

    def __init__(self):
        self.nSamples = nSamples

def f(x,c):
    return  exp(-(x - c)**2/8)
    if x < 0.5:
        return 5 * x
    else:
        return 5 - 5 * x


def DFT(samples):
    c = []
    N = len(samples)
    for k in range(N//2+1):
        thisC = 0
        for n,yn in enumerate(samples):
            thisC += yn * exp(-2j * pi * k * n/N)
        c.append(thisC)
    return c



def getTimeEvolved(x,t,coeffs,freq):
    val = 0
    for i,k in enumerate(coeffs):
        val += ( k.real * cos(2 * pi  * x * i/40) + k.imag * sin(2 * pi * x * i/40)) * cos(2 * pi * t * i/40)
        #        val += ( k.real * cos(2 * pi * freq[i] * x) + k.imag * sin(2 * pi * freq[i] * x)) * cos(2 * pi * freq[i] * t)

    return val

samplingTime = 40.  #32
fN = 0.5  #0.2 for a 1 Hz signal works really well to show aliasing.
dt = 1./(2. * fN)
print(dt, 'dt')
NSamples = int(samplingTime/dt)
x = linspace(0,samplingTime,NSamples)
y = [f(n,30) for n  in x]
c = DFT(y)
freq = linspace(0,fN,NSamples/2+1)
plt.figure(1)
plt.scatter(freq,abs(c))
plt.show()
print(NSamples, "samples")
xD = linspace(0,samplingTime,1000)
plt.figure(2)
print(NSamples)
for t in arange(0,25,0.1):
    signal = getTimeEvolved(xD,t,c,freq)



    plt.scatter(xD,signal)
    plt.ylim(-20,50)
    plt.xlim(0,40)
    plt.draw()
    plt.pause(0.0000000005)
    plt.clf()
