#define function
import random

it_is_match= False

def compare(u_number,c_number):
    if u_number <c_number:
        print(" Too low \n Guess again")
    elif u_number >c_number:
        print ("Too High \n Guess again")
    elif u_number==c_number:
        print(f"Correct!!, you guessed the number, and it's {u_number}")
        

# take user choice 

computer_number = random.randint(1,100)
u_choice = int(input("Enter your choice: \n 1 for Hard level \n 2 for Easy level \n -----> "))
it_is_match=False

if u_choice==1:
    attempts= 5
elif u_choice ==2:
    attempts =10

for i in range (1,attempts+1):
    if i< attempts:
        user_number=int(input(f" You are trying {i} attempt(s) of {attempts}, Enter your next guess:"))
        compare(user_number, computer_number)
    elif i== attempts:
        user_number=int(input(f" You are trying the last {i} attempt(s) of {attempts}, Enter your next guess:"))
        compare(user_number, computer_number)
        if it_is_match == False:
            print("Sorry! you failed in guessing the number")



