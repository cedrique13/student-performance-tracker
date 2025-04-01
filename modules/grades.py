from modules.database import Database
from modules.student import Student
from tabulate import tabulate


#  CREATE TABLE grades (id INT  AUTO_INCREMENT PRIMARY KEY, student_id int, subject varchar(50), score INT, exam_type VARCHAR(50), FOREIGN KEY (student_id) REFERENCES students(id))

class Grades:
    @staticmethod
    def record_grade(student_id, subject, score, exam_type):
        """Record a student's grade"""
        db = Database()
        if not Student.validate_student(student_id):
            print("❌ Student ID not found.")
            db.close()
            return
        query = "INSERT INTO grades (student_id, subject, score, exam_type) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (student_id, subject, score, exam_type))
        db.close()
        print("✅ Grade recorded successfully!")

    
