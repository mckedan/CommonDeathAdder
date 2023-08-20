from SimBot import SimBot
import math

sBot = SimBot(0,0,math.pi/2)

steps = [0,0,0]

for i in range(3):
    #print(i)
    steps[i] = sBot.move(2, i, 1)

for i in steps:
    print(steps)