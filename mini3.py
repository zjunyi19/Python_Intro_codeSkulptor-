# http://www.codeskulptor.org/#user45_CO5G0BicFNbPWhb.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
msec = 0
isStop = True
num_try = 0
num_exact_stop = 0
msec_limit = 10*60*60

# define helper function format that  converts time
# in tenths of seconds into formatted string A:BC.D
def print_time(num):
    if num < 10 : 
        return "0"+str(num)
    return str(num)

def format(t):
    left_sec = msec / 10
    return str(left_sec / 60)+":"+print_time(left_sec % 60)+":"+str(msec % 10)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isStop
    isStop = False

def stop():
    global isStop, num_try, num_exact_stop
    
    if not isStop :
        num_try += 1
        if msec % 10 == 0:
            num_exact_stop += 1
        
    isStop = True    

def reset():
    global isStop, msec, num_try, num_exact_stop
    isStop = True
    msec = 0
    num_try = 0
    num_exact_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global msec
    if not isStop  :
        msec += 1
    # if timer exceed 60 minutes, then set to 0
    if msec >= msec_limit :
        msec = 0

# define draw handler
def draw(canvas):
    canvas.draw_text(format(msec), [100,100], 50, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
timer.start()

# start frame
frame.start()