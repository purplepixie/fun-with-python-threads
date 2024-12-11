from random import randint

MIN=1
MAX=100
MAXGUESSES=10

n=randint(MIN, MAX)
guesses=0
correct=False

print("Find the secret number between "+str(MIN)+" and "+str(MAX))

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