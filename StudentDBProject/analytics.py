from tkinter import messagebox

from database import cur

# ==========================================
# SHOW TOPPERS
# ==========================================

def show_toppers():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        students.department,
        marks.percentage

    FROM students

    INNER JOIN marks
    ON students.id = marks.student_id

    ORDER BY marks.percentage DESC

    LIMIT 10
    """)

    toppers = cur.fetchall()

    if not toppers:

        messagebox.showerror(
            "No Data",
            "No topper data found"
        )

        return

    result = "TOP STUDENTS\n\n"

    rank = 1

    for topper in toppers:

        result += (
            f"Rank : {rank}\n"
            f"Student ID : {topper[0]}\n"
            f"Name : {topper[1]}\n"
            f"Department : {topper[2]}\n"
            f"Percentage : {topper[3]:.2f}%\n\n"
        )

        rank += 1

    messagebox.showinfo(
        "School Toppers",
        result
    )

# ==========================================
# WEAK STUDENTS ANALYSIS
# ==========================================

def weak_students_analysis():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        students.department,
        marks.percentage

    FROM students

    INNER JOIN marks
    ON students.id = marks.student_id

    WHERE marks.percentage < 40
    """)

    students = cur.fetchall()

    if not students:

        messagebox.showinfo(
            "Analysis",
            "No weak students found"
        )

        return

    result = "WEAK STUDENTS\n\n"

    for student in students:

        result += (
            f"Student ID : {student[0]}\n"
            f"Name : {student[1]}\n"
            f"Department : {student[2]}\n"
            f"Percentage : {student[3]:.2f}%\n\n"
        )

    messagebox.showwarning(
        "Weak Students",
        result
    )

# ==========================================
# ATTENDANCE RISK
# ==========================================

def attendance_risk():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        attendance.attendance_percentage

    FROM students

    INNER JOIN attendance
    ON students.id = attendance.student_id

    WHERE attendance.attendance_percentage < 75
    """)

    students = cur.fetchall()

    if not students:

        messagebox.showinfo(
            "Attendance Analysis",
            "No attendance risk students"
        )

        return

    result = "LOW ATTENDANCE STUDENTS\n\n"

    for student in students:

        result += (
            f"Student ID : {student[0]}\n"
            f"Name : {student[1]}\n"
            f"Attendance : {student[2]:.2f}%\n\n"
        )

    messagebox.showwarning(
        "Attendance Risk",
        result
    )

# ==========================================
# PERFORMANCE INSIGHTS
# ==========================================

def performance_insights():

    cur.execute("""
    SELECT
        AVG(percentage)
    FROM marks
    """)

    avg_percentage = cur.fetchone()[0]

    if avg_percentage is None:

        messagebox.showerror(
            "No Data",
            "No marks data found"
        )

        return

    performance = ""

    if avg_percentage >= 90:

        performance = "Excellent School Performance"

    elif avg_percentage >= 75:

        performance = "Good School Performance"

    elif avg_percentage >= 50:

        performance = "Average School Performance"

    else:

        performance = "Poor School Performance"

    messagebox.showinfo(
        "Performance Insights",
        f"""
Average School Percentage : {avg_percentage:.2f}%

Performance Status :

{performance}
"""
    )

# ==========================================
# DEPARTMENT ANALYSIS
# ==========================================

def department_analysis():

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

    result = "DEPARTMENT ANALYSIS\n\n"

    for row in rows:

        result += (
            f"Department : {row[0]}\n"
            f"Average Percentage : {row[1]:.2f}%\n\n"
        )

    messagebox.showinfo(
        "Department Analysis",
        result
    )
