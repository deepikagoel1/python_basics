print("Welcome to the self created Calculator!")

while True:
    print("""Enter the choice as per the operation you want to perform \n 
    1 for Addition
    2 for Subtraction
    3 for Multiplication
    4 for Division
    5 for Modulus
    6 for Exponential
    7 for Floor Division
    0 for exit
    """)

    n = int(input("Enter the choice as per the operation you want to perform \t"))

    if (n == 1):
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        print("Addition of two numbers is:", (a + b))

    elif (n == 2):
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        if(a < b):
            print("Subtraction of two numbers is:", (b - a))
        else:
            print("Subtraction of two numbers is:", (a - b))

    elif (n == 3):
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        print("Multiplication of two numbers is:", (a * b))

    elif (n == 4):
        a = int(input("Enter the numerator \t"))
        b = int(input("Enter the denominator \t"))
        print("Division of two numbers is:", (a / b))

    elif (n == 5):
        a = int(input("Enter the numerator \t"))
        b = int(input("Enter the denominator \t"))
        print("Remainder of two numbers is:", (a % b))

    elif (n == 6):
        a = int(input("Enter the number whose power you want to find out \t"))
        b = int(input("Enter the degree of the number \t"))
        print("Remainder of two numbers is:", (a ** b))

    elif (n == 7):
        a = int(input("Enter the numerator \t"))
        b = int(input("Enter the denominator \t"))
        print("Division of two numbers is:", (a // b))

    elif (n == 0):
      break