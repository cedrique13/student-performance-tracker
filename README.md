# Student Performance Tracker

## Overview

The **Student Performance Tracker** is a command-line interface (CLI) application designed to help educators and administrators track student performance efficiently. Built using Python and MySQL, the app allows users to manage student records, enter grades, track attendance, analyze performance trends, and generate reports.

## Features

- **Student Management:** Add, update, and delete student records.
- **Attendance Tracking:** Mark and list student attendance.
- **Performance Tracking:** Record and update student grades for different subjects.
- **Reports & Insights:** Generate performance reports and identify low-performing students.
- **Database Integration:** Stores data in a structured MySQL database for easy retrieval.
- **CLI-Based Interface:** Simple and interactive command-line interface for ease of use.

## Prerequisites

Ensure you have the following installed on your system:

- Python (>=3.8)
- MySQL (as database backend)
- Required Python libraries:
  - `mysql-connector-python`
  - `python-dotenv`
  - `tabulate`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/student-performance-tracker.git
   cd student-performance-tracker
   ```
2. Set up the database:
   Run the following SQL script in MySQL Workbench:
   ```sql
   CREATE DATABASE IF NOT EXISTS student_tracker;
   USE student_tracker;

   CREATE TABLE students (
       id VARCHAR(10) PRIMARY KEY,
       name VARCHAR(255),
       age INT,
       grade_level VARCHAR(50)
   );

   CREATE TABLE attendance (
       id INT AUTO_INCREMENT PRIMARY KEY,
       student_id VARCHAR(10),
       date DATE,
       FOREIGN KEY (student_id) REFERENCES students(id)
   );

   CREATE TABLE grades (
       id INT AUTO_INCREMENT PRIMARY KEY,
       student_id VARCHAR(10),
       subject VARCHAR(100),
       score FLOAT,
       exam_type VARCHAR(50),
       FOREIGN KEY (student_id) REFERENCES students(id)
   );
   ```

## Usage

Run the application with:

```sh
python main.py
```

You will be presented with a CLI menu with several options such:

- Add a new student
- Mark attendance
- Enter grades
- View student performance
- Generate reports
- Identify low-performing students
- Exit the application

## Project Structure

```
student-performance-tracker/
│── modules/
│   ├── database.py       # Database connection and query execution
│   ├── student.py        # Manage student records (add, list, update, remove)
│   ├── attendance.py     # Mark and list student attendance
│   ├── grades.py         # Record and retrieve student grades
│   ├── report.py         # Generate reports and identify low performers
│── main.py               # CLI interface for interacting with the application
│── .env.example          # Environment variables for database connection
└── README.md             # Documentation for the project
```

## Example Operations

### Adding a Student:

```sh
Enter Student Name: John Doe
Enter Age: 15
Enter Grade Level: 10A
Student added successfully!
```

### Marking Attendance:

```sh
Enter Student ID: 101
Enter Date (YYYY-MM-DD): 2024-03-31
Attendance recorded successfully!
```

### Entering Grades:

```sh
Enter Student ID: 101
Enter Subject: Mathematics
Enter Score: 85
Enter Exam Type: Midterm
Grade recorded successfully!
```

### Generating Report:

```sh
+-----------+----------+---------+
| StudentID | Subject  | Score   |
+-----------+----------+---------+
| 101       | Math     | 85      |
| 101       | Science  | 90      |
+-----------+----------+---------+
```

### Identifying Low Performers:

```sh
+-----------+----------+---------+
| StudentID | Subject  | Score   |
+-----------+----------+---------+
| 102       | Math     | 45      |
| 103       | Science  | 48      |
+-----------+----------+---------+
```

## Future Enhancements

- Implement a graphical user interface (GUI)
- Add data visualization for student performance trends
- Integrate machine learning for predictive analytics

## License

This project is licensed under the MIT License.

