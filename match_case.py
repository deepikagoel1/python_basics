
x = input("Enter the operand according which you want to perform the mathematical operation!!!! \t")

# x is the variable to match
match x:
    # if x is 0
    case '+':
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        print("Addition of two numbers is:", (a + b))

    case '-':
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        if(a < b):
            print("Subtraction of two numbers is:", (b - a))
        else:
            print("Subtraction of two numbers is:", (a - b))

    case '*':
        a = int(input("Enter first number \t"))
        b = int(input("Enter second number \t"))
        print("Multiplication of two numbers is:", (a * b))

    case '/':
        a = int(input("Enter the numerator \t"))
        b = int(input("Enter the denominator \t"))
        print("Division of two numbers is:", (a / b))

    case '%':
        a = int(input("Enter the numerator \t"))
        b = int(input("Enter the denominator \t"))
        print("Remainder of two numbers is:", (a % b))

    # case '**':
    #     a = int(input("Enter the number whose power you want to find out \t"))
    #     b = int(input("Enter the degree of the number \t"))
    #     print("Remainder of two numbers is:", (a ** b))

    # case '//':
    #     a = int(input("Enter the numerator \t"))
    #     b = int(input("Enter the denominator \t"))
    #     print("Division of two numbers is:", (a // b))
       
    # # case with if-condition
    # case 4 if x % 2 == 0:
    #     print("x % 2 == 0 and case is 4")
    # # Empty case with if-condition
    # case _ if x < 10:
    #     print("x is < 10")
    # # default case(will only be matched if the above cases were not matched)
    # # so it is basically just an else:
    # case _:
    #     print(x)