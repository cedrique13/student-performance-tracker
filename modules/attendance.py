from modules.database import Database
from modules.student import Student


class Attendance:
    @staticmethod
    def mark_attendance(student_id):
        """Mark attendance for a student"""
        db = Database()
        if not Student.validate_student(student_id):
            print("❌ Student ID not found.")
            db.close()
            return

        query = "SELECT name FROM students WHERE id = %s"
        student = db.fetch_results(query, (student_id,))

        if student:
            print(f"✅ Student Found: {student[0][0]}")
            confirmation = input("Mark attendance for today? (Y/N): ")
            if confirmation.lower() == 'y':
                query = "INSERT INTO attendance (student_id, date) VALUES (%s, CURDATE())"
                db.execute_query(query, (student_id,))
                print("✅ Attendance marked successfully!")
        db.close()

    @staticmethod
    def list_attendance():
        """List all attendance records"""
        db = Database()
        query = "SELECT s.name, a.date FROM attendance a JOIN students s ON a.student_id = s.id ORDER BY a.date DESC"
        results = db.fetch_results(query)
        db.close()

        if results:
            print(tabulate(results, headers=[
                  "Student Name", "Attendance Date"], tablefmt="grid"))
        else:
            print("❌ No attendance records found.")
