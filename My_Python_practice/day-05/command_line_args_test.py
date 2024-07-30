import sys

# Reading command-line arguments

num1 = float(sys.argv[1])
num2 = float(sys.argv[3])


# Function definitions

def add(num1, num2):
    output = num1 + num2
    return output

def sub(num1, num2):
    output = num1 -num2
    return output

def mul(num1, num2):
    output = num1*num2
    return output

# Operation selection from command line

operation = sys.argv[2]


# Perform operation based on input

if operation == "add":
    result = add(num1, num2)
elif operation == "sub":
    result = sub(num1, num2)
elif operation == "mul":
    result = mul(num1, num2)
else:
    print("unsuported operation")
    sys.exit(1)  # Exit with error status if operation is unsupported


# Print the result

print(result)


