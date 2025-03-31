from modules.student import Student
from modules.attendance import Attendance
from modules.grades import Grades
from modules.report import Report


def main():
    """CLI menu for the Student Performance Tracker"""
    while True:
        print("""
        1. Add Student
        2. List Students
        3. Update Student
        4. Remove Student
        5. Mark Attendance
        6. List Attendance
        7. Record Grade
        8. Retrieve Academic Record
        9. Generate Performance Report
        10. Identify Low Performers
        11. Exit
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Student ID (unique): ")
            name = input("Student Name: ")
            age = input("Age: ")
            grade = input("Grade Level: ")
            Student.add_student(student_id, name, age, grade)
        elif choice == "2":
            Student.list_students()
        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            if Student.validate_student(student_id):
                name = input("New Name: ")
                age = input("New Age: ")
                grade = input("New Grade Level: ")
                Student.update_student(student_id, name, age, grade)
            else:
                print("❌ Student ID not found.")
        elif choice == "4":
            student_id = input("Enter Student ID to remove: ")
            if Student.validate_student(student_id):
                Student.remove_student(student_id)
            else:
                print("❌ Student ID not found.")
        elif choice == "5":
            student_id = input("Enter Student ID for attendance: ")
            if Student.validate_student(student_id):
                Attendance.mark_attendance(student_id)
            else:
                print("❌ Student ID not found.")
        elif choice == "6":
            Attendance.list_attendance()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            if Student.validate_student(student_id):
                subject = input("Enter Subject: ")
                score = input("Enter Score: ")
                exam_type = input("Enter Exam Type (e.g., Midterm, Final): ")
                Grades.record_grade(student_id, subject, score, exam_type)
            else:
                print("❌ Student ID not found.")
        elif choice == "8":
            student_id = input("Enter Student ID: ")
            if Student.validate_student(student_id):
                Student.retrieve_academic_record(student_id)
            else:
                print("❌ Student ID not found.")
        elif choice == "9":
            Report.generate_student_report()
        elif choice == "10":
            Report.identify_low_performers()
        elif choice == "11":
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
