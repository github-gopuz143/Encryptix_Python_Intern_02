# Python Simple Calculator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

# Perform calculation
result = calculator(num1, num2, operator)

# Print the result
print("Result: ", result)
