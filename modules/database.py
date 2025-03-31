import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
# Load environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')

class Database:
    def __init__(self):
        """Initialize database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_pass,
                database=db_name
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
            print("✅ Query executed successfully!")

    def fetch_results(self, query, values=None):
        """Fetch results from the database"""
        if self.connection:
            self.cursor.execute(query, values or ())
            return self.cursor.fetchall()
        return []
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("✅ Database connection closed!")
