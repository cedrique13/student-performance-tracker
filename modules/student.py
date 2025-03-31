from modules.database import Database


class Student:
    def __init__(self, name, age, grade_level):
        """Initialize student attributes"""
        self.name = name
        self.age = age
        self.grade_level = grade_level

    @staticmethod
    def add_student(name, age, grade_level):
        """Add a new student to the database"""
        db = Database()
        query = "INSERT INTO students (name, age, grade_level) VALUES (%s, %s, %s)"
        db.execute_query(query, (name, age, grade_level))
        db.close()
        
    @staticmethod
    def list_students():
        """List all students in the database"""
        db = Database()
        query = "SELECT * FROM students"
        results = db.fetch_results(query)
        # Print results in a readable format
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade Level: {row[3]}")
        db.close()
        return results
