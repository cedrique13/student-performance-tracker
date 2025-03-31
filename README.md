# Student Performance Tracker

## Overview

The **Student Performance Tracker** is a Python-based application designed to help manage student records, including attendance, grades, and performance reports. It uses a **MySQL database** to store student information and provides a menu-driven interface for easy interaction.

## Features

- **Student Management**: Add and view students.
- **Attendance Tracking**: Mark and view attendance records.
- **Grade Management**: Add and view student grades.
- **Performance Reports**: Generate reports showing students' average scores.

## Technologies Used

- **Python** (Core programming language)
- **MySQL** (Database for storing records)
- **MySQL Connector** (Python package for database connection)
- **Tabulate** (For formatting reports in a readable table format)

---

## Installation Guide

### Step 1: Install Python

Ensure Python is installed. If not, download and install it from [python.org](https://www.python.org/downloads/).
Check installation:

```sh
python --version
```

### Step 2: Install Required Packages

Run the following command to install necessary dependencies:

```sh
pip install mysql-connector-python tabulate
```

### Step 3: Install and Set Up MySQL

1. Download and install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/).
2. Open **MySQL Workbench** or the MySQL Command Line.
3. Create the database and tables using the script below.

### Step 4: Set Up the Database

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

---

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
│── .env                  # Environment variables for database connection
└── README.md             # Documentation for the project

```


---

## ⚙️ Features  

### 👤 Student Management  
- ✅ **Add Student** (Ensures unique Student ID)  
- ✅ **List Students**  
- ✅ **Update Student Information**  
- ✅ **Remove Student**  

### 📅 Attendance Tracking  
- ✅ **Mark Attendance** (Only valid students)  
- ✅ **List Attendance Records**  

### 📊 Academic Performance  
- ✅ **Record Grades** (Subject, Score, Exam Type)  
- ✅ **Retrieve Student Academic Record**  

### 📜 Reports & Insights  
- ✅ **Generate Student Performance Report** (Sorted from highest to lowest)  
- ✅ **Identify Low-Performing Students** (Below 50%)  

---

## 🛠️ Setup & Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/student-performance-tracker.git
cd student-performance-tracker



---

## Usage

### Running the Application

Start the application using:

```sh
python menu.py
```

### Menu Options

1. **Manage Students**: Add or view student records.
2. **Manage Attendance**: Mark or view attendance records.
3. **Manage Grades**: Add or view student grades.
4. **Generate Reports**: Display student performance reports.
5. **Exit**: Close the application.

---

## How to Contribute

### Step 1: Clone the Repository

```sh
git clone <repository_url>
cd student-performance-tracker
```

### Step 2: Create a Branch

Each contributor should create a branch based on their task:

```sh
git checkout -b <feature_branch>
```

### Step 3: Commit and Push Changes

```sh
git add .
git commit -m "Added feature XYZ"
git push origin <feature_branch>
```

### Step 4: Submit a Pull Request

1. Go to the repository on GitHub.
2. Click **Pull Requests** > **New Pull Request**.
3. Select the branch and request a review before merging.

---

## Testing the Application

### Functional Testing

- Run **menu.py** and test each feature.
- Verify MySQL tables contain expected records.

### Database Connection Testing

- Ensure **database.py** connects successfully to MySQL.

### Report Testing

- Check if reports generate correctly with formatted data.

---

## Author

This project is developed by **Cedrick and team**.

---

## License

This project is open-source and free to use under the MIT License.
