import random

def guess_game(l, h):
    number = random.randrange(l, h) # Get random number between [1 and 1000)
    guesses = 0
    guess = int(input(f"\nGuess my number between {l} and {h}: "))

    while guess != number:
        guesses += 1
        if guess > number:
            print(guess, "is too high.")
        elif guess < number:
            print(guess, "is too low.")
        guess = int(input("Guess again: "))

    print("\nGreat, you got it in", guesses,  "guesses!\n")
