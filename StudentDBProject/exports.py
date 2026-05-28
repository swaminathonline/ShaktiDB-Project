from tkinter import messagebox

import pandas as pd

from database import cur

# ==========================================
# EXPORT TO EXCEL
# ==========================================

def export_students_excel():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        students.department,
        students.age,

        COALESCE(
            attendance.attendance_percentage,
            0
        ),

        COALESCE(
            marks.subjects,
            'No Marks'
        ),

        COALESCE(
            marks.max_marks,
            0
        ),

        COALESCE(
            marks.obtained_marks,
            0
        ),

        COALESCE(
            marks.percentage,
            0
        ),

        COALESCE(
            marks.grade,
            'N/A'
        )

    FROM students

    LEFT JOIN attendance
    ON students.id = attendance.student_id

    LEFT JOIN marks
    ON students.id = marks.student_id
    """)

    rows = cur.fetchall()

    if not rows:

        messagebox.showerror(
            "No Data",
            "No student data found"
        )

        return

    columns = [
        "Student ID",
        "Name",
        "Department",
        "Age",
        "Attendance %",
        "Subjects",
        "Maximum Marks",
        "Obtained Marks",
        "Percentage",
        "Grade"
    ]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    filename = (
        "/home/swaminathsd/Downloads/"
        "Student_Records.xlsx"
    )

    df.to_excel(
        filename,
        index=False
    )

    messagebox.showinfo(
        "Excel Export Success",
        f"""
Student Records Exported Successfully

Saved To:

{filename}
"""
    )

# ==========================================
# EXPORT TO CSV
# ==========================================

def export_students_csv():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        students.department,
        students.age,

        COALESCE(
            attendance.attendance_percentage,
            0
        ),

        COALESCE(
            marks.subjects,
            'No Marks'
        ),

        COALESCE(
            marks.max_marks,
            0
        ),

        COALESCE(
            marks.obtained_marks,
            0
        ),

        COALESCE(
            marks.percentage,
            0
        ),

        COALESCE(
            marks.grade,
            'N/A'
        )

    FROM students

    LEFT JOIN attendance
    ON students.id = attendance.student_id

    LEFT JOIN marks
    ON students.id = marks.student_id
    """)

    rows = cur.fetchall()

    if not rows:

        messagebox.showerror(
            "No Data",
            "No student data found"
        )

        return

    columns = [
        "Student ID",
        "Name",
        "Department",
        "Age",
        "Attendance %",
        "Subjects",
        "Maximum Marks",
        "Obtained Marks",
        "Percentage",
        "Grade"
    ]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    filename = (
        "/home/swaminathsd/Downloads/"
        "Student_Records.csv"
    )

    df.to_csv(
        filename,
        index=False
    )

    messagebox.showinfo(
        "CSV Export Success",
        f"""
Student Records Exported Successfully

Saved To:

{filename}
"""
    )

# ==========================================
# DATABASE BACKUP
# ==========================================

def backup_database():

    cur.execute(
        "SELECT * FROM students"
    )

    students = cur.fetchall()

    cur.execute(
        "SELECT * FROM attendance"
    )

    attendance = cur.fetchall()

    cur.execute(
        "SELECT * FROM marks"
    )

    marks = cur.fetchall()

    filename = (
        "/home/swaminathsd/Downloads/"
        "School_ERP_Backup.txt"
    )

    with open(filename, "w") as file:

        file.write(
            "========== STUDENTS ==========\n\n"
        )

        for student in students:

            file.write(str(student) + "\n")

        file.write(
            "\n========== ATTENDANCE ==========\n\n"
        )

        for att in attendance:

            file.write(str(att) + "\n")

        file.write(
            "\n========== MARKS ==========\n\n"
        )

        for mark in marks:

            file.write(str(mark) + "\n")

    messagebox.showinfo(
        "Backup Success",
        f"""
Database Backup Created Successfully

Saved To:

{filename}
"""
    )
