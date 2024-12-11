# Here we use sleeping threads... to update a global variable

import threading
import time
from random import randint

x = 0

def SomeFunction(num):
    global x
    delay = randint(0,1000)
    print("Hello from the thread "+str(num)+", x="+str(x)+" and I will sleep for "+str(delay)+" ms")
    time.sleep(delay/1000)
    x = x+1
    print("Goodbye from thread "+str(num)+", x="+str(x))

print("Starting the program")
print("Starting threads")

for n in range(0,10):
    t = threading.Thread(target=SomeFunction,args=(n,))
    t.start()

print("Have started the threads")
print("Main code finished and x="+str(x))
