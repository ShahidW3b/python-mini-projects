tasks = []

while True:

    print("\nTask Manager")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")

    chose = input("Choose an option: ")

    if chose == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

    elif chose == "2":
        print("Tasks:", tasks)

    elif chose == "3":
        task = input("Enter task to remove: ")
        tasks.remove(task)

    elif chose == "4":
        print("Goodbye")
        break
