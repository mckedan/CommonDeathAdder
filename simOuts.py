"""
This will be used to print displays to the standard output depending on what inputs
are read. For simulation only.


TODO:
Incorporate equation with updating graph
Done?  Needs testing. Only works for small timesteps - should be ok?: Figure out actual equation

Date:
8/19/23
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

#Find notes for this section
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

r_wheel = 12

"""
Calculate how the bot moves from two sides motor speeds;
Do this by considering it in two steps. First calculate how far the bot would
move in a straight line by using the lesser of the motor velocities.
Then calculate how the bot has turned by using the remainder of greaterVelocity - lesserVelocity
to pivot the bot
This might work, or might not.

x0 is initial x-position of bot in inches
y0 is initial y-position of bot in inches
theta0 is initial angle bot is facing, with positive x (to the right) being 0. theta0
    expressed in radians, going up to 2pi
omegaL is left motor speed in rpm
omegaR is right motor speed in rpm
tStep is the time step, how long the motors are run at these speeds in seconds
"""
def simPos(x0, y0, theta0, omegaL, omegaR, tStep):
    #start by converting motor speeds to distance of each train
    dL = omegaL*tStep*r_wheel*(2*math.pi/60)#dL is in inches
    dR = omegaR*tStep*r_wheel*(2*math.pi/60)#"
    
    #Compute how far the bot travels straight
    dStraight = min(dL, dR)
    xStraight = x0 + dStraight*math.cos(theta0)
    yStraight = y0 + dStraight*math.sin(theta0)
    
    dDiff = max(dL, dR) - min(dL, dR)
    
    turningLeft = dR > dL #if right wheels travel farther, bot will turn left
    turningRight = dL > dR

    if(turningLeft):
        xL = xStraight + w_bot/2 * cos(theta0 + math.pi/2) #xStraight is position of middle of bot, plus x component of half the width (distance to left wheels) use angle + 90deg to left to get proper angle
        yL = yStraight + w_bot/2 * sin(theta0 + math.pi/2) #same for y-position
        
        xR = xStraight + dDiff*math.cos(theta0) + w_bot/2 * cos(theta0-math.pi/2) #offset half the width of the bot similar to pivot side, also include dDiff along original angle to put the turning side ahead of the pivot side
        yR = yStraight + dDiff*math.sin(theta0) + w_bot/2 * sin(theta0-math.pi/2) #similar to above
        
    #Similar to above but now with other negative signs
    elif(turningRight):
        xL = xStraight + dDiff*math.cos(theta0) + w_bot/2 * math.cos(theta0+math.pi/2)
        yL = yStraight + dDiff*math.sin(theta0) + w_bot/2 * math.sin(theta0+math.pi/2)
        
        xR = xStraight + w_bot/2 * math.cos(theta0 - math.pi/2)
        yR = yStraight + w_bot/2 * math.sin(theta0 - math.pi/2)
        
    else:
        xL = 0
        yL = 0
        xR = 0
        yR = 0
    
    #Update x, y, theta
    x = xStraight + (xR - xL)/2
    y = yStraight + (yR - yL)/2
    theta = math.atan(y/x)
    
    return [x,y,theta]

"""
print(simPos(0,0,math.pi/2,60,60,1))
print(simPos(0,0,math.pi/4,60,60,1))
print(simPos(0,0,math.pi/2,60,45,1))
print(simPos(0,0,math.pi/2,60, 60, 3))
"""