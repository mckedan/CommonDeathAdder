"""
This is the menu, which will eventually let you choose between operator control modes,
choose different autonomous routines to run (eventually), safely shut down the robot, etc.

The menu is launched initially, and should include options to start and stop operator control
of the robot. Pressing shit+m while driving the robot will pause robot movement and reopen the menu.

TODO:
Make move command call bot's move method

Date:
4/30/23
"""
import keyboard
import sys
from bot import move


print('This is the menu!')
print('Pressing \'m\' allows movement of the bot. Currently this means the throttle value will be printed. Throttle controlled by scrolling')
print('Pressing \'q\' will quit the menu.')
print('When in the move mode (after pressing \'m\') hold shift and press \'m\' to return to the menu here.')

while True:
    event = keyboard.read_event()
    
    print("in while")
    if event.event_type == keyboard.KEY_DOWN and event.name=='q':
        sys.exit()
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'm':
        print('Bot move method called')
        move()