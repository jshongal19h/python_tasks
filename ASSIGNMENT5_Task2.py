# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

original_list = list(range(1,11))
print(original_list)
extracted_list = original_list[0:6]
print(f"Extracted  first five elements from the list {original_list} are {extracted_list}")
reversed_list = extracted_list[::-1]
print(f"Reverse of extracted elements {extracted_list} is {reversed_list}")
print(f"Both extracted list  {extracted_list} and reversed list will be {reversed_list}")