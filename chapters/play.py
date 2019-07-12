
def linearFunction(t,a,b):
    return a * t + b

class rWalker:

    def __init__(self,nWalkers,nSteps):
        from random import uniform
        from numpy import array
        self.nWalkers = nWalkers
        self.walkers = array([uniform(-.05,0.05) for n in range(self.nWalkers)])
        self.stepsize = 1.0
        
        self.nSteps = nSteps
        
    def rWalk(self,movie = True):
        from random import randint,uniform
        from numpy import mean
        from matplotlib import pyplot
        
        self.average = []
        for w in range(self.nSteps):
            for i in range(self.nWalkers):
                #walker = randint(0,self.nWalkers-1)
                direction = uniform(0,1)
                if direction < 0.5:
                    self.walkers[i] -= self.stepsize
                else:
                    self.walkers[i] += self.stepsize

            self.average.append(mean(self.walkers**2))

            if movie:
                for i in self.walkers:
                    pyplot.plot(w,i,'.')
                    #pyplot.xlim(-5,5)
                pyplot.draw()
                pyplot.pause(1e-8)
                #pyplot.clf()
    def plot(self):
        from matplotlib import pyplot
        from scipy.optimize import curve_fit
        pyplot.plot(self.average,'r.',markersize = 8)
        pyplot.xlabel('steps (time)',fontsize = 22)
        pyplot.ylabel(r'$\langle x^2\rangle$',fontsize = 22)
        pyplot.xticks(fontsize=22)
        pyplot.yticks(fontsize=22)
        t = range(self.nSteps)
        fitparams,fitUnc = curve_fit(linearFunction,t,self.average)
        self.line = t * fitparams[0] + fitparams[1]
        D = fitparams[0]/2
        print("The diffusion constant it {}".format(D))
        #        pyplot.plot(t,self.line)
        pyplot.show()


myWalkers = rWalker(500,100)
myWalkers.rWalk(movie=False)
myWalkers.plot()
        
