from tkinter import (
    messagebox,
    simpledialog
)

from database import (
    cur,
    conn
)

# ==========================================
# GET SUBJECTS
# ==========================================

def get_subjects(department):

    if department == "BIOLOGY SCIENCE":

        return [
            "Physics",
            "Chemistry",
            "Mathematics",
            "Biology",
            "English"
        ]

    elif department == "COMPUTER SCIENCE":

        return [
            "Physics",
            "Chemistry",
            "Mathematics",
            "Computer Science",
            "English"
        ]

    elif department == "COMMERCE":

        return [
            "Accountancy",
            "Business Studies",
            "Economics",
            "English"
        ]

    elif department == "HUMANITIES":

        return [
            "History",
            "Political Science",
            "Economics",
            "Sociology",
            "Geography",
            "English"
        ]

    return []

# ==========================================
# CALCULATE GRADE
# ==========================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "FAIL"

# ==========================================
# ADD MARKS
# ==========================================

def add_marks(refresh_dashboard):

    sid = simpledialog.askstring(
        "Marks Entry",
        "Enter Student ID"
    )

    if sid is None:
        return

    # GET STUDENT

    cur.execute(
        """
        SELECT
            name,
            department
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

    student_name = student[0]

    department = student[1]

    subjects = get_subjects(department)

    # SECOND LANGUAGE

    second_language = simpledialog.askstring(
        "Second Language",
        "Enter Hindi or Malayalam"
    )

    if second_language is None:
        return

    subjects.append(second_language)

    subject_text = ""

    total_max = 0

    total_obtained = 0

    # SUBJECT ENTRY

    for subject in subjects:

        max_mark = simpledialog.askinteger(
            "Maximum Marks",
            f"Enter Maximum Marks for {subject}"
        )

        if max_mark is None:
            return

        obtained = simpledialog.askinteger(
            "Obtained Marks",
            f"Enter Obtained Marks for {subject}"
        )

        if obtained is None:
            return

        if obtained > max_mark:

            messagebox.showerror(
                "Invalid Marks",
                f"{subject} marks exceed maximum"
            )

            return

        total_max += max_mark

        total_obtained += obtained

        subject_text += (
            f"{subject} : "
            f"{obtained}/{max_mark}\n"
        )

    # PERCENTAGE

    percentage = (
        total_obtained / total_max
    ) * 100

    grade = calculate_grade(percentage)

    # DELETE OLD RECORD

    cur.execute(
        """
        DELETE FROM marks
        WHERE student_id=%s
        """,
        (sid,)
    )

    # INSERT NEW RECORD

    cur.execute(
        """
        INSERT INTO marks(
            student_id,
            subjects,
            max_marks,
            obtained_marks,
            percentage,
            grade
        )
        VALUES(%s,%s,%s,%s,%s,%s)
        """,
        (
            sid,
            subject_text,
            total_max,
            total_obtained,
            percentage,
            grade
        )
    )

    conn.commit()

    refresh_dashboard()

    result = f"""
Student Name : {student_name}

Department : {department}

--------------------------------

{subject_text}

--------------------------------

Maximum Marks : {total_max}

Obtained Marks : {total_obtained}

Percentage : {percentage:.2f}%

Grade : {grade}
"""

    messagebox.showinfo(
        "Marks Added Successfully",
        result
    )

# ==========================================
# TOPPER ANALYSIS
# ==========================================

def topper_analysis():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        marks.percentage

    FROM students

    INNER JOIN marks
    ON students.id = marks.student_id

    ORDER BY marks.percentage DESC

    LIMIT 1
    """)

    topper = cur.fetchone()

    if not topper:

        messagebox.showerror(
            "No Data",
            "No marks records found"
        )

        return

    result = f"""
School Topper

Student ID : {topper[0]}

Name : {topper[1]}

Percentage : {topper[2]:.2f}%
"""

    messagebox.showinfo(
        "Topper Analysis",
        result
    )

# ==========================================
# WEAK STUDENTS
# ==========================================

def weak_students():

    cur.execute("""
    SELECT
        students.id,
        students.name,
        marks.percentage

    FROM students

    INNER JOIN marks
    ON students.id = marks.student_id

    WHERE marks.percentage < 40
    """)

    rows = cur.fetchall()

    if not rows:

        messagebox.showinfo(
            "Result",
            "No weak students found"
        )

        return

    result = ""

    for row in rows:

        result += (
            f"ID : {row[0]}\n"
            f"Name : {row[1]}\n"
            f"Percentage : {row[2]:.2f}%\n\n"
        )

    messagebox.showwarning(
        "Weak Students",
        result
    )
