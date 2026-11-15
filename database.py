import json


def loadStudents():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)

        return students

    except FileNotFoundError as e:
        print(e)
        return []

    except json.JSONDecodeError as e:
        print(e)
        return []


def saveStudents(students):
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)