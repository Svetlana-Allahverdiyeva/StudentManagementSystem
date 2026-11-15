from student import *


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            addStudent()
        elif choice == "2":
            showAllStudents()
        elif choice == "3":
            searchStudent()
        elif choice == "4":
            updateStudent()
        elif choice == "5":
            removeStudent()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter valid data!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")