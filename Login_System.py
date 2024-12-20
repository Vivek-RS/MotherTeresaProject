# Define a dictionary to store user credentials
users = {}


#Display the menu and get user input
def display_menu():
    print("\n--- Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Exit")
    return input("Choose an option (1-4): ")


#Register a new user
def register_user():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Please choose a different username.")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print(f"User '{username}' registered successfully!")


# Login an existing user
def login_user():
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if users[username] == password:
            print(f"Welcome, {username}! You are successfully logged in.")
        else:
            print("Incorrect password! Please try again.")
    else:
        print("Username not found! Please register first.")


# Change password for an existing user
def change_password():
    username = input("Enter your username: ")
    if username in users:
        old_password = input("Enter your current password: ")
        if users[username] == old_password:
            new_password = input("Enter your new password: ")
            users[username] = new_password
            print("Password changed successfully!")
        else:
            print("Current password is incorrect! Please try again.")
    else:
        print("Username not found! Please register first.")


# Main loop to keep the program running
while True:
    choice = display_menu()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        change_password()
    elif choice == "4":
        print("Exiting the Login System. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
