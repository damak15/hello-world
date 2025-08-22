def add_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)

def subtract_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference =", a - b)

def multiply_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product =", a * b)

def divide_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Error: Division by zero!")

def find_square():
    a = int(input("Enter a number: "))
    print("Square =", a * a)


# --------- Menu-driven program ----------
while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square of a number")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_numbers()
    elif choice == '2':
        subtract_numbers()
    elif choice == '3':
        multiply_numbers()
    elif choice == '4':
        divide_numbers()
    elif choice == '5':
        find_square()
    elif choice == '6':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
