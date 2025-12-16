# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.
 
# Expected Output:
# For example, if the function is called with 5, it should return:

nums = int(input("Enter a number to calculate its factorial: "))
def factorial(nums):
    if nums == 1:
        return 1
    else:
        result = nums * factorial(nums - 1)
        return result
print("The factorial of", nums, "is", factorial(nums))

