class idealGas():
    def __init__(self,R=8.314,kB=1.38e-23):
        self.R = R
        self.kB = kB
    
    #Define what kind of ideal gas process we are dealing with
    def setProcessType(self,process, n,cV):
        self.n = n  #Set the number of moles of the gas
        self.process = process  #Indicate what kind of process it is:
                                # Isothermal, Isobaric, Adiabatic, Isochoric
        self.cV = cV
        self.cP = self.cV + self.R
        # If the process is adiabatic, we might need to know what gamma is.
        if process == 'Adiabatic':  
             self.gamma = self.cP/self.cV

    # Set the initial and final conditions for the process.
    def setConditions(self,pi=None,Vi=None,Ti=None,pf=None,Vf=None,Tf=None):
        self.pi = pi
        self.Vi = Vi
        self.Ti = Ti
        self.pf = pf
        self.Vf = Vf
        self.Tf = Tf

        #    def calcMissingQuantities():
        #if self.process == 'Adiabatic':

        #        else if self.process == 'Isothermal':

        #else if self.process == 'Isobaric':
        
    def isothermal(self):
        from math import log
        self.work = -self.n * self.R * log(self.Vf/self.Vi)
        self.deltaE = 0
        self.heat = - self.work
        
    def isochoric(self):
        self.work = 0
        self.heat = self.n * self.cV * (self.Tf - self.Ti)
        self.deltaE = heat
        
    def isobaric(self):
        self.work = - self.pI * (self.Vf - self.Vi)
        self.heat = self.n * self.cP * (self.Tf - self.Ti)
        self.deltaE = self.n * self.cV * (self.Tf - self.Ti)
        
    def adiabatic(self):
        self.heat = 0
        self.deltaE = self.n * self.cV * (self.Tf - self.Ti)
        self.work = self.deltaE

    # Depending on what type of process it is, calculate the work
    # done, heat absorbed, and change in internal energy for the process.
    def calculate(self):

        
        # These three lines can replace the lines below and its a really
        # cool use of dictionaries. Try it.
        #         processes = {'Isothermal':self.isothermal, 'Adiabatic':
        #   self.adiabatic, 'Isochoric':self.isochoric, 'Isobaric':self.isobaric}
        # processes[self.process]()

         if self.process == 'Isothermal':
             self.isothermal()
         elif self.process == 'Isochoric':
             self.isochoric()
         elif self.process == 'Isobaric':
             self.isobaric()
         else:  #Adiabatic
             self.adiabatic()

# Class definition done. What follows below illustrates how to use the class.
gasOne = idealGas()  #Initialize the class.
gasOne.setProcessType('Isothermal',3,20.8)  # Set the type of process and number of moles
gasOne.setConditions(pi = 2.0e5, pf = 1.0e5,Ti = 200, Tf = 200, Vi = 2, Vf = 5 )  # Set initial and final conditions
gasOne.calculate()  # Calculate thermodynamic properties.
print(gasOne.work)  # Print results
print(gasOne.deltaE)
