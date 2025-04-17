# gui/main_gui.py
import tkinter as tk
from tkinter import messagebox
from models.student_model import add_student, get_all_students

def submit_data():
    try:
        add_student(
            first_name_entry.get(),
            middle_name_entry.get(),
            last_name_entry.get(),
            dob_entry.get(),
            email_entry.get(),
            major_entry.get(),
            int(year_entry.get()),
            phone_entry.get(),
            address_entry.get(),
            emergency_entry.get()
        )
        messagebox.showinfo("Success", "Student added successfully!")
        clear_form()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_form():
    for entry in all_entries:
        entry.delete(0, tk.END)

def view_students():
    listbox.delete(0, tk.END)
    students = get_all_students()
    for student in students:
        listbox.insert(tk.END, student)

root = tk.Tk()
root.title("Student Management System")

# Labels and Entry Widgets
fields = [
    "First Name", "Middle Name", "Last Name", "Date of Birth (DDMMYYYY)",
    "Email", "Major", "Year of Enrollment", "Phone Number",
    "Address", "Emergency Contact Number"
]

entries = []
for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0, sticky='w')
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=2)
    entries.append(entry)

# Assign individual entries
(
    first_name_entry, middle_name_entry, last_name_entry, dob_entry,
    email_entry, major_entry, year_entry, phone_entry,
    address_entry, emergency_entry
) = entries

all_entries = entries  # For clearing form

# Buttons
tk.Button(root, text="Submit", command=submit_data).grid(row=len(fields), column=0, pady=10)
tk.Button(root, text="View All", command=view_students).grid(row=len(fields), column=1, pady=10)

# Listbox to show students
listbox = tk.Listbox(root, width=130)
listbox.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
