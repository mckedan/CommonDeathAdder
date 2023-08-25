"""
Class for a bot object that moves through simulation method.
To be instantiated and keep track of its position, uses simOuts as movement calculator

@author: DJM
@date: 8/19/23
"""
import simOuts as sim

class SimBot:
    def __init__(self, x0, y0, theta0):
        self.x = x0
        self.y = y0
        self.theta = theta0
    
    def move(self, omegaL, omegaR, tStep):
        return sim.simPos(self.x, self.y, self.theta, omegaL, omegaR, tStep)
        
    def currPos(self):
        return [self.x, self.y, self.theta]