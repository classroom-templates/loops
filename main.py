##########################
# 
# Your comment header here
# 
##########################

# this brings in the random number generator library 
# so we can use it to make random numbers
import random as rnd

# global constant to control pattern size
MAXSTARS = 10

# this defines main, but does not run it
def main():

    choice = 'y' # priming read
    while(choice == 'y'): # FIX THIS loop to work for y and Y
        
        n = rnd.randint(-MAXSTARS,MAXSTARS)

        # ############################################
        # WORK HERE
        # if negative number, print pattern
        # as shown in the examples
        
        # else if positive number print pattern
        # as shown in the examples
        
        # else print pattern shown
        # in the examples for 0
        #
        # ERASE THIS COMMENT BLOCK BEFORE YOU SUBMIT
        # ############################################
    
        choice = input("print another pattern? (y/n)")

    
# this runs main, i.e. it calls main
main()
