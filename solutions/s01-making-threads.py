## Challenge 01
## Making Threads
#
# Here we have two functions FunctionOne and FunctionTwo - each one iterates a number of times,
# pausing each time and outputting the iteration count. The functions iterate a different number
# of times and pause different times.
#
# Your challenge: make these functions execute as threads and see what the output is - do they
# "interleave" with each other? What happens? What is the difference if deamon threads are used?
#

import time
import threading

def FunctionOne():
    for x in range(1,11):
        print("Hello number "+str(x)+" from FunctionOne")
        time.sleep(0.25)
    print("FunctionOne has finished")

def FunctionTwo():
    for y in range(1,6):
        print("Hello number "+str(y)+" from FunctionTwo")
        time.sleep(0.30)
    print("FunctionTwo has finished")


t1 = threading.Thread(target=FunctionOne)
t2 = threading.Thread(target=FunctionTwo)

t1.start()
t2.start()

# note if both are deamon threads the program exits straight away (at the end of main)
# what about if just FunctionOne is a daemon? (FunctionOne doesn't finish as FunctionTwo finishes first... and program exits)