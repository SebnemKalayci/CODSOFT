FirstNumber = int(input("Enter the first number, please. "))
SecondNumber = int(input("Enter the second number, please. "))
operation = input("""Select operation.
(Addition: +, Substraction: -, Multiplication: x, Division: /)
""")

if operation == "+":
    print("Result: " +str(FirstNumber+SecondNumber))

elif operation == "-":
    print("Result: " + str(FirstNumber-SecondNumber))

elif operation == "x":
    print("Result: " + str(FirstNumber*SecondNumber))

elif operation == "/":
    if SecondNumber == 0:
        print("Cannot divide by zero")
    else:
        print("Result: " + str(FirstNumber/SecondNumber))