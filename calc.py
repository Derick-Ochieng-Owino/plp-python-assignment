print("Input two numbers and a mathematical  operator: (+, -, *, /)")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter the operator: ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif print("Division by zero is not allowed"):
        pass
else:
    print("Invalid operator")
