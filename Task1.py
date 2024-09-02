import random

def guessing_game():
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    if lower_bound >= upper_bound:
        print("Invalid bounds. Please enter a lower bound less than the upper bound.")
        return

    random_number = random.randint(lower_bound, upper_bound)

    max_guesses = int(input("Enter the maximum number of guesses: "))

    guess_count = 0
    while guess_count < max_guesses:
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print("Congratulations! You guessed the number in", guess_count + 1, "tries.")
            return
        elif guess < random_number:
            print("Try Again! You guessed too small.")
        else:
            print("Try Again! You guessed too high.")

        guess_count += 1

    print("Better Luck Next Time! The number was", random_number)

guessing_game()