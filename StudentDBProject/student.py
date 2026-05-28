from tkinter import (
    ttk,
    messagebox,
    simpledialog,
    Toplevel,
    BOTH,
    END
)

from database import (
    add_student_db,
    get_all_students,
    delete_student_db,
    cur,
    conn
)

# ==========================================
# ADD STUDENT
# ==========================================

def add_student(
    id_entry,
    name_entry,
    dept_entry,
    age_entry,
    refresh_dashboard
):

    sid = id_entry.get().strip()

    name = name_entry.get().strip()

    dept = dept_entry.get().strip()

    age = age_entry.get().strip()

    if not sid or not name or not age:

        messagebox.showerror(
            "Error",
            "Fill all fields"
        )

        return

    success = add_student_db(
        sid,
        name,
        dept,
        age
    )

    if success:

        conn.commit()

        refresh_dashboard()

        messagebox.showinfo(
            "Success",
            "Student Added Successfully"
        )

        id_entry.delete(0, END)

        name_entry.delete(0, END)

        age_entry.delete(0, END)

    else:

        messagebox.showerror(
            "Duplicate",
            "Student ID already exists"
        )

# ==========================================
# VIEW STUDENTS
# ==========================================

def view_students(root):

    window = Toplevel(root)

    window.title("Student Records")

    window.geometry("1800x700")

    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "NAME",
            "DEPARTMENT",
            "AGE",
            "ATTENDANCE",
            "SUBJECTS",
            "MAXIMUM",
            "OBTAINED",
            "PERCENTAGE",
            "GRADE"
        ),
        show="headings"
    )

    headings = [
        "ID",
        "NAME",
        "DEPARTMENT",
        "AGE",
        "ATTENDANCE",
        "SUBJECTS",
        "MAXIMUM",
        "OBTAINED",
        "PERCENTAGE",
        "GRADE"
    ]

    for h in headings:

        tree.heading(h, text=h)

        tree.column(h, width=170)

    tree.pack(fill=BOTH, expand=True)

    rows = get_all_students()

    for row in rows:

        tree.insert(
            "",
            END,
            values=row
        )

# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student(refresh_dashboard):

    sid = simpledialog.askstring(
        "Delete Student",
        "Enter Student ID"
    )

    if sid is None:
        return

    delete_student_db(sid)

    conn.commit()

    refresh_dashboard()

    messagebox.showinfo(
        "Deleted",
        "Student Deleted Successfully"
    )

# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student():

    sid = simpledialog.askstring(
        "Search Student",
        "Enter Student ID"
    )

    if sid is None:
        return

    cur.execute(
        """
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

        WHERE students.id=%s
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

    result = f"""
Student ID : {student[0]}

Name : {student[1]}

Department : {student[2]}

Age : {student[3]}

Attendance : {student[4]}%

Subjects:

{student[5]}

Percentage : {student[6]}%

Grade : {student[7]}
"""

    messagebox.showinfo(
        "Student Details",
        result
    )

# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student(refresh_dashboard):

    sid = simpledialog.askstring(
        "Update Student",
        "Enter Student ID"
    )

    if sid is None:
        return

    cur.execute(
        "SELECT * FROM students WHERE id=%s",
        (sid,)
    )

    student = cur.fetchone()

    if not student:

        messagebox.showerror(
            "Error",
            "Student Not Found"
        )

        return

    new_name = simpledialog.askstring(
        "Update",
        "Enter New Name"
    )

    new_department = simpledialog.askstring(
        "Update",
        "Enter New Department"
    )

    new_age = simpledialog.askinteger(
        "Update",
        "Enter New Age"
    )

    cur.execute(
        """
        UPDATE students
        SET
            name=%s,
            department=%s,
            age=%s
        WHERE id=%s
        """,
        (
            new_name,
            new_department,
            new_age,
            sid
        )
    )

    conn.commit()

    refresh_dashboard()

    messagebox.showinfo(
        "Updated",
        "Student Updated Successfully"
    )
