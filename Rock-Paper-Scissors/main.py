import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    """Prompt the user to enter a valid choice."""
    while True:
        choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter r, p, s.")

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(choices)

def display_choices(user_choice, computer_choice):
    """Print the choices with emojis."""
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    """Determine and print the result of the round."""
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    """Main game loop."""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
  play_game()
