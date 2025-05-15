def evaluate_expression(expression):
    try:
        # Evaluate the expression using eval
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("\nAdvanced CLI Calculator")
        print("Enter an arithmetic expression to evaluate or type 'quit' to exit:")

        expression = input("Expression: ")

        if expression.lower() == 'quit':
            print("Exiting the calculator. Goodbye!")
            break

        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
