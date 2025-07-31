print("simple calculator")

print("1. Addition")
print("2. Substaction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("Enter Operation number (1-5): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Try again.")
        break  # Skip rest of loop and ask again

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the seconf number: "))

    if choice == '1':
        result = num1 + num2
        print(result)

    elif choice == '2':
        result = num1 - num2
        print(result)

    elif choice == '3':
        result = num1 * num2
        print(result)

    elif choice == '4':
        result = num1/num2
        print(result)
    else:
        print("Invalid operator")
    

