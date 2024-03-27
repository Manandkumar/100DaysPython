#welcome Message 
print("Welcome to the Treasure Island. \n Your mission is to find the treasure")
#take the name
name =str(input("Enter your name: "))
#logic

choice1 = str(input("You want to go Left or Right - L / R: "))
if(choice1 =='R'):
    print(f"Sorry!! {name}. Your Game is over.")
else:
    choice2 = str(input("You want to Swim or Wait - S / W: "))
    if(choice2=='S'):
        print(f"Sorry!! {name}. Your Game is over.")
    else:
        choice3 = str(input("Which door you like to open - Red , Yellow or Blue - R / Y / B: "))
        if choice3 == 'B' or choice3 =='R':
            print(f"Sorry!! {name}. Your Game is over.")
        else:
            print(f"{name} !! You found the treasure!! You Won!!!")