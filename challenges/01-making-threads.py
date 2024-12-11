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


FunctionOne()
FunctionTwo()