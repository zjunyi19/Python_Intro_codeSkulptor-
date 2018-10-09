# http://www.codeskulptor.org/#user45_JgrZbAfuFgo1pOd.py

# implementation of card game - Memory

import simplegui
import random

WIDTH=50;
HEIGHT=100;

numlist=[];
exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
turns=0;
state=0;
choices=[-1,-1];

# helper function to initialize globals
def init():
    global numlist,exposed,moves,state,choices;
    numlist=range(0,8);
    numlist.extend(range(0,8));
    random.shuffle(numlist);
    exposed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    turns = 0
    state = 0;
    choices = [-1,-1];
    label.set_text("Turns = "+str(turns));
    
# define event handlers
def mouseclick(pos):
    global choices, state, turns;
    index = int(pos[0]/WIDTH);
    if(state == 0):
        if(exposed[index]==0):
            if(numlist[choices[0]] != numlist[choices[1]]):
                exposed[choices[0]] = 0;
                exposed[choices[1]] = 0;
            exposed[index]=1;
            state=1;
            choices[0]=index;
    elif state == 1:
        if(exposed[index] == 0):
            state = 0;
            exposed[index] = 1;
            choices[1] = index;
            turns += 1;    
            label.set_text("Turns = "+str(turns));
            if not(0 in exposed):
                print "The game ended in "+str(moves)+" turns";
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(0,len(numlist)):
        if(exposed[index]==0):
            canvas.draw_polygon([(WIDTH*index,0), (WIDTH*(index+1), 0), (WIDTH*(index+1), 100),(WIDTH*index,100)],3,"Yellow","Blue");
        else:
            canvas.draw_text(str(numlist[index]),[WIDTH*index+5,HEIGHT-25],60,"White");
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label=frame.add_label("Turns = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()