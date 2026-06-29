print("😎Welcome To Number Guessing Game😎")

number1 = 60
print("Note :- You Have Only 3️⃣    Attempts To Guess The Number Between 1 to 100")
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
    
    

    