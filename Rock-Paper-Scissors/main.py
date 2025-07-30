import random

choices = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}

def get_user_choice():
    """Prompt the user to enter a valid choice."""
    while True:
        choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

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
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
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
