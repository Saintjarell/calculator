def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


print("Choose the following:")
print("1. addition")
print("2. subtract")
print("3. divide")
print("4. multiply")

while True:
    choice = input("choose your choice (1,2,3,4):")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = (input("Your first number:"))
            num2 = (input("Your second number:"))
        except ValueError:
            print("Please insert a correct number.")
            continue
    if choice == "1":
        num1 = float(num1)
        num2 = float(num2)

        sum = num1 + num2

        print("The sum of", num1, "+", num2, "=", sum)

    elif choice == "2":
        num1 = float(num1)
        num2 = float(num2)

        print("{}" - "{}".format(num1, num2))
        print(num1 - num2)


    elif choice == "3":
        num1 = float(num1)
        num2 = float(num2)

        print("{}" / "{}".format(num1, num2))
        print(num1 / num2)


    elif choice == "4":
        num1 = float(num1)
        num2 = float(num2)

        print("{}" * "{}".format(num1, num2))
        print(num1 * num2)

    continuation_of_calculation = input("continue with calculation? (y/n?:)")

    if continuation_of_calculation == ("n"):
        break

    else:
        "y"
        continue
