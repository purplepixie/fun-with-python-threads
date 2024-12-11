# Here we do the same with sleeping threads but we set daemon=True
# What is different?

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
    x = threading.Thread(target=SomeFunction,args=(n,),daemon=True)
    x.start()

print("Have started the threads")
print("Main code finished")
