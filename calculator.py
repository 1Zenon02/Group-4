calculations = []  # List to store all calculations

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show summary of all calculations")
    print("6. Exit")

    try:
        choice = input("Enter the number corresponding to the operation (1/2/3/4/5/6): ")
        choice = int(choice)  # Convert input to an integer to check its validity
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the operation.")
        continue  # Go back to the start of the loop

    if choice == 6:
        print("Exiting the calculator. Goodbye!")
        break

    if choice == 5:
        if calculations:
            print("\nSummary of all calculations:")
            for calc in calculations:
                print(calc)
        else:
            print("No calculations have been performed yet.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:a
        print("Invalid input. Please enter numeric values.")
        continue

    # Perform the selected operation
    if choice == 1:
        result = num1 + num2
        calculations.append(f"{num1} + {num2} = {result}")
        print(f"{num1} + {num2} = {result}")  # Only show the current calculation
    elif choice == 2:
        result = num1 - num2
        calculations.append(f"{num1} - {num2} = {result}")
        print(f"{num1} - {num2} = {result}")  # Only show the current calculation
    elif choice == 3:
        result = num1 * num2
        calculations.append(f"{num1} * {num2} = {result}")
        print(f"{num1} * {num2} = {result}")  # Only show the current calculation
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            calculations.append(f"{num1} / {num2} = {result}")
            print(f"{num1} / {num2} = {result}")  # Only show the current calculation
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")