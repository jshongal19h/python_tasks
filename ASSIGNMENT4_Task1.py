# ASSIGNMENT 4:
# Module 5: Files, Exceptions, and Errors in Python
 
# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
 
# Expected Output:

# If the file exists:


try:
       with open("Sample.txt", "rt") as fh:
        contents = fh.readlines()
        for lines in contents:
            print(lines)
        # line1 =fh.readline()
        # line2 =fh.readline()
        # line3 =fh.readline()
        # print(f"Reading the file content: ")
        # print(f"Line1 is {line1} ")
        # print(f"Line2 is {line2} ")
        # print(f"Line3 is {line3} ")

except FileNotFoundError as file_error:
     file_error = ("Error: The file 'Sample.txt' not found")
     print(file_error)
