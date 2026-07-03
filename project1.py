# print("😎Welcome To Number Guessing Game😎")
# print(" ")

# number1 = 60
# print("Note :- You Have Only 3️⃣    Attempts To Guess The Number Between 1 to 100")
# print(" ")
# for i in range(3):
#     user = int(input(" ATTEMTS :- "))
#     if user==number1  :
#         print("congratulations🎉🎉🎉, you guessed correct")
#         break
#     elif user>number1:
#         print("You selected Very High Number📈, Try Again ")
        
#     else:
#         print("You selected Very Low Number📉, Try Again ")
        
# else:
#     print("You Have Exceeded Your Attempts, Game Over !")
    
    

# num = 60
# A = 0
# while A < 3 :
#     user = input("enter lunky number :- ")
#     A+=1
    
#     if user.isdigit():
#         user = int(user)
#     else:
#         print("enter valid  number ")
#         continue
        
#     if user == num :
#         print("congrulation ")
#         break
#     elif user > num :
#         print("user number is too high ")
#     else :
#         print("user number is too low")
# else :
#     print("Game is over ")
# student_name1 = {}

# def student_mark(student_name1):
#     name = input("Enter Student Name :- ")
#     mark = float(input("enter student mark :-"))
#     student_name1[name]=mark
#     print(student_name1)
# student_mark(student_name1)
        
# print("hello Sir 👋")
# print(" ")
# print("Welcome to  office")
# name = input("enter your name :- ")

# def office():
#     if name == "Dev Thakkar":
#         print("Welcome  Sir 👋")
#     else:
#         print("Your Are Not In Stuff ")
        
# office()
# print(" ")
# print(" office Timing")
# panching = int(input("enter panching  timing "))

# def time():
#     if panching >= 9:
#         print("Good Morning Sir 😊")
#     elif panching>=12:
#         print("Good Afternoom 😎")
#     elif panching >= 18:
#         print("Good Evening 🙂")
#     elif panching>= 20:
#         print("Good Night")
#     else:
#         print("enter indian timing ")
        
# time()
# print(" ")
# print(" Stuff List ")
# def list1():
#     mylist = ["bhavya","dev","indrajit"]
    
#     for i in mylist:
#         print(i)
# list1()

# num  = int(input("enter your number :- "))
# print(num)    


# student = {
#     "dev":65,
#     "harshil":98,
#     "bhavy": 78,
#     "indrajeet":85,
    
# }

# update_mark = student.update({"dev": 70})
# update_mark = student.update({"harshil": 70})
# update_mark = student.update({"bhavy": 70})
# update_mark = student.update({"indrajeet": 70})
# print(student)


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
    user = input("enter number to remove(-) in list ")
    
    if user.isdigit():
        user = int(user)
        mylist.remove(user)
        print("remove number is successfull")
    else:
        print("number is not found  ")
    print(mylist)
   
while True:
    print("option 1. for add number in list ")
    print("option 2. for remove number in list ")
    print("option 3. Exit....")
    
    if user := input("enter your option :- "):
        if user == "1":
            add_function(mylist)
        elif user == "2":
            remove_function(mylist)
        elif user == "3":
            print("Exit....")
            break
        else:
            print("Invalid Input ")