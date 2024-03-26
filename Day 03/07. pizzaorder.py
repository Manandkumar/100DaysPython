# printing welcome message

print("Thank your for choosing the Python Pizza Deliverables")
pizza_size = str(input("What size of Pizza do you want? S / M / L: "))
pizza_pepperoni = str(input("Do you want pepperoni? Y / N :"))
pizza_extracheese = str(input("Do you want Exra cheese? Y / N :"))

pizza_totalcost = 0

if pizza_size == 'L':
    pizza_totalcost = 25
    if pizza_pepperoni == 'Y':
        pizza_totalcost = pizza_totalcost+3
    else:
        pizza_totalcost = pizza_totalcost
    if pizza_extracheese == 'Y':
        pizza_totalcost = pizza_totalcost+1
    else:
        pizza_totalcost = pizza_totalcost
    print(f"The Total cost of your Pizza is: $ {pizza_totalcost}")
elif pizza_size == 'M':
    pizza_totalcost = 20
    if pizza_pepperoni == 'Y':
        pizza_totalcost = pizza_totalcost+3
    else:
        pizza_totalcost = pizza_totalcost
    if pizza_extracheese == 'Y':
        pizza_totalcost = pizza_totalcost+1
    else:
        pizza_totalcost = pizza_totalcost
    print(f"The Total cost of your Pizza is: $ {pizza_totalcost}")
elif pizza_size == 'S':
    pizza_totalcost = 15
    if pizza_pepperoni == 'Y':
        pizza_totalcost = pizza_totalcost+2
    else:
        pizza_totalcost = pizza_totalcost
    if pizza_extracheese == 'Y':
        pizza_totalcost = pizza_totalcost+1
    else:
        pizza_totalcost = pizza_totalcost
    print(f"The Total cost of your Pizza is: $ {pizza_totalcost}")
