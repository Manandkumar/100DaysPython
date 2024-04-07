# intial coffee machine - water 300 ml, mil 200 ml, coffee 100 g and Money 0
# 3 hot flavours - Espresso[50 ml ater,18g coffee], Latte[200 ml water, 24g coffee, 150 ml milk], Cappucciono [250ml water, 24g coffee, 100 ml milk] 
# nicle 
# coin operate
# automatic cup dispense 
# counting cup seliing

# Print report how mcuh of resources left
# check the resources sufficicnet and say what's insufficent 
# process coins 
# check trascation succesful
# manage resources 
MONEY =0
WATER=300
MILK=200
COFFEE=100


#def check_resources():
    
def user_transaction(choice,amount):
    print(f"Your choice of drink is {choice}, it cost {amount}, and please pay in cash")
    global MONEY
    change_1= int(input("Enter how many 10 Rs: "))
    change_2= int(input("Enter how many 50 Rs: "))
    change_3= int(input("Enter how many 100 Rs: "))
    change_4= int(input("Enter how many 200 Rs: "))
    total = (change_1*10)+(change_2*50)+(change_3*100)+(change_4*200)
    if total <amount:
        print("You gave insufficent Amount")
    elif total > amount:
        change_return= total-amount
        print(f"You have given more than the actual amount, please take your change {change_return} ")
        MONEY = MONEY +amount
    elif total == amount:
        print("Proceed to take your drink in a moment")
        MONEY = MONEY +amount
            
def usage_report():
    print(f"Current Report \n Water: {WATER} \n Milk: {MILK} \n Coffee: {COFFEE}\n Total Amount collected: {MONEY}")

def resources_reset():
    global WATER, MILK, COFFEE
    WATER +=300 
    MILK += 200
    COFFEE += 100
    print(f"Report after Refilling \n Water: {WATER} \n Milk: {MILK} \n Coffee: {COFFEE}\n Total Amount collected: {MONEY}")

def main_function():
    global WATER,COFFEE,MILK,MONEY

    coffee_continue = True
    while coffee_continue==True:
        
        u_choice = int(input(("What would you like? press your choice : 1. Espresso/ 2. Latte/ 3. Cappuccino: ")))

        if u_choice == 1:
            if WATER >= 50:
                if COFFEE >=18:
                    WATER -=50
                    COFFEE -=18
                    amount = 150
                    user_transaction(u_choice,amount)
                else:
                    print("Coffee is insufficent")
            else:
                print("Water is insufficent")

        elif u_choice == 2:
            if WATER >= 200:
                if COFFEE >=24:
                    if MILK >=150:
                        WATER -=200
                        COFFEE -=24
                        MILK -=150
                        amount = 250
                        user_transaction(u_choice,amount)
                    else:
                        print("Milk is insufficent")
                else:
                    print("Coffee is insufficent")
            else:
                print("Water is insufficent")
        elif u_choice == 3:
            if WATER >= 250:
                if COFFEE >=24:
                    if MILK >=100:
                        WATER -=250
                        COFFEE -=24
                        MILK -=100
                        amount = 100
                        user_transaction(u_choice,amount)
                    else:
                        print("Milk is insufficent")
                else:
                    print("Coffee is insufficent")
            else:
                print("Water is insufficent")

        elif u_choice==4:
            usage_report()
            exit()
        elif u_choice==5:
            resources_reset() 
            

main_function()