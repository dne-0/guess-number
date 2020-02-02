import random

print("Guess the number between 0 and 20! You have 5 chances...")

numtg = random.randrange(0, 20)
chances = 4
guess = 21

while guess != numtg:
    guess = int(input("Guess: "))

    if guess < numtg:
        print("Too low! You have", chances, "chances...")
        chances = chances - 1

    if guess > numtg:
        print("Too high! You have", chances, "chances...")
        chances = chances - 1

    if guess == numtg:
        win = 1
        break
    
    if chances == 0:
        win = 0
        break

if win == 1:
    print("You got it! The number was", numtg)
else:
    print("You lost! Better luck next time!")