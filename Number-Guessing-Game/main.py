import random

randomNumber = random.randint(1, 100)
attempts = 0
max_attempts = 10
guesses = []

while attempts < max_attempts:
    try:
        UserGuess = int(input(f"Attempt {attempts + 1}/10 - Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue

    guesses.append(UserGuess)
    attempts += 1

    if UserGuess == randomNumber:
        print(f"Your guess: {UserGuess}")
        print("Congratulations! You guessed it right!")
        break
    elif UserGuess < randomNumber:
        print("Too Low!")
    else:
        print("Too High!")

    print(f"Previous guesses: {guesses}")

    if attempts == max_attempts:
        print("\nYou've reached the maximum number of attempts.")
        print(f"The correct number was: {randomNumber}")
