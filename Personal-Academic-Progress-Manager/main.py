subjects = {}


def show_menu():
    print("\n" + "=" * 45)
    print("     PERSONAL ACADEMIC PROGRESS MANAGER")
    print("=" * 45)

    print(" 1. Add a subject")
    print(" 2. Show all subjects")
    print(" 3. Search for a subject")
    print(" 4. Add a study session")
    print(" 5. Add a test score")
    print(" 6. Add a task")
    print(" 7. Show tasks")
    print(" 8. Mark a task as completed")
    print(" 9. Calculate a subject's average score")
    print("10. Calculate total study time")
    print("11. Show the subject with the highest average")
    print("12. Show a subject's progress percentage")
    print("13. Update subject status")
    print("14. Remove a subject")
    print("15. Exit")

    print("=" * 45)


def add_subject(subjects):
    print("\n--- Add Subject ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name in subjects:
        print("Subject already exists.")
        return

    progress = input(
        "Enter progress "
        "(Not Started / In Progress / Completed): "
    ).strip().title()

    subjects[sub_name] = {
        "progress": progress,
        "study_sessions": [],
        "scores": [],
        "tasks": []
    }

    print("Subject added successfully.")


def show_subjects(subjects):
    print("\n--- All Subjects ---")

    if len(subjects) == 0:
        print("No subjects found.")
        return

    subject_number = 1

    for subject in subjects:
        print(f"\nSubject number: {subject_number}")
        print(f"Subject: {subject}")
        print(f"Progress: {subjects[subject]['progress']}")
        print("-" * 30)

        subject_number += 1


def search_subject(subjects):
    print("\n--- Search Subject ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    subject_data = subjects[sub_name]

    print(f"\nSubject found: {sub_name}")
    print(f"Progress: {subject_data['progress']}")
    print(f"Study sessions: {subject_data['study_sessions']}")
    print(f"Scores: {subject_data['scores']}")

    if len(subject_data["tasks"]) == 0:
        print("Tasks: No tasks added.")
    else:
        print("Tasks:")

        for task_number, task in enumerate(
            subject_data["tasks"],
            start=1
        ):
            status = "Completed" if task["completed"] else "Pending"

            print(
                f"  {task_number}. "
                f"{task['name']} - {status}"
            )


def add_session(subjects):
    print("\n--- Add Study Session ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    try:
        session = float(
            input("How many hours have you studied? ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if session <= 0:
        print("Study time must be greater than zero.")
        return

    subjects[sub_name]["study_sessions"].append(session)

    print("Study session added successfully.")


def add_test_score(subjects):
    print("\n--- Add Test Score ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    try:
        test_score = float(input("Enter your test score: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if test_score < 0 or test_score > 100:
        print("The score must be between 0 and 100.")
        return

    subjects[sub_name]["scores"].append(test_score)

    print("Test score added successfully.")


def add_task(subjects):
    print("\n--- Add Task ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    task_name = input(
        "Enter the task you want to do: "
    ).strip().title()

    if not task_name:
        print("Task name cannot be empty.")
        return

    subjects[sub_name]["tasks"].append({
        "name": task_name,
        "completed": False
    })

    print("Task added successfully.")


def show_tasks(subjects):
    print("\n--- Show Tasks ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    tasks = subjects[sub_name]["tasks"]

    if len(tasks) == 0:
        print("No tasks found.")
        return

    print(f"\nTasks for {sub_name}:")

    for task_number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\nTask number: {task_number}")
        print(f"Task: {task['name']}")
        print(f"Status: {status}")
        print("-" * 30)


def complete_task(subjects):
    print("\n--- Mark Task as Completed ---")

    sub_name = input("Enter the subject name: ").strip().title()

    if sub_name not in subjects:
        print("Subject not found.")
        return

    tasks = subjects[sub_name]["tasks"]

    if len(tasks) == 0:
        print("No tasks found for this subject.")
        return

    print(f"\nTasks for {sub_name}:")

    for task_number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{task_number}. "
            f"{task['name']} - {status}"
        )

    try:
        selected_task = int(
            input("\nEnter the task number to complete: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if selected_task < 1 or selected_task > len(tasks):
        print("Invalid task number.")
        return

    selected_task_data = tasks[selected_task - 1]

    if selected_task_data["completed"]:
        print("This task is already completed.")
        return

    selected_task_data["completed"] = True

    print(
        f"Task '{selected_task_data['name']}' "
        "marked as completed."
    )


def subject_average(subjects):
    sub_name = input("Enter the subject name: ").title()
    if sub_name not in subjects: 
        print("Subject not found.")

    else: 
        
        scores = subjects[sub_name]["scores"]

        if len(scores) == 0: 
            print("No score found.")
            return
        
        total = 0

        for score in scores: 
            total += score

        average = total / len(scores)

        print(f"The average for {sub_name} is {average:.2f}")
                

    

def total_study_time(subjects):
    sub_name = input("Enter the subject name: ").title()
    if sub_name not in subjects: 
        print("Subject not found.")

    else: 

        study_sessions = subjects[sub_name]["study_sessions"]

        if len(study_sessions) == 0: 
            pri.nt("No study session found.")
            return

        total_time = 0 

        for session in study_sessions: 
             total_time += session

        print(f"Study time for {sub_name} is {total_time}")


def highest_average(subjects):
    highest_average = 0
    best_subject = ""

    for subject in subjects: 
        
        scores = subjects[subject]["scores"]

        if len(scores) == 0: 
            continue

        total = 0 

        for score in scores: 
            total += score

        average = total / len(scores)

        if average > highest_average:
            highest_average = average
            best_subject = subject

    if best_subject == "": 
        print("No scores available")
    else: 
        
        print(f"Best subject : {best_subjectsubject}")    
        print(f"Highest average : {highest_average:.2f}")


def subject_progress(subjects):
    sub_name = input("Enter the subject name: ").title()

    if sub_name not in subjects: 
        print("Subject not found.")
        return

    progress = subjects[sub_name]["progress"]
    print(f"{sub_name} Progress: {progress}")

def subject_update(subjects):
    sub_name = input("Enter the subject name: ").title()
    if sub_name not in subjects: 
        print("Subject not found.")
        return

    try: 
        progress = int(input("Enter new progress (0-100): "))

        if progress < 0 or progress > 100: 
            print("Progress must be between 0 and 100.")
            return

    except ValueError: 
        print("Please enter a valid number.")
        return

    subjects[sub_name]["progress"] = progress

    print(f"{sub_name} updated succsssfully.")


def subject_remove(subjects):
    sub_name = input("Enter the subject name: ").title() 
    if sub_name not in subjects: 
        print("Subject not found.")
        return

    del subjects[sub_name]

    print(f"{sub_name} has been removed successfully.")

while True:
    show_menu()

    choice = input("\nChoose an option (1-15): ").strip()

    if choice == "1":
        add_subject(subjects)

    elif choice == "2":
        show_subjects(subjects)

    elif choice == "3":
        search_subject(subjects)

    elif choice == "4":
        add_session(subjects)

    elif choice == "5":
        add_test_score(subjects)

    elif choice == "6":
        add_task(subjects)

    elif choice == "7":
        show_tasks(subjects)

    elif choice == "8":
        complete_task(subjects)

    elif choice == "9":
        subject_average(subjects)

    elif choice == "10":
        total_study_time(subjects)

    elif choice == "11":
        highest_average(subjects)

    elif choice == "12":
        subject_progress(subjects)

    elif choice == "13":
        subject_update(subjects)

    elif choice == "14":
        subject_remove(subjects)

    elif choice == "15":
        print("\nThank you for using the program.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please choose from 1 to 15.")
