"""A simple command-line calculator."""


def calculate(first: float, operator: str, second: float) -> float:
    """Perform an arithmetic operation on two numbers."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main() -> None:
    print("Simple Calculator")
    print("Enter q at any prompt to quit.")

    while True:
        first_input = input("\nFirst number: ").strip()
        if first_input.lower() == "q":
            break

        operator = input("Operation (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break

        second_input = input("Second number: ").strip()
        if second_input.lower() == "q":
            break

        try:
            result = calculate(float(first_input), operator, float(second_input))
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result:g}")

    print("Goodbye!")


if __name__ == "__main__":
    main()
