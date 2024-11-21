

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
   git clone https://github.com/Utkarshwb/grademanagementsystem-System.git
2. Navigate to the project folder:
   ```bash
   cd Student-Grade-Management-System
   
3. Run the application:
    ```bash
   python grademanagement.py
   
```mermaid
graph TD;
    A[🎓 Main Application] --> B[📘 Add Student];
    A --> C[📊 Add Grade];
    A --> D[👩‍🎓 View Student Info];
    A --> E[📈 Calculate Class Average];
    B --> F[📂 Student Object];
    C --> F;
    D --> F;
    E --> F;

    %% Style Enhancements %%
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#9f9,stroke:#333,stroke-width:2px;
    style C fill:#9cf,stroke:#333,stroke-width:2px;
    style D fill:#fc9,stroke:#333,stroke-width:2px;
    style E fill:#c9f,stroke:#333,stroke-width:2px;
    style F fill:#ffc,stroke:#333,stroke-width:2px;

    %% Highlight Key Interactions %%
    linkStyle 0 stroke-width:2px,stroke:#333,fill:none;
    linkStyle 1 stroke-width:2px,stroke:#333,fill:none;
    linkStyle 2 stroke-width:2px,stroke:#333,fill:none;
    linkStyle 3 stroke-width:2px,stroke:#333,fill:none;

