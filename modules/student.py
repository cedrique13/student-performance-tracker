from modules.database import Database
from tabulate import tabulate


class Student:
    def __init__(self, student_id, name, age, grade_level):
        """Initialize student attributes"""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade_level = grade_level

    @staticmethod
    def validate_student(student_id):
        """Check if a student ID exists"""
        db = Database()
        query = "SELECT id FROM students WHERE id = %s"
        result = db.fetch_results(query, (student_id,))
        db.close()
        return bool(result)

    @staticmethod
    def add_student(student_id, name, age, grade_level):
        """Add a new student with unique ID"""
        db = Database()
        if Student.validate_student(student_id):
            print("❌ Student ID already exists. Try a different ID.")
            db.close()
            return
        query = "INSERT INTO students (id, name, age, grade_level) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (student_id, name, age, grade_level))
        db.close()
        print("✅ Student added successfully!")

    @staticmethod
    def list_students():
        """List all students"""
        db = Database()
        query = "SELECT * FROM students"
        results = db.fetch_results(query)
        db.close()
        if results:
            print(tabulate(results, headers=[
                  "ID", "Name", "Age", "Grade Level"], tablefmt="grid"))
        else:
            print("❌ No students found.")

    @staticmethod
    def update_student(student_id, name, age, grade_level):
        """Update student details"""
        db = Database()
        query = "UPDATE students SET name = %s, age = %s, grade_level = %s WHERE id = %s"
        db.execute_query(query, (name, age, grade_level, student_id))
        db.close()
        print("✅ Student details updated successfully!")

    @staticmethod
    def remove_student(student_id):
        """Remove a student"""
        db = Database()
        query = "DELETE FROM students WHERE id = %s"
        db.execute_query(query, (student_id,))
        db.close()
        print("✅ Student removed successfully!")

    @staticmethod
    def retrieve_academic_record(student_id):
        """Retrieve a student's academic record"""
        db = Database()
        query = "SELECT subject, score, exam_type FROM grades WHERE student_id = %s ORDER BY score DESC"
        results = db.fetch_results(query, (student_id,))
        db.close()

        if results:
            print(tabulate(results, headers=[
                  "Subject", "Score", "Exam Type"], tablefmt="grid"))
        else:
            print("❌ No records found for this student.")
