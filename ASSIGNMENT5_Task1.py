# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


students_list = { "John" : 89, "Steve" : 90, "Reena" : 45 }
input_student_name = input("Enter student name: ")
if input_student_name in students_list:
    marks = students_list[input_student_name]
    print(f"{input_student_name} obtained {marks} marks")
else:
    print("Student name not found!!!")