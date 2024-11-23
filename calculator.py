def calculator():
    print("Welcome to the LAN'S Calculator!")

    calculations = []  # List to store all calculations

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Show summary of all calculations")
        print("6. Exit")

        choice = input("Enter the number corresponding to the operation (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break

        if choice == '5':
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
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = num1 + num2
            calculations.append(f"{num1} + {num2} = {result}")
            print(f"The result of the Addition {num1} + {num2} is: {result}")
        elif choice == '2':
            result = num1 - num2
            calculations.append(f"{num1} - {num2} = {result}")
            print(f"The result of the Subtraction {num1} - {num2} is: {result}")
        elif choice == '3':
            result = num1 * num2
            calculations.append(f"{num1} * {num2} = {result}")
            print(f"The result of the Multiplication {num1} * {num2} is: {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                calculations.append(f"{num1} / {num2} = {result}")
                print(f"The result of the Division {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid input. Please select a valid operation.")

# Call the calculator function
calculator()

