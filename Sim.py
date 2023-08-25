from SimBot import SimBot
import math

sBot = SimBot(0,0,math.pi/2)

steps = []

for i in range(3):
    print("Pre-Step", i, ":", sBot.currPos())
    steps.append(sBot.move(2, 2, math.pi/2))
    print("Post-Step", i, ":", sBot.currPos())

print(steps)

#Looks like sBot object isn't being updated but its output is being stored in the array -- need to update global variable in sBot object when move method is run