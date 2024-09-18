import csv 


#Define a function to display the main menu.
def display_menu():
    '''Prints the main menu options'''
    print ("-" * 50)
    print ("Hey there, Welcome to your personal task tracker")
    print ("-" * 50)
    print ("Select an option below to proceed\n")
    print("1. View tasks")
    print("2. Add new tasks")
    print("3. Modify tasks")
    print("4. Delete tasks")
    print ("5. Exit\n")


#Define a functio to get user input.
def get_user_input():


    while True:
        try:
            option = int(input("Enter  your choice: "))
            if 1<= option <=5:
                return option
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#Main program
def main():
    while True:
        display_menu()
        option = get_user_input()

        if option == 1:
            view_tasks()

        elif option == 2:
            add_task()

        elif  option == 3:
            modify_task()

        elif  option == 4:
            delete_task()
        elif  option == 5:
            print("Exiting the program. Goodbye!")
            break

def view_tasks():
    #This function will display all the tasks in the task list.
        readall_file()

def add_task():

        write_to_file()
    #This function will add a new task to the task list.
    #print("working on it")
    


def modify_task():
    #This function will modify an existing task in the task list.
    print("working on it ")

def delete_task():
    #This function will delete an existing task from the task list.
    print("working on it ")

def readall_file():
    with open("file1.csv",'r') as f:
             data=csv.reader(f)
             for i in data:
                print(i)
    print("\n")

def  write_to_file():
    with open("file1.csv",'a',newline='') as f:
        data=csv.writer(f)

        dt = input("Enter date and time in this format (01/11/2020, 08:45 AM ) : ")
        task = input("Enter task name : ")
        data.writerow([DATE & TIME, TASKS,  STATUS])

        print ("NEW TASK ADDED SUCESSFULLY ✅")


if __name__ == "__main__":
    main()









