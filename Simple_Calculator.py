# Simple Calculator in Python
print("Welcome to the Simple Calculator!")
# Get numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Get operation
print("Choose an operation: +, -, *, /")
operation = input("Enter operation: ")
# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero!"
else:
    result = "Invalid Operation."
# Show result
print("Result:", result)