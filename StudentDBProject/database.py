import psycopg2

# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = psycopg2.connect(
    dbname="postgres",
    user="swaminathsd",
    password="1234",
    host="localhost"
)

cur = conn.cursor()

# ==========================================
# CREATE TABLES
# ==========================================

def create_tables():

    # STUDENTS TABLE

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(50),
        age INT
    )
    """)

    # ATTENDANCE TABLE

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        student_id VARCHAR(20) PRIMARY KEY,
        present_days INT,
        absent_days INT,
        attendance_percentage FLOAT
    )
    """)

    # MARKS TABLE

    cur.execute("""
    CREATE TABLE IF NOT EXISTS marks(
        student_id VARCHAR(20) PRIMARY KEY,
        subjects TEXT,
        max_marks INT,
        obtained_marks INT,
        percentage FLOAT,
        grade VARCHAR(10)
    )
    """)

    conn.commit()

# ==========================================
# ADD STUDENT
# ==========================================

def add_student_db(
    sid,
    name,
    department,
    age
):

    cur.execute(
        "SELECT * FROM students WHERE id=%s",
        (sid,)
    )

    existing = cur.fetchone()

    if existing:

        return False

    cur.execute(
        """
        INSERT INTO students(
            id,
            name,
            department,
            age
        )
        VALUES(%s,%s,%s,%s)
        """,
        (
            sid,
            name,
            department,
            age
        )
    )

    conn.commit()

    return True

# ==========================================
# GET ALL STUDENTS
# ==========================================

def get_all_students():

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

    return cur.fetchall()

# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student_db(sid):

    cur.execute(
        """
        DELETE FROM attendance
        WHERE student_id=%s
        """,
        (sid,)
    )

    cur.execute(
        """
        DELETE FROM marks
        WHERE student_id=%s
        """,
        (sid,)
    )

    cur.execute(
        """
        DELETE FROM students
        WHERE id=%s
        """,
        (sid,)
    )

    conn.commit()

# ==========================================
# DASHBOARD COUNTS
# ==========================================

def get_dashboard_counts():

    cur.execute(
        "SELECT COUNT(*) FROM students"
    )

    student_count = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM attendance"
    )

    attendance_count = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM marks"
    )

    marks_count = cur.fetchone()[0]

    return (
        student_count,
        attendance_count,
        marks_count
    )
