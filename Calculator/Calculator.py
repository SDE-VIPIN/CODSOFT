def add(x,y):
    result = x + y
    return result

def sub(x,y):
    result = x - y
    return result

def mul(x,y):
    result = x*y
    return result

def div(x,y):
    if (y != 0):
        return x/y
    else:
        return "infinite"
       

def calculator():

    while True:
        print("Select Operations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice : ")

        if choice in ('1','2','3','4'):

                num1 = eval(input("Enter the first number : "))
                num2 = eval(input("Enter the second number : "))

                if choice == '1':
                    print(f"Addition of {num1} and {num2} is : ", add(num1,num2))

                elif choice == '2':
                    print(f"Subtraction of {num1} and {num2} is : ", sub(num1,num2))

                elif choice == '3':
                    print(f"Multiplication of {num1} and {num2} is : ", mul(num1,num2))

                elif choice == '4':
                    print(f"Division of {num1} and {num2} is : ", div(num1,num2))

                else:
                    print("Invalid input")
                    
        user_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if user_choice != 'yes':
            break
        else:
            calculator()

calculator()