#Carys Lewelling
#Simple Calculator

#Initial
#Functions
def add(num1, num2):#add num1 w num2 and print the results
    result = str(int(num1) + int(num2))
    print("The result is " + result)
def sub(num1, num2):#subtract num1 w num2 and print the results
    result = str(int(num1) - int(num2))
    print("The result is " + result)
def mul(num1, num2):#multiply num1 w num2 and print the results
    result = str(int(num1) * int(num2))
    print("The result is " + result)
def div(num1, num2):#divide num1 w num2 and print the results
    result = str(int(num1) / int(num2))
    print("The result is " + result)
def simple_calculator():
    print("Welcome to Simple Calculator")
    while True:
        print("Select an operation: ")
        print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit""")
        option = int(input("Select option (1-5): "))
        if option == 1:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            add(int1, int2)
        if option == 2:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            sub(int1, int2)
        if option == 3:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            mul(int1, int2)
        if option == 4:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            div(int1, int2)
        if option == 5:
            print("ok bye")
            break
#Main
simple_calculator()
