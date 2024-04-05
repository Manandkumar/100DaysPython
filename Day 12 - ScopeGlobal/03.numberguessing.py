#define function
import random
EASY_LEVEL =10
HARD_LVEL=5
IT_IS_A_MATCH = False


def compare(u_number,c_number):
    if u_number <c_number:
        print(" Too low \n Guess again")
    elif u_number >c_number:
        print ("Too High \n Guess again")
    elif u_number==c_number:
        IT_IS_A_MATCH == True
        print(f"Correct!!, you guessed the number, and it's {u_number}")
        exit()
        

# take user choice 

def try_game():
    computer_number = random.randint(1,100)
    u_choice = int(input("Enter your choice: \n 1 for Hard level \n 2 for Easy level \n -----> "))

    if u_choice==1:
        attempts= HARD_LVEL
    elif u_choice ==2:
        attempts =EASY_LEVEL

    for i in range (1,attempts+1):
        if i< attempts:
            user_number=int(input(f" You are trying {i} attempt(s) of {attempts}, Enter your next guess:"))
            compare(user_number, computer_number)
        elif i== attempts:
            user_number=int(input(f" You are trying the last {i} attempt(s) of {attempts}, Enter your next guess:"))
            compare(user_number, computer_number)
            if IT_IS_A_MATCH == False:
                print("Sorry! you failed in guessing the number")

while str.lower(input("Do you like to continue the game again Y /N : ")) =='y':
    try_game()

