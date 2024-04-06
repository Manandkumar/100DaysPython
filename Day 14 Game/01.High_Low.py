
from game_data import data
import random

def format_data(account):
    """Format the account data from file to printable format """
    account_name = account["name"]
    account_desc = account["description"]
    account_country=account["country"]
    return (f"{account_name},a {account_desc}, from {account_country} ")
def check_user_guess(guess,a_guess,b_guess):
    if a_guess>b_guess:
        return guess =="a"
    else:
        return guess =='b'

score =0
game_continue = True
account_b=random.choice(data)
#Generate a radom account from game data 

while game_continue:

    account_a= account_b
    account_b= random.choice(data)
    while account_a == account_b:
        account_b=random.choice(data)
    #format the account data into printable format

    print("Compare A: ",format_data(account_a),".")
    print("Compare B: ",format_data(account_b),".")

    #ask the user for guess
    #check if the user is correct
    u_guess=str.lower((input("Who has more follower, Enter your guess A / B: ")))
    a_follower_count = account_a["count"]
    b_follower_count = account_b["count"]

    is_correct = check_user_guess(u_guess,a_follower_count,b_follower_count)
    #score keeping 
    if is_correct :
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry! that's wrong! Current score: {score}.")
        game_continue=False

# Make the game repeatable
#making account at position B become the next accout at position A

#clear screen