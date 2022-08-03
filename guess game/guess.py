#This is a guess the number game
import random

print("Hello. What is your name?")
name = input()

secretNumber = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20, take a guess...")

#print("DEBUG: Seret number is " + str(secretNumber))

#Ask the player to guess 6 times

for guessesTake in range(1,7):
    print("Take a guess...")
    guess = int(input())

    if guess < secretNumber:
        print("your guess is too low.")
    elif guess > secretNumber:
        print("your giess is too high.")
    else:
        break   #This condition is the correct guess!

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTake) + " guesses!")
else:
    print("Nope, the number i was thinking of was " + str(secretNumber) + " .")