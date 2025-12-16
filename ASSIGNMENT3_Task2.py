# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
#  Expected Output:
#  For example, if the user enters 25, the output should be:

import math

input_number = float(input("Enter a number: "))
square_root = math.sqrt(input_number)
natural_log = math.log(input_number)
sine_value = math.sin(input_number)
print("Square root of", input_number, "is:", square_root)
print("Natural logarithm (log base e) of", input_number, "is:", natural_log)
print("Sine of", input_number, "is:", sine_value)   
