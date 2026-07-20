print("======Welcome TO The Bank OF Student========")

bos = {
    "dev":100000,
    "bhavya":50000,
    "indrajeet":150000,
    "satyam":200000,
    
}

def deposit(bos):
    name = input("Enter Your Name :- ")
    if name.isalpha():
        name = str(name)
        if name in bos:
            amount = input("Enter Amount To Deposit :- ")
            if amount.isdigit():
                amount = int(amount)
                bos[name] += amount
                print(f"Amount Deposited Successfully. New Balance: {bos[name]}")
            else:
                print("Invalid input. Amount should be a number.")
        else:
            print("Account holder name  not found.")
            print("Please To Create Account :- ",name)
    else:
        print("Invalid input. Name should contain only letters.")


def withdraw(bos):
    name = input("Enter Your Name :- ")
    if name.isalpha():
        name = str(name)
        if name in bos:
            amount = input("Enter Amount To Withdraw :- ")
            if amount.isdigit():
                amount = int(amount)
                if bos[name] >= amount:
                    bos[name] -= amount
                    print(f"Amount Withdrawn Successfully. New Balance: {bos[name]}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid input. Amount should be a number.")
        else:
            print("Account holder name not found.")
    else:
        print("Invalid input. Name should contain only letters.")
        
def check_balance(bos):
    name = input("Enter Your Name :- ")
    if name.isalpha():
        name = str(name)
        if name in bos:
            print(f"Your Current Balance: {bos[name]}")
        else:
            print("Account holder name not found.")
    else:
        print("Invalid input. Name should contain only letters.")
        
def create_account(bos):
    name = input("Enter Your Name :- ")
    if name.isalpha():
        name = str(name)
        if name not in bos:
            initial_deposit = input("Enter Initial Deposit Amount :- ")
            if initial_deposit.isdigit():
                initial_deposit = int(initial_deposit)
                bos[name] = initial_deposit
                print(f"Account Created Successfully. Current Balance: {bos[name]}")
            else:
                print("Invalid input. Amount should be a number.")
        else:
            print("Account holder name already exists.")
    else:
        print("Invalid input. Name should contain only letters.")
        
while True:
    print("\nOPTION 1. Deposit Money")
    print("OPTION 2. Withdraw Money")
    print("OPTION 3. Check Balance")
    print("OPTION 4. Create Account")
    print("OPTION 5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        deposit(bos)
    elif choice == "2":
        withdraw(bos)
    elif choice == "3":
        check_balance(bos)
    elif choice == "4":
        create_account(bos)
    elif choice == "5":
        print("Exiting..., THANK YOU!")
        break
    else:
        print("Invalid choice. Please try again.")
        
print("Thank you for using the Bank of Student. Have a great day!")
