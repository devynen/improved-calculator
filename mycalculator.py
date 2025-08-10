
# Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")


if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")

elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")

elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")

elif operation == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please enter +, -, * or /")
