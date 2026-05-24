from tabulate import tabulate
import psycopg2
import datetime

# =========================================
# DATABASE CONNECTION
# =========================================

conn = psycopg2.connect(
    dbname="postgres",
    user="swaminathsd",
    password="1234",
    host="localhost"
)

cur = conn.cursor()

# =========================================
# CREATE STUDENTS TABLE
# =========================================

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    age INT
)
""")

conn.commit()

# =========================================
# CREATE ATTENDANCE TABLE
# =========================================

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    student_id INT,
    student_name VARCHAR(100),
    status VARCHAR(20),
    attendance_date DATE
)
""")

conn.commit()

# =========================================
# LOGIN SYSTEM
# =========================================

print("====================================")
print("         LOGIN SYSTEM")
print("====================================")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username != "admin" or password != "1234":
    print("Invalid Login")
    exit()

print("Login Successful")

# =========================================
# MAIN MENU LOOP
# =========================================

while True:

    print("\n====================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Count Students")
    print("7. Show Date and Time")
    print("8. Mark Attendance")
    print("9. View Attendance")
    print("10. Exit")

    choice = input("Enter Choice: ")

    # =====================================
    # ADD STUDENT
    # =====================================

    if choice == "1":

        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        age = int(input("Enter Age: "))

        cur.execute(
            """
            INSERT INTO students(name, department, age)
            VALUES(%s,%s,%s)
            """,
            (name, department, age)
        )

        conn.commit()

        print("Student Added Successfully")

    # =====================================
    # VIEW STUDENTS
    # =====================================

    elif choice == "2":

        cur.execute("SELECT * FROM students")

        rows = cur.fetchall()

        if len(rows) == 0:

            print("No Student Records Found")

        else:

            print("\nSTUDENT RECORDS")

            print(tabulate(
                rows,
                headers=["ID", "Name", "Department", "Age"],
                tablefmt="grid"
            ))

    # =====================================
    # SEARCH STUDENT
    # =====================================

    elif choice == "3":

        search = input("Enter Student Name: ")

        cur.execute(
            """
            SELECT * FROM students
            WHERE name=%s
            """,
            (search,)
        )

        rows = cur.fetchall()

        if len(rows) == 0:

            print("Student Not Found")

        else:

            print("\nSEARCH RESULTS")

            print(tabulate(
                rows,
                headers=["ID", "Name", "Department", "Age"],
                tablefmt="grid"
            ))

    # =====================================
    # DELETE STUDENT
    # =====================================

    elif choice == "4":

        sid = int(input("Enter Student ID to Delete: "))

        cur.execute(
            """
            DELETE FROM students
            WHERE id=%s
            """,
            (sid,)
        )

        conn.commit()

        print("Student Deleted Successfully")

    # =====================================
    # UPDATE STUDENT
    # =====================================

    elif choice == "5":

        sid = int(input("Enter Student ID to Update: "))

        new_name = input("Enter New Name: ")
        new_department = input("Enter New Department: ")
        new_age = int(input("Enter New Age: "))

        cur.execute(
            """
            UPDATE students
            SET name=%s,
                department=%s,
                age=%s
            WHERE id=%s
            """,
            (new_name, new_department, new_age, sid)
        )

        conn.commit()

        print("Student Updated Successfully")

    # =====================================
    # COUNT STUDENTS
    # =====================================

    elif choice == "6":

        cur.execute("SELECT COUNT(*) FROM students")

        count = cur.fetchone()[0]

        print(f"Total Students = {count}")

    # =====================================
    # SHOW DATE AND TIME
    # =====================================

    elif choice == "7":

        now = datetime.datetime.now()

        print("Current Date and Time:")
        print(now)

    # =====================================
    # MARK ATTENDANCE
    # =====================================

    elif choice == "8":

        sid = int(input("Enter Student ID: "))
        sname = input("Enter Student Name: ")
        status = input("Enter Status (Present/Absent): ")

        cur.execute(
            """
            INSERT INTO attendance(
                student_id,
                student_name,
                status,
                attendance_date
            )
            VALUES(%s,%s,%s,CURRENT_DATE)
            """,
            (sid, sname, status)
        )

        conn.commit()

        print("Attendance Marked Successfully")

    # =====================================
    # VIEW ATTENDANCE
    # =====================================

    elif choice == "9":

        cur.execute("SELECT * FROM attendance")

        rows = cur.fetchall()

        if len(rows) == 0:

            print("No Attendance Records")

        else:

            print("\nATTENDANCE RECORDS")

            print(tabulate(
                rows,
                headers=[
                    "Student ID",
                    "Student Name",
                    "Status",
                    "Date"
                ],
                tablefmt="grid"
            ))

    # =====================================
    # EXIT
    # =====================================

    elif choice == "10":

        print("Thank You")
        break

    # =====================================
    # INVALID OPTION
    # =====================================

    else:

        print("Invalid Choice")

# =========================================
# CLOSE DATABASE CONNECTION
# =========================================

cur.close()
conn.close()
