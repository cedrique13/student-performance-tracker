from modules.database import Database


class Grades:
    @staticmethod
    def record_grade(student_id, subject, score):
        """Record a student's grade"""
        db = Database()
        query = "INSERT INTO grades (student_id, subject, score) VALUES (%s, %s, %s)"
        db.execute_query(query, (student_id, subject, score))
        db.close()
