import random 
secretNumber = random.randint(1, 10)

for guessesTaken in range(1, 4): 
    print("Take a guess")
    number = int(input())

    if number > secretNumber:
        print("Your guess is too high!")
    elif number < secretNumber:
        print("Your guess is too low!")
    else:
        break

if number == secretNumber:
    print("You guessed the number in " + str(guessesTaken) + " guesses")
else:
    print("Unfortunately you couldn't guess the number, the secret number was " + str(secretNumber))