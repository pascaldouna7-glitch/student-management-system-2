import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "students.txt"

# ===== FILE FUNCTIONS =====
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(",".join(student) + "\n")

# ===== FUNCTIONS =====
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if not name or not age or not course:
        messagebox.showwarning("Error", "All fields are required!")
        return

    students = load_students()
    student_id = str(len(students) + 1)

    students.append([student_id, name, age, course])
    save_students(students)

    view_students()
    clear_fields()
    messagebox.showinfo("Success", "Student added!")

def view_students():
    listbox.delete(0, tk.END)
    for s in load_students():
        listbox.insert(tk.END, f"{s[0]} | {s[1]} | {s[2]} | {s[3]}")

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a student!")
        return

    index = selected[0]
    students = load_students()
    students.pop(index)

    save_students(students)
    view_students()
    messagebox.showinfo("Deleted", "Student removed!")

def search_student():
    keyword = search_entry.get().lower()
    listbox.delete(0, tk.END)

    for s in load_students():
        if keyword in s[1].lower():
            listbox.insert(tk.END, f"{s[0]} | {s[1]} | {s[2]} | {s[3]}")

def update_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a student!")
        return

    index = selected[0]
    students = load_students()

    students[index][1] = name_entry.get()
    students[index][2] = age_entry.get()
    students[index][3] = course_entry.get()

    save_students(students)
    view_students()
    messagebox.showinfo("Updated", "Student updated!")

def fill_fields(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        student = load_students()[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, student[1])

        age_entry.delete(0, tk.END)
        age_entry.insert(0, student[2])

        course_entry.delete(0, tk.END)
        course_entry.insert(0, student[3])

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# ===== GUI DESIGN =====
root = tk.Tk()
root.title("Student Management System PRO")
root.geometry("600x500")
root.configure(bg="#2c3e50")

# Title
tk.Label(root, text="Student Management System", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#34495e")
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="#34495e", fg="white").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Age", bg="#34495e", fg="white").grid(row=1, column=0)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1)

tk.Label(frame, text="Course", bg="#34495e", fg="white").grid(row=2, column=0)
course_entry = tk.Entry(frame)
course_entry.grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack()

tk.Button(btn_frame, text="Add", width=10, bg="#27ae60", fg="white", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, bg="#f39c12", fg="white", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, bg="#e74c3c", fg="white", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", width=10, bg="#95a5a6", command=clear_fields).grid(row=0, column=3, padx=5)

# Search
search_entry = tk.Entry(root)
search_entry.pack(pady=5)

tk.Button(root, text="Search", bg="#3498db", fg="white", command=search_student).pack()

# Listbox
listbox = tk.Listbox(root, width=70)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", fill_fields)

# Load data
view_students()

# Run
root.mainloop()