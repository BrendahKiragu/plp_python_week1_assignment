def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ ⚠️  Invalid input! Please enter a numeric value.")

def Calculator():
    print("Welcome to Brendah's Calculator!")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("⚠️ ⚠️  Cannot divide by zero.")
    else:
        print("⚠️ ⚠️  Invalid operation selected.")

Calculator()
