"""
This is the menu, which will eventually let you choose between operator control modes,
choose different autonomous routines to run (eventually), safely shut down the robot, etc.

The menu is launched initially, and should include options to start and stop operator control
of the robot. Pressing shit+m while driving the robot will pause robot movement and reopen the menu.

TODO:
Make menu keys reliably working
TODO:
Make move command call bot's move method

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