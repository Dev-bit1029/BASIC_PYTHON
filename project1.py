print("😎Welcome To Number Guessing Game😎")
print(" ")

number1 = 60
print("Note :- You Have Only 3️⃣    Attempts To Guess The Number Between 1 to 100")
print(" ")
for i in range(3):
    user = int(input(" ATTEMTS :- "))
    if user==number1  :
        print("congratulations🎉🎉🎉, you guessed correct")
        break
    elif user>number1:
        print("You selected Very High Number📈, Try Again ")
        
    else:
        print("You selected Very Low Number📉, Try Again ")
        
else:
    print("You Have Exceeded Your Attempts, Game Over !")
    
    

num = 60
A = 0
while A < 3 :
    user = input("enter lunky number :- ")
    A+=1
    
    if user.isdigit():
        user = int(user)
    else:
        print("enter valid  number ")
        continue
        
    if user == num :
        print("congrulation ")
        break
    elif user > num :
        print("user number is too high ")
    else :
        print("user number is too low")
else :
    print("Game is over ")
student_name1 = {}

def student_mark(student_name1):
    name = input("Enter Student Name :- ")
    mark = float(input("enter student mark :-"))
    student_name1[name]=mark
    print(student_name1)
student_mark(student_name1)
        
print("hello Sir 👋")
print(" ")
print("Welcome to  office")
name = input("enter your name :- ")

def office():
    if name == "Dev Thakkar":
        print("Welcome  Sir 👋")
    else:
        print("Your Are Not In Stuff ")
        
office()
print(" ")
print(" office Timing")
panching = int(input("enter panching  timing "))

def time():
    if panching >= 9:
        print("Good Morning Sir 😊")
    elif panching>=12:
        print("Good Afternoom 😎")
    elif panching >= 18:
        print("Good Evening 🙂")
    elif panching>= 20:
        print("Good Night")
    else:
        print("enter indian timing ")
        
time()
print(" ")
print(" Stuff List ")
def list1():
    mylist = ["bhavya","dev","indrajit"]
    
    for i in mylist:
        print(i)
list1()

num  = int(input("enter your number :- "))
print(num)    


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


mylist = [1,2,3,4,5,6,7,8,9]

def add_function(mylist):
    user = input("enter number to  add(+) in list :-  ")
    if user.isdigit():
        user = int(user)
        mylist.append(user)
        print(mylist)
    else:
        print("Invalid Input ")
        
def remove_function(mylist):
    user = input("enter number to remove(-) in list :-  ")
    if user.isdigit():
        user = int(user)
        if user in mylist:
            mylist.remove(user)
            print("successfully removed from list ")
            print(mylist)
        else:
            print("Number not found in list")
            
    else:
        print("Invalid Input ")
        
def display_list(mylist):
    print("Current List: ", mylist)

def update_list(mylist):
    user = input("enter number to update in list :-  ")
    if user.isdigit():
        user = int(user)
        if user in mylist:
            new_value = input("enter new value to update :- ")
            if new_value.isdigit():
                new_value = int(new_value)
                index = mylist.index(user)
                mylist[index] = new_value
                print("successfully updated in list ")
                print(mylist)
            else:
                print("Invalid Input for new value")
        else:
            print("Number not found in list")
    else:
        print("Invalid Input ")        

        
while True:
    print("option 1. for add number in list ")
    print("option 2. for remove number in list ")
    print("option 3. for update number in list ")
    print("option 4. Exit....")
    
    if user := input("enter your option :- "):
        if user == "1":
            add_function(mylist)
        elif user == "2":
            remove_function(mylist)
        elif user == "3":
            update_list(mylist)
        elif user == "4":
            print("Exit....")
            break
        else:
            print("Invalid Input ")
            

print("Thank You For Using This Program 😊")

print("=====NUMBER OPERTION PROGRAM=====")

user = input("Enter Your Number :- ")



def even_num(user):
    if user.isdigit():
        user = int(user)
        if user <=0:
            print("invalid input")
        for x in range(user):
            if x%2==0:
                print(x)
            else:
                print("selected valid option ")
        
    else:
        print("invalid input ")
      

def odd_num(user):
    if user.isdigit():
        user = int(user)
        
        for d in range(user):
            if d%2!=0:
                print(d)
            elif x==0:
                print("the number is zero")
            else:
                print("selected valid option  ")
    else:
        print("invalid input ")
        
def mul_num(user):
    if user.isdigit():
        user = int(user)
        
        for v in range(1,11):
            print(f" {v} * {user} = {v*user}")
    else:
        print("ivalid input")

    
print("option 1. for even number ")
print("option 2. for odd number ")
print("option 3. for multiplication table ")
print("option 4. for all function ")
print("option 5. Exit....")

while True:
    choice = input("Enter Your Choice :- ")
    if choice == "1":
        even_num(user)
    elif choice == "2":
        odd_num(user)
    elif choice == "3":
        mul_num(user)
    elif choice == "4":
        print("Running all functions...")
        even_num(user)
        odd_num(user)
        mul_num(user)
    elif choice == "5":
        print("Exit....")
        break
    else:
        print("Invalid Input ")
        
print("Thank You For Using This Program 😊")

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


print("=====Welcome To The Bank Of Student=====")

bos = {
    "dev":50000,
    "bhavya":100000,
    "indrajeet":150000,
    "harshil":200000,
}

def deposit(bos):
    name = input("Enter account holder name: ")
    if name in bos:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            bos[name] += amount
            print(f"Deposit successful! New balance for {name}: {bos[name]}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    else:
        print("Account not found.")
deposit(bos)

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


