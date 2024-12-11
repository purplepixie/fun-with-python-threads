# Here we start 10 threads and number them 0 to 9 (because programmers count from zero!)
# each thread now sleeps a random time from 0ms to 1000ms
# Run several times, do we see a difference in output?

import threading
import time
from random import randint

def SomeFunction(num):
    delay = randint(0,1000)
    print("Hello from the thread "+str(num)+" I will sleep for "+str(delay)+" ms")
    time.sleep(delay/1000)
    print("Goodbye from thread "+str(num))

print("Starting the program")
print("Starting threads")

for n in range(0,10):
    x = threading.Thread(target=SomeFunction,args=(n,))
    x.start()

print("Have started the threads")
print("Main code finished")
