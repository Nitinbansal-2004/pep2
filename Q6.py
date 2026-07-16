# 6. Write a complete program that does all of the following:
# a) Creates a module called student_utils.py with: •  A function get_grade(avg) that returns
# grade using default argument for pass_mark=40 • A function calculate_average(*marks) using *args 
# b) In the main program, import student_utils and:
# •  Accept details for 3 students (name, 3 subject marks) from the user 
# •Calculate average and grade for each student •  Use exception handling to catch 
# invalid marks (non-numeric or < 0 or > 100)
# c) Write the report to a text file 'report.txt' in this format: Name: Priya | Average: 87.33 |
# Grade: A Name: Raj  | Average: 54.00 | Grade: C
# d) Also save all student data to a JSON file 'students.json' 
# e) Read back both files and print their contents to the console 
# f) Use readlines() to read 'report.txt' line by line and print each line with its line number

import student_utils
import json

students = []

for i in range(3):
    name = input("Enter Name: ")

    while True:
        try:
            m1 = float(input(""))
            m2 = float(input(""))
            m3 = float(input(""))

            if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
                raise ValueError("Marks must be between 0 and 100.")
            break

        except ValueError as e:
            print(e)

    avg = student_utils.calculate_average(m1, m2, m3)
    grade = student_utils.get_grade(avg)

    students.append({
        "Name": name,
        "Average": avg,
        "Grade": grade
    })


with open("report.txt", "w") as f:
    for s in students:
        f.write(f"Name: {s['Name']} | Average: {s['Average']:.2f} | Grade: {s['Grade']}\n")

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

with open("report.txt", "r") as f:
    print(f.read())

with open("students.json", "r") as f:
    print(f.read())

with open("report.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    print( lines[i])
