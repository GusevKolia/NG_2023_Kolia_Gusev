import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, **, sqrt): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "**":
    result = num1 ** num2
elif operator == "sqrt":
    result = math.sqrt(num1)

print("Result7: ", result)