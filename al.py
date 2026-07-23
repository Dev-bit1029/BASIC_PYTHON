def even_number(num):
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def odd_number(num):
    if num % 2 != 0:
        print("The number is odd.")
    else:
        print("The number is even.")

def factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f"The factorial of {num} is {fact}.")

def table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

while True:
    print("OPTION 1. Check if the number is even")
    print("OPTION 2. Check if the number is odd")
    print("OPTION 3. Display the multiplication table of the number")
    print("OPTION 4. Calculate the factorial of the number")
    print("OPTION 5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user = input("Enter any number:- ")
        if user.isdigit():
            user = int(user)
            even_number(user)
        else:
            print("Invalid input")
    elif choice == "2":
        user = input("Enter any number:- ")
        if user.isdigit():
            user = int(user)
            odd_number(user)
        else:
            print("Invalid input")
    elif choice == "3":
        user = input("Enter any number:- ")
        if user.isdigit():
            user = int(user)
            table(user)
        else:
            print("Invalid input")
    elif choice == "4":
        user = input("Enter any number:- ")
        if user.isdigit():
            user = int(user)
            factorial(user)
        else:
            print("Invalid input")
    elif choice == "5":
        print("Exiting..., THANK YOU!")
        break
    else:
        print("Invalid choice. Please try again.")
        
        

    