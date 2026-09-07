import mysql.connector
import getpass
print("b.Tech student progress AI Tracker")
print("starting..")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass.getpass("Enter mysql password:"),
    database="btech_student_tracker"
)
if connection.is_connected():
    print("mysql Database connected sussfully!")

print("\n==============ADD STUDENT============")
roll_no=input("Enter Roll No:")
name=input("Enter Student Name:")
email=input("Enter Email:")
phone=input("Enter Phone:")
branch=input("Enter Branch:")
semester=int(input("Enter Semester:"))
subjects=[]
marks=[]
for i in range(6):
    print(f"\nSubject{i+1}")
    subject=input("Enter the subject Name:")
    mark=float(input("Enter marks(0-100):"))
    subjects.append(subject)
    marks.append(mark)

print("\nStudent details received successfully!")

print("Roll No:",roll_no)
print("Name:",name)
print("Email:",email)
print("Phone:",phone)
print("Branch:",branch)
print("Semester:",semester)

print("\nsubjects and Marks:")
for i in range(6):
    print(subjects[i],":",marks[i])
# ==============================
# PERFORMANCE CALCULATION
# ==============================

grades = []

for mark in marks:
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 40:
        grade = "C"
    else:
        grade = "F"

    grades.append(grade)

average = sum(marks) / 6

cgpa = round(average / 10, 2)

highest = max(marks)
lowest = min(marks)

weak_index = marks.index(lowest)
weak_subject = subjects[weak_index]

if average >= 80:
    performance = "Excellent"
elif average >= 60:
    performance = "Good"
elif average >= 40:
    performance = "Average"
else:
    performance = "Needs Improvement"


print("\n===== PERFORMANCE ANALYSIS =====")

for i in range(6):
    print(subjects[i], ":", marks[i], "Grade:", grades[i])

print("\nAverage Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("CGPA:", cgpa)
print("Overall Performance:", performance)
print("Weak Subject:", weak_subject)

# ==============================
# SAVE DATA INTO DATABASE
# ==============================

cursor = connection.cursor()

# Insert student details
student_query = """
INSERT INTO STUDENTS
(ROLL_NO, NAME, EMAIL, PHONE, BRANCH, SEMESTER, CGPA)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

student_values = (
    roll_no,
    name,
    email,
    phone,
    branch,
    semester,
    cgpa
)

cursor.execute(student_query, student_values)

# Get automatically generated Student ID
student_id = cursor.lastrowid

# Insert 6 subjects and marks
performance_query = """
INSERT INTO PERFORMANCE
(STUDENT_ID, SUBJECT, MARKS, GRADE)
VALUES (%s, %s, %s, %s)
"""

for i in range(6):
    performance_values = (
        student_id,
        subjects[i],
        marks[i],
        grades[i]
    )

    cursor.execute(performance_query, performance_values)

# Save permanently
connection.commit()

print("\nData stored in MySQL successfully!")
print("Student ID:", student_id)

