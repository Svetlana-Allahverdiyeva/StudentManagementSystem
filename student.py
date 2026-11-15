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
