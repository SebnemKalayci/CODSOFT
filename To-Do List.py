tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def deleteTask():
    if tasks:
        taskToDelete = input("Please enter a task to delete: ")
        if taskToDelete in tasks:
            tasks.remove(taskToDelete)
            print(f"Task '{taskToDelete}' deleted from the list.")
        else:
            print(f"Task '{taskToDelete}' not found in the list.")
    else:
        print("No tasks in the list to delete.")

def listTasks():
    if tasks:
        print("Tasks in the list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

if __name__ == "__main__":
    print("Welcome to your To Do List!")
    while True:
        print("\nPlease select one of the following options:")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")