
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y



while True:

    print("Select operation.")

    choice = input("Enter choice(+/-/*//): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input")

    repeat = input("Do you want to perform another operation? (y/n)")
    if repeat != 'y':
        break
