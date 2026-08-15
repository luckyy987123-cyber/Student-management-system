students = {}


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
    else:
        for student_id, student in students.items():
            print("\nStudent ID:", student_id)
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])


def search_student():
    student_id = int(input("Enter Student ID to search: "))

    if student_id in students:
        student = students[student_id]

        print("Student ID:", student_id)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")


def update_student():
    student_id = int(input("Enter Student ID to update: "))

    if student_id in students:
        students[student_id]["name"] = input("Enter New Name: ")
        students[student_id]["age"] = int(input("Enter New Age: "))
        students[student_id]["course"] = input("Enter New Course: ")
        students[student_id]["marks"] = float(input("Enter New Marks: "))

        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def display_grade():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        marks = students[student_id]["marks"]

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Marks:", marks)
        print("Grade:", grade)
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate/Display Grade")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        display_grade()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")