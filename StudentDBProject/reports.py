from tkinter import (
    messagebox,
    simpledialog
)

from database import cur

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

# ==========================================
# GENERATE PDF REPORT
# ==========================================

def generate_report():

    sid = simpledialog.askstring(
        "Generate Report",
        "Enter Student ID"
    )

    if sid is None:
        return

    # FETCH STUDENT DATA

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
            'No Marks Added'
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

    WHERE students.id=%s
    """, (sid,))

    student = cur.fetchone()

    if not student:

        messagebox.showerror(
            "Error",
            "Student Not Found"
        )

        return

    # FILE LOCATION

    filename = (
        f"/home/swaminathsd/Downloads/"
        f"{sid}_ReportCard.pdf"
    )

    # PDF DOCUMENT

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # TITLE

    title = Paragraph(
        """
        <font size=20>
        <b>SCHOOL REPORT CARD</b>
        </font>
        """,
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # DETAILS

    details = f"""
    <font size=12>

    <b>Student ID :</b> {student[0]}<br/><br/>

    <b>Student Name :</b> {student[1]}<br/><br/>

    <b>Department :</b> {student[2]}<br/><br/>

    <b>Age :</b> {student[3]}<br/><br/>

    <b>Attendance Percentage :</b>
    {student[4]:.2f}%<br/><br/>

    <b>Subjects & Marks :</b><br/><br/>

    {student[5].replace(chr(10), '<br/>')}<br/><br/>

    <b>Maximum Marks :</b>
    {student[6]}<br/><br/>

    <b>Obtained Marks :</b>
    {student[7]}<br/><br/>

    <b>Percentage :</b>
    {student[8]:.2f}%<br/><br/>

    <b>Grade :</b>
    {student[9]}<br/><br/>

    </font>
    """

    paragraph = Paragraph(
        details,
        styles['BodyText']
    )

    elements.append(paragraph)

    elements.append(Spacer(1, 40))

    # SIGNATURES

    signature = Paragraph(
        """
        <font size=12>

        _______________________<br/>
        Class Teacher Signature

        <br/><br/><br/>

        _______________________<br/>
        Principal Signature

        </font>
        """,
        styles['BodyText']
    )

    elements.append(signature)

    # BUILD PDF

    doc.build(elements)

    messagebox.showinfo(
        "PDF Generated",
        f"""
Report Card Generated Successfully

Saved To:

{filename}
"""
    )
