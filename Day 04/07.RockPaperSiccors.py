# ROCK PAPER and SCISSOR
import random

# Logic Implementation 

print("Welcome to the ROCK PAPER SCISSOR Game!! \n")
user_choice =int(input ("Please Enter your choice for ROCK [0], PAPER [1], SCISSOR [2] : "))
if user_choice < 0 or user_choice>2:
    print("You enter a Wrong Choice!! Try Again")
else:
    machine_choice = int(random.randint(0,2))
    if (user_choice ==0) and (machine_choice== 2):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Won!!")
    elif (user_choice ==2) and (machine_choice==1 ):
            print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Won!!")
    elif (user_choice ==1) and (machine_choice== 0):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Won!!")
    elif (user_choice ==2) and (machine_choice== 0):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Lost!!")
    elif (user_choice ==1) and (machine_choice== 2):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Lost!!")
    elif (user_choice ==0) and (machine_choice== 1):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - You Lost!!")
    elif (user_choice ==2) and (machine_choice== 2):
        print(f"Your choice {user_choice} and Computer choice {machine_choice} - It's a Draw!!")
