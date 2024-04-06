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

WATER=300
MILK=200
COFFEE=100
MONEY= 0

#def check_resources():
    
def user_transaction():
    print("Step #1")

def usage_report():
    print(WATER,MILK, COFFEE)

coffee_continue = True

while coffee_continue:
    
    u_choice = int(input(("What would you like? press your choice : 1. Espresso/ 2. Latte/ 3. Cappuccino")))

    if u_choice == 1 and WATER >= 50 and COFFEE >=18:
        user_transaction()
        WATER -=50
        COFFEE -=18
        usage_report()
    else:
        print("Insufficient resources")
        usage_report()
        coffee_continue == False
