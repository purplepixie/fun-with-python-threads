# Here we see a function SomeFunction being spun up as a thread
# Run the code a few times... what do we see?

import threading

def SomeFunction():
    print("Hello from the threaded function!")

print("Starting the program")
print("Starting the thread")

x = threading.Thread(target=SomeFunction)
x.start()

print("Have started the thread")
print("Main code finished")
