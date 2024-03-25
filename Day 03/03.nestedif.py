# Program from Nested If Statements
print ("Welcome to the Rollercoaster !")
#take necessary information from the user 


height=int(input ("Whats your height in CM: "))

#condition check for the height
if height>=120:
    print(" Welcome to the Ride!! , Please proceed")
    rider_age= int(input("What's your age: "))
    if rider_age <= 12:
        print("Please pay $5 for the ride")
    elif rider_age<=18:
        print("Please pay $7 for the ride")
    else:
        print("Please pay $12 for the ride")
else:
    print("Sorry! your height dosen't match to the required height!!")
