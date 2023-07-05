"""
This is the main controller for the robot. Other supporting files will provide select functionality
but this module is what will be directing the robot and calling the other functions/files.

The move function records keyboard strokes & scroll wheel movement as inputs and calls other functions to produce outputs.

The open_menu function will provide a text-based menu to the terminal so the user can select 
different options and see statuses, (and check feedbacks?)

Currently the only way to end the program is ctrl+c

Date:
4/28/2023

TODO:
Make opening the menu an option
TODO:
Add in Control Outputs
TODO:
Make calculation for Control Outputs (throttle*dir +/- bias)
TODO:
Make simulation mode which reads input same way, and uses simOuts to display behavior
"""
import keyboard
import mouse

#g_straight = open('simTexts/0.txt', 'r').read()

exitToMain = False

def move():
    #Throttle will reset to 0 when entering the move mode
    throttle = 0
    
    print("throttle = 0, entering while")
    
    while True:
        keyboard.add_hotkey('shift+m', setExitTrue())
        
        mevents = []
        mouse.hook(mevents.append)
        
        mouse.unhook(mevents.append)
        if(len(mevents) != 0):
            scrs = []
            for x in range(len(mevents)):
                if(type(mevents[x]) == mouse.WheelEvent):
                    scrs.append(mevents[x].delta)
            
            if(len(scrs) != 0):
                throttle += sum(scrs)#/len(scrs)#sum should be used to capture entire range of mouse scroll, not just the average of the movement. This makes it less jerky, obviously.
                print(throttle)
        
        if(exitToMain):
            break

def setExitTrue():
    print('Exit bool set true')
    exitToMain = True
