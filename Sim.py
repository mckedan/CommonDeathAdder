from SimBot import SimBot
import math

sBot = SimBot(0,0,math.pi/2)

steps = [0,0,0] #need to make this a list of a 3 index array, not a 3 index array

for i in range(3):#And have this iterate through the LIST
    #print(i)
    steps[i] = sBot.move(2, 2, math.pi/2)
    continue

for i in steps:
    print(steps)