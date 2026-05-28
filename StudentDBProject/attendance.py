from tkinter import (
    messagebox,
    simpledialog
)

from database import (
    cur,
    conn
)

# ==========================================
# MARK ATTENDANCE
# ==========================================

def mark_attendance(refresh_dashboard):

    sid = simpledialog.askstring(
        "Attendance",
        "Enter Student ID"
    )

    if sid is None:
        return

    cur.execute(
        """
        SELECT name
        FROM students
        WHERE id=%s
        """,
        (sid,)
    )

    student = cur.fetchone()

    if not student:

        messagebox.showerror(
            "Error",
            "Student Not Found"
        )

        return

    present = simpledialog.askinteger(
        "Attendance",
        "Enter Present Days"
    )

    if present is None:
        return

    absent = simpledialog.askinteger(
        "Attendance",
        "Enter Absent Days"
    )

    if absent is None:
        return

    total_days = present + absent

    if total_days == 0:

        percentage = 0

    else:

        percentage = (
            present / total_days
        ) * 100

    cur.execute(
        """
        DELETE FROM attendance
        WHERE student_id=%s
        """,
        (sid,)
    )

    cur.execute(
        """
        INSERT INTO attendance(
            student_id,
            present_days,
            absent_days,
            attendance_percentage
        )
        VALUES(%s,%s,%s,%s)
        """,
        (
            sid,
            present,
            absent,
            percentage
        )
    )

    conn.commit()

    refresh_dashboard()

    messagebox.showinfo(
        "Attendance Updated",
        f"""
Student ID : {sid}

Present Days : {present}

Absent Days : {absent}

Attendance Percentage : {percentage:.2f}%
"""
    )

# ==========================================
# ATTENDANCE ANALYTICS
# ==========================================

def attendance_analytics():

    cur.execute("""
    SELECT
        students.id,
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
            "No attendance records found"
        )

        return

    result = ""

    for row in rows:

        sid = row[0]

        name = row[1]

        percentage = row[2]

        status = ""

        if percentage >= 90:

            status = "Excellent"

        elif percentage >= 75:

            status = "Good"

        elif percentage >= 50:

            status = "Average"

        else:

            status = "Low Attendance"

        result += (
            f"ID : {sid}\n"
            f"Name : {name}\n"
            f"Attendance : {percentage:.2f}%\n"
            f"Status : {status}\n\n"
        )

    messagebox.showinfo(
        "Attendance Analytics",
        result
    )

# ==========================================
# LOW ATTENDANCE
# ==========================================

def low_attendance_students():

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

    rows = cur.fetchall()

    if not rows:

        messagebox.showinfo(
            "Result",
            "No low attendance students"
        )

        return

    result = ""

    for row in rows:

        result += (
            f"ID : {row[0]}\n"
            f"Name : {row[1]}\n"
            f"Attendance : {row[2]:.2f}%\n\n"
        )

    messagebox.showwarning(
        "Low Attendance Students",
        result
    )
