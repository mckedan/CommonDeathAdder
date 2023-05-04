"""
This will be used to print different text displays to the standard output depending on what inputs
are read. For simulation only.

TODO:
Make this print text depending on what OP is received as argument.
May need to add methods to do this, and receive different/multiple parameters.
Need to make this return instead of print. Probably.
Currently it is set up as returning a single string for a single output, so would need
to be called twice (1 for left and 1 for right) by move method. May want to change this.

Date:
4/30/23
"""
import math

OP = 5.3

def simO(OP):
    if OP > 0.9:
        print('-')
        print('here')
        
    #Designed for 0 < OP < 1
    for x in range(math.ceil(OP)*10)
        print('-')
    
    print('_')
    
    
#Am drunk and idk if this works, I want it to print '-' on a new line ceil(OP) times, then print '_' at the end, also on a new line. Have not tested at all. Am drunk. Signing out.