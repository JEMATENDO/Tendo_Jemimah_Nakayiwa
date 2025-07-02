inputt=int(input("Enter a number to calculate its factorial: "))

def factorial(input):
    if input < 0:
        return "Factorial is not defined for negative numbers."
    elif input == 0 or input == 1:
        return 1
    else:
        fact=input*factorial(input-1)
        return fact
    
print(factorial(inputt))    