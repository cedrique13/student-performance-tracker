from modules.database import Database


class Attendance:
    @staticmethod
    def mark_attendance(student_id, status):
        """Record attendance for a student"""
        db = Database()
        query = "INSERT INTO attendance (student_id, date, status) VALUES (%s, CURDATE(), %s)"
        db.execute_query(query, (student_id, status))
        db.close()
