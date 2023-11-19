def add_numbers():
    numbers = []

    # Get the number of values to add
    num_count = int(input("Enter the number of values to add: "))

    # Get input from the user
    for i in range(num_count):
        value_str = input(f"Enter value {i + 1}: ")
        
        # Check if the input value is a float or an integer
        try:
            value = float(value_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        numbers.append(value)

    # Perform addition
    sum_result = sum(numbers)

    # Check if the result has a fractional part
    if sum_result.is_integer():
        sum_result = int(sum_result)

    # Display the result
    print(f"The sum of the numbers is: {sum_result}")

if __name__ == "__main__":
    add_numbers()

