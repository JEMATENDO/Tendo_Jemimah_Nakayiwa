try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid ! Please enter numeric values.")
except ZeroDivisionError:
    print("wrrrrooonnggg! Division by zero is not allowed.")
else:
    print(f"The result of dividing {num1} by {num2} is {result}")