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