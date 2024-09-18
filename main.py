import csv
from datetime import datetime

# Define a function to display the main menu.
def display_menu():
    """Prints the main menu options"""
    print("-" * 50)
    print("Hey there, Welcome to your personal task tracker")
    print("-" * 50)
    print("Select an option below to proceed\n")
    print("1. View tasks")
    print("2. Add new tasks")
    print("3. Modify tasks")
    print("4. Delete tasks")
    print("5. Mark task as in progress or done")
    print("6. List all tasks that are done")
    print("7. List all tasks that are not done")
    print("8. List all tasks that are in progress")
    print("9. Exit\n")

# Define a function to get user input.
def get_user_input():
    """Gets user input and validates it"""
    while True:
        try:
            option = int(input("Enter your choice: "))
            if 1 <= option <= 9:
                return option
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Define a function to read all tasks from the file.
def read_all_tasks():
    """Reads all tasks from the file"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print("\n")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to add a new task to the file.
def add_task():
    """Adds a new task to the file"""
    with open("tasks.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        date_time = datetime.now().strftime("%m/%d/%Y, %I:%M %p")
        task = input("Enter task name: ")
        status = "Not Started"
        writer.writerow([date_time, task, status])
        print("NEW TASK ADDED SUCCESSFULLY ")

# Define a function to modify an existing task in the file.
def modify_task():
    """Modifies an existing task in the file"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task[1]}")
            task_number = int(input("Enter the task number to modify: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the new task name: ")
                tasks[task_number - 1][1] = new_task
                with open("tasks.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(tasks)
                print("TASK MODIFIED SUCCESSFULLY ")
            else:
                print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to delete an existing task from the file.
def delete_task():
    """Deletes an existing task from the file"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task[1]}")
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                with open("tasks.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(tasks)
                print("TASK DELETED SUCCESSFULLY ")
            else:
                print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to mark a task as in progress or done.
def mark_task():
    """Marks a task as in progress or done"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task[1]}")
            task_number = int(input("Enter the task number to mark: "))
            if 1 <= task_number <= len(tasks):
                status = input("Enter the new status (In Progress/Done): ")
                tasks[task_number - 1][2] = status
                with open("tasks.csv", 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(tasks)
                print("TASK STATUS UPDATED SUCCESSFULLY ")
            else:
                print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to list all tasks that are done.
def list_done_tasks():
    """Lists all tasks that are done"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            done_tasks = [task for task in tasks if task[2] == "Done"]
            if done_tasks:
                for task in done_tasks:
                    print(task)
            else:
                print("No tasks are done.")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to list all tasks that are not done.
def list_not_done_tasks():
    """Lists all tasks that are not done"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            not_done_tasks = [task for task in tasks if task[2] != "Done"]
            if not_done_tasks:
                for task in not_done_tasks:
                    print(task)
            else:
                print("All tasks are done.")
    except FileNotFoundError:
        print("No tasks available.")

# Define a function to list all tasks that are in progress.
def list_in_progress_tasks():
    """Lists all tasks that are in progress"""
    try:
        with open("tasks.csv", 'r') as file:
            reader = csv.reader(file)
            tasks = list(reader)
            in_progress_tasks = [task for task in tasks if task[2] == "In Progress"]
            if in_progress_tasks:
                for task in in_progress_tasks:
                    print(task)
            else:
                print("No tasks are in progress.")
    except FileNotFoundError:
        print("No tasks available.")

# Main program
def main():
    while True:
        display_menu()
        option = get_user_input()

        if option == 1:
            read_all_tasks()

        elif option == 2:
            add_task()

        elif option == 3:
            modify_task()

        elif option == 4:
            delete_task()

        elif option == 5:
            mark_task()

        elif option == 6:
            list_done_tasks()

        elif option == 7:
            list_not_done_tasks()

        elif option == 8:
            list_in_progress_tasks()

        elif option == 9:
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()