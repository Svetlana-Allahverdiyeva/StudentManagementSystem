from database import *


def addStudent():
    students = loadStudents()

    try:
        student_id = int(input("Enter student ID: "))

        if student_id <= 0:
            print("Error: ID must be positive!")
            return

        for student in students:
            if student["id"] == student_id:
                print("Error: This ID already exists!")
                return

        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Name cannot be empty!")
            return

        age = int(input("Enter student age: "))

        if age <= 0:
            print("Error: Age must be positive!")
            return

        major = input("Enter student major: ").strip()

        if not major:
            print("Error: Major cannot be empty!")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "major": major
        }

        students.append(student)

        saveStudents(students)

        print("Student added successfully!")

    except ValueError:
        print("Error: ID and age must be numbers!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def showAllStudents():
    students = loadStudents()

    if not students:
        print("No students found!")
        return

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Major: {student['major']}")

def searchStudent():
    students = loadStudents()

    search_name = input("Enter student name: ").strip().lower()

    for student in students:
        if student["name"].lower() == search_name:
            print("Student found!")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Major: {student['major']}")
            return

    print("Student not found!")

def updateStudent():
    students = loadStudents()

    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("Enter new name: ").strip()
            student["age"] = int(input("Enter new age: "))
            student["major"] = input("Enter new major: ").strip()

            saveStudents(students)

            print("Student updated successfully!")
            return

    print("Student not found!")

def removeStudent():
    students = loadStudents()

    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            saveStudents(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")