import random  # Import random module to generate random choices
import string  # Import string module for predefined character sets


def generate_password():
    print("\n--- Password Generator ---")
    try:
        # Ask the user for the desired password length, ensuring it's a valid number
        length = int(input("Enter the desired password length (minimum 6): "))

        if length < 6:
            print("Password length must be at least 6!")
            return

        # Prompt the user to select which character types to include
        print("Select the character types to include:")
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        include_digits = input("Include numbers? (y/n): ").lower() == "y"
        include_symbols = input("Include special characters? (y/n): ").lower() == "y"

        # Ensure at least one character type is selected
        if not (include_uppercase or include_lowercase or include_digits or include_symbols):
            print("You must select at least one character type!")
            return

        # Build a pool of valid characters based on user choices
        character_pool = ""
        if include_uppercase:
            character_pool += string.ascii_uppercase
        if include_lowercase:
            character_pool += string.ascii_lowercase
        if include_digits:
            character_pool += string.digits
        if include_symbols:
            character_pool += string.punctuation

        # Generate the password by randomly selecting characters from the pool
        password = "".join(random.choice(character_pool) for _ in range(length))

        # Display the generated password
        print(f"\nGenerated Password: {password}")
    except ValueError:
        # Handle invalid input for the length
        print("Invalid input! Please enter a valid number.")


# Main loop to allow generating multiple passwords
while True:
    generate_password()  # Call the password generation function
    repeat = input("\nDo you want to generate another password? (y/n): ").lower()

    # Exit the loop if the user doesn't want to generate another password
    if repeat != "y":
        print("Exiting Password Generator. Stay secure!")
        break
