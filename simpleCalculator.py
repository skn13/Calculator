def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Zero division error. Please enter a valid number.")
        return 0


print("Please select what function to use.")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")


def calculate():
    option = input("please enter your option here: ")
    num1 = input("Enter first number here: ")
    num2 = input("Enter second number here: ")

    if option == "1":
        print(addition(int(num1), int(num2)))
    elif option == "2":
        print(subtraction(int(num1), int(num2)))
    elif option == "3":
        print(multiplication(int(num1), int(num2)))
    elif option == "4":
        print(division(int(num1), int(num2)))
    else:
        print("Input error")

calculate()