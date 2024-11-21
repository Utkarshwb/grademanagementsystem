# grademanagementsystem

### this is student grade management system

# Student Grade Management System

## Objective
The **Student Grade Management System** is a GUI-based application developed using Python and Tkinter. The objective of this project is to allow users to manage student data, add grades, and calculate averages in an easy-to-use interface.

---

## Features
- Add new students with their name and unique ID.
- Add grades for individual students.
- View detailed information about a student, including their grades and average.
- Calculate and display the class average grade.
- User-friendly interface using Tkinter.

---

## Implementation
- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Class Design**: Used OOP principles with a `Student` class to encapsulate student data and logic.
- **Error Handling**: Implemented validations for inputs like unique student IDs and numeric grades.
- **Modular Structure**: The code is structured with separate methods for different functionalities.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Student-Grade-Management-System.git


```mermaid
graph TD;
    A[Main Application] --> B[Add Student];
    A --> C[Add Grade];
    A --> D[View Student Info];
    A --> E[Calculate Class Average];
    B --> F[Student Object];
    C --> F;
    D --> F;
    E --> F;
