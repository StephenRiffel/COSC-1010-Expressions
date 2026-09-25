def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = int(input("Choose an operation (1-4): "))

if choice == 1:
    result = add(num1, num2)
    print("The result of addition is", result)

elif choice == 2:
    result = subtract(num1, num2)
    print("The result of subtraction is", result)

elif choice == 3:
    result = multiply(num1, num2)
    print("The result of multiplication is", result)

elif choice == 4:
    result = divide(num1, num2)
    print("The result of division is", result)

else:
    print("Invalid choice.")

