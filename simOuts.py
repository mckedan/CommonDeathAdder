"""
This will be used to print displays to the standard output depending on what inputs
are read. For simulation only.


TODO:
Incorporate equation with updating graph
Figure out actual equation

Date:
6/12/23
"""
import math

""" Old idea, not best one.
OP = 5.3
def simO(OP):
    if OP > 0.9:
        print('-')
        print('here')
        
    #Designed for 0 < OP < 1
    for x in range(math.ceil(OP)*10)
        print('-')
    
    print('_')
return 0
"""

#width of the bot in inches
w_bot = 24
t = 1 #how do we determine the length of a timestep?

def simVels(x0, y0, omegaL, omegaR):
    sL = omegaL*t #t is ideally an actual time step, placeholder for now
    sR = omegaR*t
    
    RgtL = sL > sR
    
    if(RgtL):
        rL = w_bot * sL / (sR - sL)
        rR = w_bot + rL
    else:
        rL = -w_bot * sL / (sR - sL)
        rR = -w_bot + rL
    
    r = (rL+rR) / 2
    theta = (sL/rL + sR/rL)/2 #it feels better to take the average of theta calculated from right side and theta calculated from left side. Not sure why.
    
    xStep = math.cos(theta)*r
    yStep = math.sin(theta)*rL
    
    return [xStep, yStep]

print(simVels(0,0,24,48))