from modules.database import Database


class Attendance:
    @staticmethod
    def mark_attendance():
        """Record attendance for a student"""
        db = Database()
        id = input("Student ID: ")
        status = input("Stauts (Present/Absent): ")
    
        query = "INSERT INTO attendance (student_id, date, status) VALUES (%s, CURDATE(), %s)"
        db.execute_query(query, (id, status))
        db.close()
        
    def list_attendance():
        """List attendance records"""
        db = Database()
        query = "SELECT * FROM attendance"
        results = db.fetch_results(query)
        for row in results:
            # Print the results in a formatted way
            print(f"Student ID: {row[1]}, Date: {row[2]}, Status: {row[3]}")
            # print(row)
        db.close()
