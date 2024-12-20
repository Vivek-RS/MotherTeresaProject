import random  # Import random module to simulate the computer's choice


def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    # Define the choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get the user's choice
        user_choice = input("Enter your choice (rock, paper, scissors). Type 'exit' to quit: ").lower()

        # Allow the user to quit the game by typing 'exit'
        if user_choice == 'exit':
            print("Goodbye!")
            break

        # Validate the user's input
        if user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Randomly select the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "scissors" and computer_choice == "paper") or \
                (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")


# Start the game
rock_paper_scissors()
