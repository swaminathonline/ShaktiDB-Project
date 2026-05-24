#!/bin/bash

# ==========================================
# STUDENT MANAGEMENT SYSTEM
# ==========================================

students_file="students.txt"

# Create file if not exists
touch $students_file

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Login Function
login() {

clear
echo "====================================="
echo "        LOGIN SYSTEM"
echo "====================================="

read -p "Enter Username: " user
read -s -p "Enter Password: " pass

echo ""

if [[ $user == "admin" && $pass == "1234" ]]
then
    echo -e "${GREEN}Login Successful${NC}"
    sleep 2
else
    echo -e "${RED}Invalid Login${NC}"
    sleep 2
    login
fi
}

# Add Student
add_student() {

clear

echo "====================================="
echo "          ADD STUDENT"
echo "====================================="

read -p "Enter Student ID: " id
read -p "Enter Name: " name
read -p "Enter Department: " dept
read -p "Enter Age: " age
read -p "Enter Phone: " phone

echo "$id | $name | $dept | $age | $phone" >> $students_file

echo -e "${GREEN}Student Added Successfully${NC}"

read -p "Press Enter to continue..."
}

# View Students
view_students() {

clear

echo "====================================="
echo "         STUDENT RECORDS"
echo "====================================="

cat $students_file

echo ""
read -p "Press Enter to continue..."
}

# Search Student
search_student() {

clear

echo "====================================="
echo "         SEARCH STUDENT"
echo "====================================="

read -p "Enter Name or ID: " search

grep -i "$search" $students_file

echo ""
read -p "Press Enter to continue..."
}

# Delete Student
delete_student() {

clear

echo "====================================="
echo "         DELETE STUDENT"
echo "====================================="

read -p "Enter Student ID to Delete: " did

grep -v "^$did" $students_file > temp.txt

mv temp.txt $students_file

echo -e "${GREEN}Deleted Successfully${NC}"

read -p "Press Enter to continue..."
}

# Update Student
update_student() {

clear

echo "====================================="
echo "         UPDATE STUDENT"
echo "====================================="

read -p "Enter Student ID to Update: " uid

grep -v "^$uid" $students_file > temp.txt

mv temp.txt $students_file

echo "Enter New Details"

read -p "Enter Student ID: " id
read -p "Enter Name: " name
read -p "Enter Department: " dept
read -p "Enter Age: " age
read -p "Enter Phone: " phone

echo "$id | $name | $dept | $age | $phone" >> $students_file

echo -e "${GREEN}Updated Successfully${NC}"

read -p "Press Enter to continue..."
}

# Count Students
count_students() {

clear

echo "====================================="
echo "         TOTAL STUDENTS"
echo "====================================="

count=$(wc -l < $students_file)

echo "Total Students: $count"

echo ""
read -p "Press Enter to continue..."
}

# Backup Records
backup_records() {

clear

cp $students_file backup_students.txt

echo -e "${GREEN}Backup Created Successfully${NC}"

read -p "Press Enter to continue..."
}

# Show Date
show_date() {

clear

echo "====================================="
echo "           CURRENT DATE"
echo "====================================="

date

echo ""
read -p "Press Enter to continue..."
}

# Show Calendar
show_calendar() {

clear

echo "====================================="
echo "            CALENDAR"
echo "====================================="

cal

echo ""
read -p "Press Enter to continue..."
}

# Show Disk Space
disk_space() {

clear

echo "====================================="
echo "           DISK SPACE"
echo "====================================="

df -h

echo ""
read -p "Press Enter to continue..."
}

# Show RAM Usage
ram_usage() {

clear

echo "====================================="
echo "            RAM USAGE"
echo "====================================="

free -h

echo ""
read -p "Press Enter to continue..."
}

# Show Logged Users
logged_users() {

clear

echo "====================================="
echo "          LOGGED USERS"
echo "====================================="

who

echo ""
read -p "Press Enter to continue..."
}

# Calculator
calculator() {

clear

echo "====================================="
echo "            CALCULATOR"
echo "====================================="

read -p "Enter First Number: " a
read -p "Enter Second Number: " b

echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"

read -p "Choose Option: " op

case $op in

1)
    result=$((a+b))
    echo "Result = $result"
    ;;

2)
    result=$((a-b))
    echo "Result = $result"
    ;;

3)
    result=$((a*b))
    echo "Result = $result"
    ;;

4)
    result=$((a/b))
    echo "Result = $result"
    ;;

*)
    echo "Invalid Choice"
    ;;

esac

echo ""
read -p "Press Enter to continue..."
}

# Main Menu
main_menu() {

while true
do

clear

echo -e "${BLUE}"
echo "====================================="
echo "      STUDENT MANAGEMENT SYSTEM"
echo "====================================="
echo -e "${NC}"

echo "1. Add Student"
echo "2. View Students"
echo "3. Search Student"
echo "4. Delete Student"
echo "5. Update Student"
echo "6. Count Students"
echo "7. Backup Records"
echo "8. Show Date"
echo "9. Show Calendar"
echo "10. Disk Space"
echo "11. RAM Usage"
echo "12. Logged Users"
echo "13. Calculator"
echo "14. Exit"

echo ""

read -p "Enter your choice: " choice

case $choice in

1)
    add_student
    ;;

2)
    view_students
    ;;

3)
    search_student
    ;;

4)
    delete_student
    ;;

5)
    update_student
    ;;

6)
    count_students
    ;;

7)
    backup_records
    ;;

8)
    show_date
    ;;

9)
    show_calendar
    ;;

10)
    disk_space
    ;;

11)
    ram_usage
    ;;

12)
    logged_users
    ;;

13)
    calculator
    ;;

14)
    echo "Thank You"
    exit
    ;;

*)
    echo -e "${RED}Invalid Choice${NC}"
    sleep 2
    ;;

esac

done
}

# Program Start
login
main_menu
