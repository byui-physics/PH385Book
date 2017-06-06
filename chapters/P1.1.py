
from math import pi,sin,sinh
from numpy import arange,linspace
from matplotlib import pyplot as plt

nPoints = 100
a = 0
b = pi/2

dx = (b - a)/(nPoints - 1)
x = arange(a,b+dx,dx)
x = linspace(a,b,nPoints)   #Cell-edged grid
xCentered = arange(a + dx/2,b+dx/2,dx)  # Cell-centered grid
xGhost,dxGhost = linspace(a - dx/2, b + dx/2,nPoints + 1,retstep = True)  #Cell-centered grid with ghost points (points outside of the domain).
y = [sin(f) for f in xGhost]
print xGhost
print y
plt.scatter(xGhost,y,linewidth = 3)
plt.show()
