import json
import math


HISTORY_FILE = "history.json"


def initialize_history_file():
    try:
        with open(HISTORY_FILE, "r") as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)


def load_history():
    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def calculate():
    history = load_history()
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. View History")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice == "6":
            print("\nCalculation History:")
            for entry in history:
                print(entry)
            continue

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid input. Try again.")
            continue

        if choice == "5":  
            try:
                num = float(input("Enter a number: "))
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                    continue
                result = math.sqrt(num)
                operation = "Square Root"
                entry = {"operation": operation, "num": num, "result": result}
                history.append(entry)
                save_history(history)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            result = num1 + num2
            operation = "Addition"
        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"
        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            operation = "Division"

        
        entry = {"operation": operation, "num1": num1, "num2": num2, "result": result}
        history.append(entry)
        save_history(history)

        print(f"Result: {result}")


if __name__ == "__main__":
    initialize_history_file()
    calculate()
