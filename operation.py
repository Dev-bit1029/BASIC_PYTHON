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
            elif d==0:
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