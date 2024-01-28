class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2

# Example usage:
calculator = Calculator()

# Addition
result_addition = calculator.add(10, 5)
print("Addition:", result_addition)  # Output: 15

# Subtraction
result_subtraction = calculator.subtract(10, 5)
print("Subtraction:", result_subtraction)  # Output: 5

# Division
result_division = calculator.divide(10, 5)
print("Division:", result_division)  # Output: 2.0

# Multiplication
result_multiplication = calculator.multiply(10, 5)
print("Multiplication:", result_multiplication)  # Output: 50
