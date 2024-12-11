## Challenge 02
## Password
#
# Here's a simple password program, it allows you up to 5 attempts to get the right password
# Your challenge... only allow a maximum time (say 10 seconds!) using threads
#
import threading
import time
import os

PASSWORD="awesome"
ATTEMPTS=5
TIME=10 # maximum time allowed in seconds

correct=False
attempt=0

def Timer():
    global TIME # total max time in s
    global correct
    elapsed = 0 # time elapsed in ms (note difference to TIME s and ms)
    while not correct and elapsed < (TIME*1000):
        time.sleep(0.1) # sleep 100ms
        elapsed += 100
    print("Time is up - login failed")
    os._exit(0)

t = threading.Thread(target=Timer,daemon=True)
t.start()

while not correct and attempt < ATTEMPTS:
    attempt = attempt+1
    if input("Password: ") == PASSWORD:
        correct=True
    else:
        print("INCORRECT!")

if correct is True:
    print("Login successful")
else:
    print("Login failed")