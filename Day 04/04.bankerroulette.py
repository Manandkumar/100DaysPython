# Banker Roulette Program 
import random
print("Welcome to Banker Roulette Program")

guests = input("Enter the names of people who all are having lunch / dinner together now \n Enter names seperated by comma:")

names =guests.split(",")
guests_count = len(names)
#choose who'll pay the bill
vip = int(random.randint(0,guests_count))
print(f"{names[vip]} will pay today's bill")

