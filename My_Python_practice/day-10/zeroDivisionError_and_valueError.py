import sys

numbers = input("Enter any 2 numbers for division separeated by space:").split()

# Learning "try" and "except" methods

try:
    num1 = float(numbers[0])
    num2 = float(numbers[1])
except ValueError:
        print("Please enter numbers only....")
        sys.exit(2) # exits the program for Entering string values instead of numbers

try:
        division = num1/num2
except ZeroDivisionError:
        print("Error: cannot be divided by zero(0)")
        sys.exit(1) # exits the program here is num2 = 0

print(division)
        
