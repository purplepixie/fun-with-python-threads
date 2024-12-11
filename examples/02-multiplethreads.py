# Here we start 10 threads and number them 0 to 9 (because programmers count from zero!)
# Run several times, do we see a difference in output?

import threading

def SomeFunction(num):
    print("Hello from the thread "+str(num))

print("Starting the program")
print("Starting threads")

for n in range(0,10):
    x = threading.Thread(target=SomeFunction,args=(n,))
    x.start()

print("Have started the threads")
print("Main code finished")
