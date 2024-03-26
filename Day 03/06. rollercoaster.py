# Program from Nested If Statements
print ("Welcome to the Rollercoaster !")
#take necessary information from the user 
total_cost =0
def picprice(ride_cost):
    wantpicture = input("Do you like to have a pic along with the ride Y / N:")
    if wantpicture == 'Y':
        total_cost= 3+ride_cost
    elif wantpicture=='N':
        total_cost=ride_cost
    return(total_cost)

height=int(input("Whats your height in CM:"))

#condition check for the height
if height>=120:
    print(" Welcome to the Ride!! , Please proceed")
    rider_age= int(input("What's your age: "))
    if rider_age <= 12:
        ride_cost=5
        actul_cost=picprice(ride_cost)
        print(f"Please pay ${actul_cost} for the ride")
    elif rider_age<=18:
        ride_cost=7
        actul_cost=picprice(ride_cost)
        print(f"Please pay ${actul_cost} for the ride")
    else:
        ride_cost=12
        actul_cost=picprice(ride_cost)
        print(f"Please pay ${actul_cost} for the ride")
else:
    print("Sorry! your height dosen't match to the required height!!")

# code to add additional charge for the photo along with ride

