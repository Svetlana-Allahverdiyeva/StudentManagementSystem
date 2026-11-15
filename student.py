from database import *


def addStudent():
    students = loadStudents()

    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    major = input("Enter student major: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    }

    students.append(student)

    saveStudents(students)

    print("Student added successfully!")

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