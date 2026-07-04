print("========================================")
print("   PERSONAL STUDY PERFORMANCE TRACKER")
print("========================================")

study_time = []
subjects = []
ratings = []

while True:
    print("\n1. Add study session")
    print("2. Show all study sessions")
    print("3. Search subject")
    print("4. Remove study session")
    print("5. Show total study time")
    print("6. Show best-rated subject")
    print("7. Show lowest-rated subject")
    print("8. Exit")
    print("----------------------------------------")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n---------- New Study Session ----------")
        subject_name = input("Enter subject name: ")
        minutes_studied = int(input("Enter study time in minutes: "))
        rate = int(input("Rate your study session from 1 to 10: "))

        subjects.append(subject_name)
        study_time.append(minutes_studied)
        ratings.append(rate)

        print("Session added successfully.")

    elif choice == "2":
        print("\n---------- All Study Sessions ----------")

        if len(subjects) == 0:
            print("No sessions available.")
        else:
            for i in range(len(subjects)):
                print(f"\nSession {i + 1}")
                print(f"Subject: {subjects[i]}")
                print(f"Study time: {study_time[i]} minutes")
                print(f"Rating: {ratings[i]}/10")
                print("----------------------------------------")

    elif choice == "3":
        print("\n---------- Search Subject ----------")
        search = input("Enter subject to search: ")

        if search in subjects:
            print(f"Subject found: {search}")
        else:
            print("Subject not found.")

    elif choice == "4":
        print("\n---------- Remove Study Session ----------")
        remove = input("Enter subject to remove: ")

        if remove in subjects:
            index = subjects.index(remove)
            subjects.pop(index)
            study_time.pop(index)
            ratings.pop(index)
            print("Study session removed successfully.")
        else:
            print("Session not found.")

    elif choice == "5":
        print("\n---------- Study Summary ----------")
        total = sum(study_time)
        print(f"Total study time: {total} minutes")

    elif choice == "6":
        print("\n---------- Best-Rated Subject ----------")

        if len(ratings) == 0:
            print("No sessions available.")
        else:
            best = max(ratings)
            index = ratings.index(best)

            print(f"Subject: {subjects[index]}")
            print(f"Study time: {study_time[index]} minutes")
            print(f"Rating: {ratings[index]}/10")

    elif choice == "7":
        print("\n---------- Lowest-Rated Subject ----------")

        if len(ratings) == 0:
            print("No sessions available.")
        else:
            lowest = min(ratings)
            index = ratings.index(lowest)

            print(f"Subject: {subjects[index]}")
            print(f"Study time: {study_time[index]} minutes")
            print(f"Rating: {ratings[index]}/10")

    elif choice == "8":
        print("\nThank you for using Personal Study Performance Tracker.")
        print("Keep studying consistently. Goodbye!")
        break

    else:
        print("Invalid option. Please choose from 1 to 8.")