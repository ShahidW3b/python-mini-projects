print("========================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("========================================")

names = []
IDs = []
ages = []
majors = []
GPAs = []

while True:
    print("\n1. Add a student")
    print("2. Show all students")
    print("3. Search for a student")
    print("4. Remove a student")
    print("5. Show student with highest GPA")
    print("6. Show student with lowest GPA")
    print("7. Update student GPA")
    print("8. Show total number of students")
    print("9. Exit")

    print("----------------------------------------")
    choice = input("Choose an option (1 - 9): ")

    if choice == "1":

        print("\n---------- ADD A STUDENT ----------")

        name = input("Enter student name: ")
        ID = int(input("Enter student ID: "))
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        gpa = float(input("Enter student GPA: "))

        names.append(name)
        IDs.append(ID)
        ages.append(age)
        majors.append(major)
        GPAs.append(gpa)

        print(f"\n{name} was added successfully.")
        print("----------------------------------------")

    elif choice == "2":

        print("\n---------- ALL STUDENTS ----------")

        if len(names) == 0:
            print("No students available.")

        else:
            for i in range(len(names)):
                print(f"\nStudent {i + 1}")
                print(f"Name:  {names[i]}")
                print(f"ID:    {IDs[i]}")
                print(f"Age:   {ages[i]}")
                print(f"Major: {majors[i]}")
                print(f"GPA:   {GPAs[i]}")
                print("----------------------------------------")

    elif choice == "3":

        print("\n---------- SEARCH STUDENT ----------")
        search = int(input("Enter student ID to search: "))

        if search in IDs:
            index = IDs.index(search)

            print("\nStudent found.")
            print(f"Name:  {names[index]}")
            print(f"ID:    {IDs[index]}")
            print(f"Age:   {ages[index]}")
            print(f"Major: {majors[index]}")
            print(f"GPA:   {GPAs[index]}")

        else:
            print("Student not found.")

        print("----------------------------------------")

    elif choice == "4":

        print("\n---------- REMOVE STUDENT ----------")
        remove = int(input("Enter student ID to remove: "))

        if remove in IDs:
            index = IDs.index(remove)

            removed_name = names[index]

            names.pop(index)
            IDs.pop(index)
            ages.pop(index)
            majors.pop(index)
            GPAs.pop(index)

            print(f"{removed_name} was removed successfully.")

        else:
            print("Student not found.")

        print("----------------------------------------")

    elif choice == "5":

        print("\n---------- HIGHEST GPA ----------")

        if len(GPAs) == 0:
            print("No students available.")

        else:
            highest_gpa = max(GPAs)
            index = GPAs.index(highest_gpa)

            print(f"Name:  {names[index]}")
            print(f"ID:    {IDs[index]}")
            print(f"Age:   {ages[index]}")
            print(f"Major: {majors[index]}")
            print(f"GPA:   {GPAs[index]}")

        print("----------------------------------------")

    elif choice == "6":

        print("\n---------- LOWEST GPA ----------")

        if len(GPAs) == 0:
            print("No students available.")

        else:
            lowest_gpa = min(GPAs)
            index = GPAs.index(lowest_gpa)

            print(f"Name:  {names[index]}")
            print(f"ID:    {IDs[index]}")
            print(f"Age:   {ages[index]}")
            print(f"Major: {majors[index]}")
            print(f"GPA:   {GPAs[index]}")

        print("----------------------------------------")

    elif choice == "7":

        print("\n---------- UPDATE GPA ----------")
        student_id = int(input("Enter student ID: "))

        if student_id in IDs:
            index = IDs.index(student_id)

            print(f"Student: {names[index]}")
            print(f"Current GPA: {GPAs[index]}")

            updated_gpa = float(input("Enter new GPA: "))
            GPAs[index] = updated_gpa

            print(f"GPA updated successfully to {updated_gpa}.")

        else:
            print("Student not found.")

        print("----------------------------------------")

    elif choice == "8":

        print("\n---------- TOTAL STUDENTS ----------")
        print(f"Total number of students: {len(names)}")
        print("----------------------------------------")

    elif choice == "9":

        print("\n========================================")
        print("Thank you for using the Student Management System.")
        print("Goodbye!")
        print("========================================")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 9.")
