#  Define a list to store tasks
tasks = []


#  Display the menu and get user input
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    return input("Choose an option (1-5): ")


# Add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")


#  View all tasks with their status
def view_tasks():
    if not tasks:
        print("No tasks to display!")
    else:
        print("\n--- To-Do List ---")
        task_number = 1
        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{task_number}. {task['task']} [{status}]")
            task_number += 1


# Mark a task as completed
def mark_task_completed():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


# Delete a task from the list
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


#Main loop to keep the program running
while True:
    choice = display_menu()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
