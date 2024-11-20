import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, name, student_id):  
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0

    def get_info(self):
        average = f"{self.calculate_average():.2f}"
        return f"ID: {self.student_id}\nName: {self.name}\nGrades: {self.grades}\nAverage: {average}"


class GradeManagementSystem:
    def __init__(self, root):  # Fixed constructor name
        self.students = {}
        self.root = root
        self.root.title("Student Grade Management System")

        # Main Frame
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()

        # Buttons
        tk.Label(self.main_frame, text="Student Grade Management System", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Button(self.main_frame, text="Add Student", width=20, command=self.add_student_gui).grid(row=1, column=0, pady=5)
        tk.Button(self.main_frame, text="Add Grade", width=20, command=self.add_grade_gui).grid(row=2, column=0, pady=5)
        tk.Button(self.main_frame, text="View Student Info", width=20, command=self.view_student_gui).grid(row=3, column=0, pady=5)
        tk.Button(self.main_frame, text="Class Average", width=20, command=self.calculate_class_average).grid(row=4, column=0, pady=5)
        tk.Button(self.main_frame, text="Exit", width=20, command=self.root.quit).grid(row=5, column=0, pady=5)

    def add_student_gui(self):
        def save_student():
            name = name_entry.get()
            student_id = id_entry.get()
            if student_id in self.students:
                messagebox.showerror("Error", "Student ID already exists!")
                return
            if not name or not student_id:
                messagebox.showerror("Error", "Please fill in all fields!")
                return
            self.students[student_id] = Student(name, student_id)
            messagebox.showinfo("Success", f"Student {name} added successfully!")
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student")
        tk.Label(add_window, text="Name:").grid(row=0, column=0, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, pady=5)
        tk.Label(add_window, text="Student ID:").grid(row=1, column=0, pady=5)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=1, column=1, pady=5)
        tk.Button(add_window, text="Add", command=save_student).grid(row=2, column=0, columnspan=2, pady=10)

    def add_grade_gui(self):
        def save_grade():
            student_id = id_entry.get()
            if student_id not in self.students:
                messagebox.showerror("Error", "Student ID not found!")
                return
            try:
                grade = float(grade_entry.get())
                self.students[student_id].add_grade(grade)
                messagebox.showinfo("Success", "Grade added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid grade! Please enter a number.")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Grade")
        tk.Label(add_window, text="Student ID:").grid(row=0, column=0, pady=5)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=0, column=1, pady=5)
        tk.Label(add_window, text="Grade:").grid(row=1, column=0, pady=5)
        grade_entry = tk.Entry(add_window)
        grade_entry.grid(row=1, column=1, pady=5)
        tk.Button(add_window, text="Add Grade", command=save_grade).grid(row=2, column=0, columnspan=2, pady=10)

    def view_student_gui(self):
        def display_info():
            student_id = id_entry.get()
            if student_id not in self.students:
                messagebox.showerror("Error", "Student ID not found!")
                return
            student = self.students[student_id]
            messagebox.showinfo("Student Info", student.get_info())
            view_window.destroy()

        view_window = tk.Toplevel(self.root)
        view_window.title("View Student Info")
        tk.Label(view_window, text="Student ID:").grid(row=0, column=0, pady=5)
        id_entry = tk.Entry(view_window)
        id_entry.grid(row=0, column=1, pady=5)
        tk.Button(view_window, text="View Info", command=display_info).grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_class_average(self):
        if not self.students:
            messagebox.showerror("Error", "No students in the system!")
            return
        total = sum(student.calculate_average() for student in self.students.values())
        class_average = total / len(self.students)
        messagebox.showinfo("Class Average", f"Class Average: {class_average:.2f}")


if __name__ == "__main__":  
    root = tk.Tk()
    app = GradeManagementSystem(root)
    root.mainloop()
