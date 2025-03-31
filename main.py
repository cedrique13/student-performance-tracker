from modules.student import Student
from modules.attendance import Attendance
from modules.grades import Grades
from modules.report import Report


def main():
    """CLI menu for the Student Performance Tracker"""
    while True:
        print("1. Add Student\n2. List Students\n3. Mark Attendance\n4. List attendance \n5. Record Grade\n6. Generate Report\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student Name: ")
            age = input("Age: ")
            grade = input("Grade Level: ")
            Student.add_student(name, age, grade)
        elif choice == "2":
            Student.list_students()
        elif choice == "3":
            Attendance.mark_attendance()
        elif choice == "4":
            Attendance.list_attendance()
        elif choice == "5":
            Grades.record_grade()

        elif choice == "7":
            break


if __name__ == "__main__":
    main()
