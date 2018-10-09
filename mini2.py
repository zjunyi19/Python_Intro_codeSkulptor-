# http://www.codeskulptor.org/#user45_rkcFYF5B7uJrAaO.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

secret_number = 0
guess_left = 7
range = 100


# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0, range)
    print "New game. Rnage is [0," + str(range) + ")"
    print "Number of remaining guesses is " + str(guess_left)
    print ""
    
# define event handlers for control panel
def range100():
    global range
    global guess_left
    range = 100
    guess_left = 7

def range1000():
    global range
    global guess_left
    range = 1000
    guess_left = 10
    
def input_guess(guess):
    global guess_left
 
    guess_int = int(guess)
    guess_left = guess_left - 1
    print "Guess was " + guess
    print "Number of remaining guesses is " + str(guess_left)
    if guess > secret_number:
        print "Higher!"
    elif guess == secret_number:
        print "Correct!"
        return
    else:
        print "Lower!"
    print ""
    if guess_left == 0:
        print "You ran out of guesses. The number was " + str(secret_number)
        new_game()

    
# create frame
frame = simplegui.create_frame("Run", 350, 350)
frame.start()
button1 = frame.add_button("range100", range100)
button2 = frame.add_button("range1000", range1000)
frame.add_input("input guess", input_guess, 100)


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

