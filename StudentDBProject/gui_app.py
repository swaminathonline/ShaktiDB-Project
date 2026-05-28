import tkinter as tk
from tkinter import ttk

from database import create_tables, get_dashboard_counts

from auth import (
    validate_login,
    show_login_success,
    show_login_error
)

from student import (
    add_student,
    view_students,
    delete_student,
    search_student,
    update_student
)

from attendance import (
    mark_attendance,
    attendance_analytics,
    low_attendance_students
)

from marks import (
    add_marks,
    topper_analysis,
    weak_students
)

from reports import generate_report

from analytics import (
    show_toppers,
    weak_students_analysis,
    attendance_risk,
    performance_insights,
    department_analysis
)

from exports import (
    export_students_excel,
    export_students_csv,
    backup_database
)

# ==========================================
# CREATE DATABASE TABLES
# ==========================================

create_tables()

# ==========================================
# LOGIN WINDOW
# ==========================================

login_window = tk.Tk()

login_window.title("School ERP Login")

login_window.geometry("500x450")

login_window.configure(bg="#121212")

# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    login_window,
    text="SCHOOL ERP SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#121212",
    fg="cyan"
)

title.pack(pady=30)

# ==========================================
# USERNAME
# ==========================================

username_label = tk.Label(
    login_window,
    text="Username",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

username_label.pack()

username_entry = tk.Entry(
    login_window,
    width=30,
    font=("Arial", 12)
)

username_entry.pack(pady=10)

# ==========================================
# PASSWORD
# ==========================================

password_label = tk.Label(
    login_window,
    text="Password",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="white"
)

password_label.pack()

password_entry = tk.Entry(
    login_window,
    show="*",
    width=30,
    font=("Arial", 12)
)

password_entry.pack(pady=10)

# ==========================================
# OPEN MAIN SYSTEM
# ==========================================

def open_main_system(role):

    login_window.destroy()

    root = tk.Tk()

    root.title("Professional School ERP")

    root.geometry("1900x1000")

    root.configure(bg="#1e1e1e")

    # TITLE

    heading = tk.Label(
        root,
        text="PROFESSIONAL SCHOOL ERP SYSTEM",
        font=("Arial", 26, "bold"),
        bg="#1e1e1e",
        fg="cyan"
    )

    heading.pack(pady=20)

    # ROLE

    role_label = tk.Label(
        root,
        text=f"Logged in as : {role}",
        font=("Arial", 12, "bold"),
        bg="#1e1e1e",
        fg="white"
    )

    role_label.pack()

    # ======================================
    # DASHBOARD
    # ======================================

    dashboard_frame = tk.Frame(
        root,
        bg="#1e1e1e"
    )

    dashboard_frame.pack(pady=20)

    student_card = tk.Label(
        dashboard_frame,
        bg="#2962ff",
        fg="white",
        width=20,
        height=5,
        font=("Arial", 14, "bold")
    )

    student_card.grid(row=0, column=0, padx=20)

    attendance_card = tk.Label(
        dashboard_frame,
        bg="#00c853",
        fg="white",
        width=20,
        height=5,
        font=("Arial", 14, "bold")
    )

    attendance_card.grid(row=0, column=1, padx=20)

    marks_card = tk.Label(
        dashboard_frame,
        bg="#ff1744",
        fg="white",
        width=20,
        height=5,
        font=("Arial", 14, "bold")
    )

    marks_card.grid(row=0, column=2, padx=20)

    # ======================================
    # REFRESH DASHBOARD
    # ======================================

    def refresh_dashboard():

        counts = get_dashboard_counts()

        student_card.config(
            text=f"Total Students\n\n{counts[0]}"
        )

        attendance_card.config(
            text=f"Attendance Records\n\n{counts[1]}"
        )

        marks_card.config(
            text=f"Marks Records\n\n{counts[2]}"
        )

    refresh_dashboard()

    # ======================================
    # INPUT FRAME
    # ======================================

    input_frame = tk.Frame(
        root,
        bg="#1e1e1e"
    )

    input_frame.pack(pady=20)

    # STUDENT ID

    tk.Label(
        input_frame,
        text="Student ID",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12, "bold")
    ).grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(
        input_frame,
        width=30,
        font=("Arial", 12)
    )

    id_entry.grid(row=0, column=1)

    # NAME

    tk.Label(
        input_frame,
        text="Student Name",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12, "bold")
    ).grid(row=1, column=0, padx=10, pady=10)

    name_entry = tk.Entry(
        input_frame,
        width=30,
        font=("Arial", 12)
    )

    name_entry.grid(row=1, column=1)

    # DEPARTMENT

    tk.Label(
        input_frame,
        text="Department",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12, "bold")
    ).grid(row=2, column=0, padx=10, pady=10)

    department_options = [
        "BIOLOGY SCIENCE",
        "COMPUTER SCIENCE",
        "COMMERCE",
        "HUMANITIES"
    ]

    dept_entry = ttk.Combobox(
        input_frame,
        values=department_options,
        state="readonly",
        width=28,
        font=("Arial", 12)
    )

    dept_entry.current(0)

    dept_entry.grid(row=2, column=1)

    # AGE

    tk.Label(
        input_frame,
        text="Age",
        bg="#1e1e1e",
        fg="white",
        font=("Arial", 12, "bold")
    ).grid(row=3, column=0, padx=10, pady=10)

    age_entry = tk.Entry(
        input_frame,
        width=30,
        font=("Arial", 12)
    )

    age_entry.grid(row=3, column=1)

    # ======================================
    # BUTTON FRAME
    # ======================================

    button_frame = tk.Frame(
        root,
        bg="#1e1e1e"
    )

    button_frame.pack(pady=20)

    buttons = [

        (
            "Add Student",
            lambda: add_student(
                id_entry,
                name_entry,
                dept_entry,
                age_entry,
                refresh_dashboard
            ),
            "#00c853"
        ),

        (
            "View Students",
            lambda: view_students(root),
            "#2962ff"
        ),

        (
            "Delete Student",
            lambda: delete_student(
                refresh_dashboard
            ),
            "#d50000"
        ),

        (
            "Search Student",
            search_student,
            "#ff9800"
        ),

        (
            "Update Student",
            lambda: update_student(
                refresh_dashboard
            ),
            "#9c27b0"
        ),

        (
            "Mark Attendance",
            lambda: mark_attendance(
                refresh_dashboard
            ),
            "#00bfa5"
        ),

        (
            "Attendance Analytics",
            attendance_analytics,
            "#26a69a"
        ),

        (
            "Low Attendance",
            low_attendance_students,
            "#ef6c00"
        ),

        (
            "Add Marks",
            lambda: add_marks(
                refresh_dashboard
            ),
            "#ff1744"
        ),

        (
            "Topper Analysis",
            topper_analysis,
            "#3949ab"
        ),

        (
            "Weak Students",
            weak_students,
            "#6d4c41"
        ),

        (
            "Generate Report",
            generate_report,
            "#ffd600"
        ),

        (
            "School Toppers",
            show_toppers,
            "#1e88e5"
        ),

        (
            "Performance Insights",
            performance_insights,
            "#43a047"
        ),

        (
            "Attendance Risk",
            attendance_risk,
            "#fb8c00"
        ),

        (
            "Department Analysis",
            department_analysis,
            "#8e24aa"
        ),

        (
            "Export Excel",
            export_students_excel,
            "#2e7d32"
        ),

        (
            "Export CSV",
            export_students_csv,
            "#0277bd"
        ),

        (
            "Backup Database",
            backup_database,
            "#5d4037"
        )

    ]

    row = 0
    column = 0

    for text, command, color in buttons:

        btn = tk.Button(
            button_frame,
            text=text,
            command=command,
            bg=color,
            fg="white",
            width=25,
            height=2,
            font=("Arial", 11, "bold")
        )

        btn.grid(
            row=row,
            column=column,
            padx=10,
            pady=10
        )

        column += 1

        if column > 2:

            column = 0
            row += 1

    root.mainloop()

# ==========================================
# LOGIN FUNCTION
# ==========================================

def login():

    username = username_entry.get()

    password = password_entry.get()

    success, role = validate_login(
        username,
        password
    )

    if success:

        show_login_success(role)

        open_main_system(role)

    else:

        show_login_error()

# ==========================================
# LOGIN BUTTON
# ==========================================

login_button = tk.Button(
    login_window,
    text="LOGIN",
    command=login,
    bg="cyan",
    fg="black",
    width=20,
    height=2,
    font=("Arial", 12, "bold")
)

login_button.pack(pady=30)

# ==========================================
# RUN APP
# ==========================================

login_window.mainloop()
