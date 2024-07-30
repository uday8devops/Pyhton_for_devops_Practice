numbers = input("Enter any 2 numbers for division:").split("/")


if len(numbers) !=2:
    print("Enter exactly 2 numbers only separted by space.")
else:
    try:    
        num1 = float(numbers[0])
        num2 = float(numbers[1])

        if num2 == 0:
            print("Error: cannot be divided by Zero(0)")
        else:
            division = num1/num2
            print(f"The Division of {num1}/{num2} is:", division)
    except ValueError:
        print("Please Enter numbers only")


