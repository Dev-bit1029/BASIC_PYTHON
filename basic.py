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