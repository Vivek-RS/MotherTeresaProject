import random  # Import random module to simulate dice roll


def roll_dice():
    while True:
        # Wait for the user to press Enter to roll the dice
        input("Press Enter to roll the dice...")

        # Generate a random number between 1 and 6 to simulate rolling a dice
        result = random.randint(1, 6)

        # Display the result of the dice roll
        print(f"You rolled a {result}!")

        # Ask the user if they want to roll again
        again = input("Roll again? (y/n): ")

        # If the user doesn't input 'y', break the loop and exit
        if again.lower() != 'y':
            print("Goodbye!")
            break


# Call the dice rolling function
roll_dice()
