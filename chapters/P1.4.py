
from math import pi,sin,sinh
from numpy import arange,linspace,zeros,array,sin
from matplotlib import pyplot as plt
from scipy.special import jv

nPoints = 101
a = 0.
b = 5.

dx = (b - a)/(nPoints - 1)
x = arange(a,b+dx,dx)
x,dx = linspace(a,b,nPoints,retstep=True)   #Cell-edged grid
xCentered = arange(a + dx/2,b+dx/2,dx)  # Cell-centered grid
xGhost,dxGhost = linspace(a - dx/2, b + dx/2,nPoints,retstep = True)  #Cell-centered grid with ghost points (points outside of the domain).
y = jv(0,x)
print xGhost
print y
#plt.scatter(xGhost,y,linewidth = 3)
#plt.show()

fp = zeros(len(y))
print len(y[2:nPoints])
print len(y[0:nPoints-2])
print len(y[2:nPoints] - y[0:nPoints-2])
print y[2:nPoints] - y[0:nPoints-2]/(2 * dx)
fp[1:nPoints-1]=(y[2:nPoints]-y[0:nPoints-2])/(2*dx);

fpp = zeros(len(y))
fpp[1:nPoints-1]=(y[2:nPoints]-2*y[1:nPoints-1]+y[0:nPoints-2])/dx**2;

#fp[0]=2*fp[1]-fp[2]
#fp[nPoints-1]=2*fp[nPoints-2]-fp[nPoints-3]
#fpp[0]=2*fpp[1]-fpp[2]
#fpp[nPoints-1]=2*fpp[nPoints-2]-fpp[nPoints-3]

fp[0]=3*fp[1]-3*fp[2]+fp[3];
fp[nPoints-1]=3*fp[nPoints-2]-3*fp[nPoints-3]+fp[nPoints-4];
fpp[0]=3*fpp[1]-3*fpp[2]+fpp[3];
fpp[nPoints-1]=3*fpp[nPoints-2]-3*fpp[nPoints-3]+fpp[nPoints-4];
print max(fp)
print max(fpp)
plt.plot(xGhost,y,'r-',xGhost,fp,'g-',xGhost,fpp,'b-',linewidth=3)
plt.axis([0, 5, -1, 1])
plt.show()
