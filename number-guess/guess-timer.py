from random import randint
import time
import threading

MIN=1
MAX=100
MAXGUESSES=10

TIME=30

n=randint(MIN, MAX)
guesses=0
correct=False

def Timer(totaltime):
    remain=totaltime
    while remain > 0:
        if (remain > 10 and (remain % 5)==0) or remain <= 10:
            print(str(remain)+" seconds remaining!")
        time.sleep(1)
        remain = remain - 1
    print("OUT OF TIME!")
    exit(0)


print("Find the secret number between "+str(MIN)+" and "+str(MAX))

timer = threading.Thread(target=Timer, args=(TIME,), daemon=True)
timer.start()

while not correct and guesses < MAXGUESSES:
    guesses = guesses+1
    print("Guess "+str(guesses)+" out of "+str(MAXGUESSES))
    try:
        guess = int(input("Enter your guess: "))
        if guess == n:
            print("Well done")
            correct = True
        elif guess > n:
            print("Too high!")
        else:
            print("Too low!")
    except ValueError:
        print("Sorry! You must enter a valid integer.")

if not correct:
    print("Better luck next time")
else:
    print("Congrats, you did it in "+str(guesses)+" guesses")