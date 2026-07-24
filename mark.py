student_name1 = {}

def student_mark(student_name1):
    name = input("Enter Student Name :- ")
    mark = float(input("enter student mark :-"))
    student_name1[name]=mark
    print(student_name1)
student_mark(student_name1)

student = {
    "dev":65,
    "harshil":98,
    "bhavy": 78,
    "indrajeet":85,
    
}

update_mark = student.update({"dev": 70})
update_mark = student.update({"harshil": 70})
update_mark = student.update({"bhavy": 70})
update_mark = student.update({"indrajeet": 70})
print(student)


print("=====dictionary OPERTION PROGRAM=====")

Student = {
    "dev": 65,
    "harshil": 98,
    "bhavy": 78,
    "indrajeet": 85,
}

def Add_student(Student):
    name = input("Enter Student Name :- ")
    mark = input("Enter Student Mark :- ")
    if name.isalpha() and mark.isdigit():
        Student[name]=mark
        print("successful added ")
    else:
        print("try again bro.....")
    print(Student)
   
def display_students(Student):
    if Student == {}:
        print("No students found.")
    else:
        print(Student)

def update_student(Student):
    name = input("Enter Student Name to Update :- ")
    if name.isalpha():
        name = str(name)
        
        if name in Student:
            new_mark = input("Enter New Mark :- ")
            if new_mark.isdigit():
                new_mark = int(new_mark)
                Student[name] = new_mark
                print("Student mark updated successfully.")
                print(Student)
        else:
            print("Invalid input. Mark should be a number.")
    else:
        print("Student not found.")

def remove_student(Student):
    name = input("Enter Student Name to Remove :- ")
    if name.isalpha():
        name = str(name)
        
        if name in Student:
            del Student[name]
            print("Student removed successfully.")
            print(Student)
        else:
            print("Student not found.")
    else:
        print("Invalid input. Name should contain only letters.")

while True:
    print("OPTION 1. Add Student")
    print("OPTION 2. Display Students")
    print("OPTION 3. Update Student Mark")
    print("OPTION 4. Remove Student")
    print("OPTION 5. Exit")
    
    choice = input("Enter Your Choice :- ")
    
    if choice == "1":
        Add_student(Student)
    elif choice == "2":
        display_students(Student)
    elif choice == "3":
        update_student(Student)
    elif choice == "4":
        remove_student(Student)
    elif choice == "5":
        print("Exit....")
        break
    else:
        print("Invalid Input ")

print("=====Thank You For Using This Program 😊=====")


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