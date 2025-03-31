from modules.database import Database
from tabulate import tabulate


class Report:
    @staticmethod
    def generate_student_report():
        """Generate a student performance report, sorted from highest to lowest scores"""
        db = Database()
        query = """SELECT s.name, g.subject, g.score, g.exam_type 
                   FROM students s 
                   JOIN grades g ON s.id = g.student_id
                   ORDER BY g.score DESC"""
        results = db.fetch_results(query)
        db.close()

        if results:
            print(tabulate(results, headers=[
                  "Name", "Subject", "Score", "Exam Type"], tablefmt="grid"))
        else:
            print("❌ No records found.")
