# welcome message 
from turtle import clearscreen


print("Welcome to the secret auction program ")

#empty dic
my_auction ={}
bidding_finished =False



def fin_best(bidding_amount):
    best_amount =0
    for bidder in bidding_amount:
        new_amount=bidding_amount[bidder]
        if best_amount < new_amount:
            best_amount== new_amount
            Winner = bidder
    print(f"The winner is {Winner} with a bid of $ {new_amount}")

#bidding info 

while not bidding_finished:
    user_name= str(input("What's your Name: "))
    user_bid= int(input("What's your bid amount $: "))
    my_auction[user_name] =user_bid
    user_ask = str(input("Are there any additional bidders: Y / N  -"))
    if user_ask =='N':
        bidding_finished=True
        fin_best(my_auction)
    elif user_ask =='Y':
        clearscreen()




