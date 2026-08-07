class Person:
    def __init__(
        self,
        first_name,
        last_name,
        age,
        email
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email


    def intorduce_person(self):
        print("\n==== Student Information ====")
        print(
            f"First Name : {self.first_name.title()}\n"
            f"Last Name: {self.last_name.title()}\n"
            f"Age : {self.age}\n"
            f"Email Address : {self.email}"
        )

        print("==============================")


    def update_email(self):
        new_email = input("Enter the new email please: ")
        self.email = new_email
        print("Email successfully updated.")


class Student(Person):
    def __init__(
        self,
        first_name,
        last_name,
        age,
        email,
        student_id,
        major,
        enrollment_year
    ):

        super().__init__(
            first_name,
            last_name,
            age,
            email
        )

        self.student_id = student_id
        self.major = major
        self.enrollment_year = enrollment_year
        self.registered_courses = []
        self.completed_courses = []


    def intorduce_student(self):
        print("\n==== Student Information ====")
        print(
            f"ID : {self.student_id}\n"
            f"Major : {self.major.title()}\n"
            f"Enrollement Year : {self.enrollment_year}\n"
            f"Registered Courses : {self.registered_courses}\n"
            f"Completed Course : {self.completed_courses}"
        )

        print("==============================")


    def register_course(self):
        course = input("Enter the course your want to register: ").title()

        if course in self.registered_courses: 
            print("Entered course already exist.")
        
        else: 
            self.registered_courses.append(course)
            print("Course added successfully.")


    def drop_course(self):
        course = input("Enter the course your want to dropt out: ").title()

        if course not in self.registered_courses: 
            print("Course is not available.")

        else: 
            self.registered_courses.remove(course)
            print(f" {course} successfully dropped.")


    def complete_course(self):
        course = input("Enter the course you want ot complete: ").title()

        if course in self.registered_courses: 

            self.completed_courses.append(course)
            self.registered_courses.remove(course)
            print("Coursed completed successfully.")
        
        elif course in self.completed_courses: 
            print("Course already completed.")

        else: 
            print("You are not registered to this course.")


    def show_registered_courses(self):
        print(self.registered_courses)


    def show_completed_courses(self):
        print(self.completed_courses)


class Teacher(Person):
    def __init__(
        self,
        first_name,
        last_name,
        age,
        email,
        teacher_id,
        department
    ):

        super().__init__(
            first_name,
            last_name,
            age,
            email
        )

        self.teacher_id = teacher_id
        self.department = department
        self.assigned_courses = []


    def intorduce_teacher(self):
        print("\n==== Teacher Information ====")
        print(
            f"ID : {self.teacher_id}\n"
            f"Department : {self.department.title()}\n"
            f"Assigned Courses : {self.assigned_courses}"
        )

        print("==============================")


    def assigend_course(self):
        course = input("Enter the course you want to assigned in: ").title()
        
        if course in self.assigned_courses:
            print("You are already assigend to this course.")

        else: 
            self.assigned_courses.append(course)
            print(f"You are successfully assigned to {course}.")


    def remove_course(self):
        course = input("Enter the course you want to remove: ").title()

        if course not in self.assigned_courses: 
            print("You are not assigned to this course.")

        else:
            self.assigned_courses.remove(course)
            print(f"{course} removed successfully.")


    def show_assigend_courses(self):
        print(self.assigned_courses)


class Course:
    def __init__(
        self,
        course_code,
        course_name,
        credit,
        capacity,
    ):

        self.course_code = course_code
        self.course_name = course_name
        self.credit = credit
        self.capacity = capacity
        self.students = []
        self.teacher = None


    def intorduce_course(self):
        print("\n==== Course Information ====")
        print(
            f"Course Code : {self.course_code}\n"
            f"Course name : {self.course_name.title()}\n"
            f"Credit : {self.credit}\n"
            f"Capacity : {self.capacity}\n"
            f"Students : {self.students}\n"
            f"Teacher : {self.teacher}"
        )

        print("==============================")


    def add_student(self, student):

        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Student alerady exist.")
                return
 
        self.students.append(student)
        print("Student added successfully.")

            
    def remove_student(self, student):
        
        for existing_student in self.students: 
            if existing_student.student_id == student.student_id:
                self.students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found")


    def assign_teacher(self, teacher):
        if self.teacher is not None:
            print("Teacher is already assigned.")
        else:
            self.teacher = teacher
            print("Teacher assigned successfully.")


    def show_students(self):
        print(self.students)




student = Student(
    "Shahabuddin",
    "Shahid",
    22,
    "shahid.kontakt@gmail.com",
    "S101",
    "Computer Science",
    2026
)

teacher = Teacher(
    "Hasam",
    "Shahid",
    20,
    "shahid@gmail.com",
    "T101",
    "Computer Science"
)

course = Course(
    "CS101",
    "Python",
    5,
    30
)


while True:
    print("\n ======= UNIVERSITY SYSTEM =======")
    print("1. Student Menu")
    print("2. Teacher Menu")
    print("3. Course Menu")
    print("4. Exit")

    chose = input("Chose an option (1-4): ")

    if chose == "1":

        while True:
            print("\n======= STUDENT MENU =======")
            print("1. Show Student Information")
            print("2. Update Email")
            print("3. Register Course")
            print("4. Drop Course")
            print("5. Complete Course")
            print("6. Show Registered Courses")
            print("7. Show Completed Courses")
            print("8. Back")

            student_chose = input("Chose an option (1-8): ")

            if student_chose == "1":
                student.intorduce_person()

            elif student_chose == "2":
                student.update_email()

            elif student_chose == "3":
                student.register_course()

            elif student_chose == "4":
                student.drop_course()

            elif student_chose == "5":
                student.complete_course()

            elif student_chose == "6":
                student.show_registered_courses()

            elif student_chose == "7":
                student.show_completed_courses()

            elif student_chose == "8":
                break


    elif chose == "2":

        while True: 
            print("\n======= TEACHER MENU =======")
            print("1. Show Teacher Information")
            print("2. Update Email")
            print("3. Assign Teacher")
            print("4. Remove Teacher")
            print("5. Show Assigend Courses")
            print("6. Back")

            teacher_chose = input("Chose an option (1-6): ")

            if teacher_chose == "1":
                teacher.intorduce_teacher()

            elif teacher_chose == "2":
                teacher.update_email()

            elif teacher_chose == "3":
                teacher.assigend_course()

            elif teacher_chose == "4":
                teacher.remove_course()

            elif teacher_chose == "5":
                teacher.show_assigend_courses()

            elif teacher_chose == "6":
                break

            


    elif chose == "3":
        
        while True:
            print("\n======= COURSE MENU =======")
            print("1. Show Course Information")
            print("2. Add Student")
            print("3. Remove Student")
            print("4. Assign Teacher")
            print("5. Show Students")
            print("6. Back")

            course_chose = input("Chose an option (1-6): ")

            if course_chose == "1":
                course.intorduce_course()

            elif course_chose == "2":
                course.add_student(student)

            elif course_chose == "3":
                course.remove_student(student)

            elif course_chose == "4":
                course.assign_teacher(teacher)
            
            elif course_chose == "5":
                course.show_students()

            elif course_chose == "6":
                break

            

    elif chose == "4":
        print(
            "Thanks for chosing our system.\n"
            "Exiting..."
        )
        break

    else:
        print("Wrong input. chose from 1 to 4.")