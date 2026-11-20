"""A simple command-line calculator for our Git branching activity."""


def add(a, b):
    """Add two numbers."""
    raise NotImplementedError("Addition is not implemented yet.")






def subtract(a, b):
    """Subtract the second number from the first."""
    raise NotImplementedError("Subtraction is not implemented yet.")






def multiply(a, b):
    """Multiply two numbers."""
    raise NotImplementedError("Multiplication is not implemented yet.")






def divide(a, b):
    """Divide the first number by the second."""
    raise NotImplementedError("Division is not implemented yet.")






def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    while True:
        print("\n=== Simple Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Thanks for using the calculator!")
            break
        if choice not in operations:
            print("Invalid option. Please choose 1 to 5.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        operation_name, operation = operations[choice]
        try:
            answer = operation(first, second)
            print(f"{operation_name} result: {answer:g}")
        except ZeroDivisionError:
            print("You cannot divide by zero.")


if __name__ == "__main__":
    main()
