"""
This is the menu, which will eventually let you choose between autonomous routines and
telecom control, see current status of signals, and safely shut down the robot.

Date:
4/30/23
"""
import keyboard
import bot

print('You\'ve opened the menu! There\'s nothing here.')

while True:
#These menu options aren't working
    event = keyboard.read_event()
    
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
        sys.exit()
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'm':
        bot.move()