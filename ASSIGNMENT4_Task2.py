
# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.
 
input_text = input("Enter the text that you would like to save in the output.txt file: ")
try:
    with open("output.txt", "wt") as fh:
        fh.write(input_text + "\n")
    with open("output.txt", "rt") as fh:
            content = fh.read()
            print("Text successfully written into the file: ")
    additional_text = input("Enter your additional text that you would like to append into the output.txt file: ")
    with open("output.txt", "at") as fh1:
        fh1.write(additional_text)
        print("Text successfully appended into the file: ")
    with open("output.txt", "rt") as fh1:
            content = fh1.read()
            print(f"Final content of the output.txt: " )
            print(content)

except Exception:
    print(f"Error occuredr")


