# Tip Caluculator 

# Welcome Message 
print("Welcome to the Tip Caluculator")
total_amount= input("What's the total bill amount:")
total_amount =float(total_amount)
tip_choice = input("How much tip you like to give? 10, 12, or 15?")
tip_choice = int(tip_choice)
number_guests = input ("How many people to split the bill")
number_guests =int (number_guests)

#caluculations
each_person = round((total_amount + (tip_choice*total_amount /100))/number_guests,2)
each_person =float(each_person)

#print the amount
print("The sheare of individual from group of ",number_guests,"is : $ ",each_person)