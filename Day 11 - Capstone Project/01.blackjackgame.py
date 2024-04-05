#creating a list 
import random
import os

#step 3
def deal_card():
    """Returns a Random Card from Deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
#step 6 to caluculate score 

def caluculate_score(cards):
    if sum(cards) ==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return"Draw"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack"
    elif user_score == 0:
        return "Win withat a Blackjack"
    elif user_score >21:
        return "You went over. You Lose :( "
    elif computer_score >21:
        return "Opponent went over. You Win :)"
    elif user_score > computer_score:
         return "You Win :) "
    else :
         return "You lose "
#step 4: deal 2 cards for computer and user 

def play_game(): 
    user_cards =[]
    computer_cards =[]

    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=caluculate_score(user_cards)
        computer_score=caluculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards}, Computer score: {computer_score}")

        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal=str.lower(input("Type 'Y' to get another cards, type 'N' to Pass: "))
            if user_should_deal =="y":
                user_cards.append(deal_card())
            else:
                is_game_over= True

    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=caluculate_score(computer_cards)

    print (f"Your final hand: {user_cards}, final score: {user_score}")
    print (f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while str.lower(input("Do you want to play a game of Blackjack:? Type 'Y' or else 'N':")) == "y":
    os.system('cls')
    play_game()
#print("Select the Deifficulty level 1 / 2/ 3 :")