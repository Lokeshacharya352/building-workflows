import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Square root of negative number not allowed")
    return math.sqrt(a)

def calculator():
    print("=== Python Calculator ===")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")

    while True:
        try:
            choice = int(input("\nEnter choice (0-6): "))

            if choice == 0:
                print("Goodbye 👋")
                break

            if choice == 6:  # square root (only one input)
                a = float(input("Enter number: "))
                print("Result:", sqrt(a))
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    print("Result:", add(a, b))
                elif choice == 2:
                    print("Result:", subtract(a, b))
                elif choice == 3:
                    print("Result:", multiply(a, b))
                elif choice == 4:
                    print("Result:", divide(a, b))
                elif choice == 5:
                    print("Result:", power(a, b))
                else:
                    print("❌ Invalid choice. Try again.")
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    calculator()
