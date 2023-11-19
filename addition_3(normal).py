# Get input from the user
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Attempt to convert input to float
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    # If conversion to float fails, use integers
    num1 = int(num1_str)
    num2 = int(num2_str)

# Perform addition
sum_result = num1 + num2

# Check if the result has a fractional part
if sum_result.is_integer():
    sum_result = int(sum_result)

# Display the result
print(f"The sum of {num1} and {num2} is: {sum_result}")

