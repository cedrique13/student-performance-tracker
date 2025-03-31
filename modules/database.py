import mysql.connector


class Database:
    def __init__(self):
        """Initialize database connection"""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Bienvenue@123",
                database="student_tracker"
            )
            self.cursor = self.connection.cursor()
            print("✅ Database connection successful!")
        except mysql.connector.Error as err:
            print(f"❌ Database connection failed: {err}")
            self.connection = None

    def execute_query(self, query, values=None):
        """Execute a query"""
        if self.connection:
            self.cursor.execute(query, values or ())
            self.connection.commit()

    def fetch_results(self, query, values=None):
        """Fetch results from the database"""
        if self.connection:
            self.cursor.execute(query, values or ())
            return self.cursor.fetchall()
        return []
