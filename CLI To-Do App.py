# TO DO App

print("+++ TO DO App +++\n")

tasks = []


def add_task():
    task = input("Enter a task:\n")
    tasks.append(task)
    print("Task added!\n")


def show_tasks():
    if len(tasks) == 0:
        print("No task available.\n")

    else:
        print("\nYour tasks:\n")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        print()


def remove_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        remove = int(input("Enter task number to remove:\n"))

    except ValueError:
        print("Please enter a valid number!\n")
        return

    if 1 <= remove <= len(tasks):
        removed = tasks.pop(remove - 1)
        print(f"{removed} removed!\n")

    else:
        print("Invalid task number!\n")


while True:
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option:\n")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input!\n")