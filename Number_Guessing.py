import random  # Import random module to generate a random number

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # To count the number of attempts made

    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempts on each guess

            # Check if the guess is correct, too low, or too high
            if guess < secret_number:
                print("Low! Try again.")
            elif guess > secret_number:
                print("High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop once the user guesses correctly
        except ValueError:
            # Handle the case when the user doesn't enter a valid integer
            print("Please enter a valid number.")

# Start the game
number_guessing_game()
