import matplotlib.pyplot as plt

from tkinter import messagebox

from database import cur

# ==========================================

# PERFORMANCE CHART

# ==========================================

def performance_chart():

cur.execute("""
SELECT
    students.name,
    marks.percentage

FROM students

INNER JOIN marks
ON students.id = marks.student_id
""")

rows = cur.fetchall()

if not rows:

    messagebox.showerror(
        "No Data",
        "No marks data found"
    )

    return

names = []
percentages = []

for row in rows:

    names.append(row[0])

    percentages.append(row[1])

plt.figure(figsize=(12, 6))

plt.bar(
    names,
    percentages
)

plt.xlabel("Students")

plt.ylabel("Percentage")

plt.title("Student Performance Chart")

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()

# ==========================================

# ATTENDANCE CHART

# ==========================================

def attendance_chart():

cur.execute("""
SELECT
    students.name,
    attendance.attendance_percentage

FROM students

INNER JOIN attendance
ON students.id = attendance.student_id
""")

rows = cur.fetchall()

if not rows:

    messagebox.showerror(
        "No Data",
        "No attendance data found"
    )

    return

names = []
attendance = []

for row in rows:

    names.append(row[0])

    attendance.append(row[1])

plt.figure(figsize=(12, 6))

plt.plot(
    names,
    attendance,
    marker="o"
)

plt.xlabel("Students")

plt.ylabel("Attendance %")

plt.title("Attendance Analysis")

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()

# ==========================================

# DEPARTMENT CHART

# ==========================================

def department_chart():

cur.execute("""
SELECT
    students.department,
    AVG(marks.percentage)

FROM students

INNER JOIN marks
ON students.id = marks.student_id

GROUP BY students.department
""")

rows = cur.fetchall()

if not rows:

    messagebox.showerror(
        "No Data",
        "No department data found"
    )

    return

departments = []
averages = []

for row in rows:

    departments.append(row[0])

    averages.append(row[1])

plt.figure(figsize=(10, 6))

plt.pie(
    averages,
    labels=departments,
    autopct='%1.1f%%'
)

plt.title("Department Performance")

plt.show()

