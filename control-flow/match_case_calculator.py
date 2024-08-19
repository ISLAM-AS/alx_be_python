## match_case_calculator.py

# Prompt for user input:0
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case:
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation."

# Perform the calculation and get the result:
result = calculate(num1, num2, operation)

# Output the result:
print(f"The result is {result}" if isinstance(result, (int, float)) else result)