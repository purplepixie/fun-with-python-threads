## Challenge 02
## Password
#
# Here's a simple password program, it allows you up to 5 attempts to get the right password
# Your challenge... only allow a maximum time (say 10 seconds!) using threads
#

PASSWORD="awesome"
ATTEMPTS=5

correct=False
attempt=0

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