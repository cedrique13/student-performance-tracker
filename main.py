from modules.student import Student
from modules.attendance import Attendance
from modules.grades import Grades
from modules.report import Report


def main():
    """CLI menu for the Student Performance Tracker"""
    while True:
        print("1. Add Student\n2. List Students\n3. Mark Attendance\n4. Record Grade\n5. Generate Report\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student Name: ")
            age = input("Age: ")
            grade = input("Grade Level: ")
            Student.add_student(name, age, grade)
        elif choice == "2":
            Student.list_students()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
