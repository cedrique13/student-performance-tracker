from modules.database import Database
from tabulate import tabulate


class Report:
    @staticmethod
    def generate_student_report():
        """Fetch and display student performance report"""
        db = Database()
        query = """SELECT s.name, g.subject, g.score 
                   FROM students s 
                   JOIN grades g ON s.id = g.student_id"""
        results = db.fetch_results(query)
        print(tabulate(results, headers=[
              "Name", "Subject", "Score"], tablefmt="grid"))
