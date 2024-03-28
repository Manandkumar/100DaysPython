# Py Password Generator 
print("Welcome to Password Generator")
import random

#configure the list
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*','(','_']

#take user preference
user_choice1 = int(input("How many letters do you like to be in password: "))
user_choice2 = int(input("How many numbers do you like to be in password: "))
user_choice3 = int(input("How many symbols do you like to be in password: "))

password = []
#logic
for user_choice01 in range(0,user_choice1):
    temp = random.randint(0,user_choice1)
    password+=letters[temp]
for user_choice02 in range(0,user_choice2):
    temp = random.randint(0,user_choice2)
    password+=numbers[temp]
for user_choice03 in range(0,user_choice3):
    temp = random.randint(0,user_choice3)
    password+=symbols[temp]
# shuffle password generated
random.shuffle(password)

final_password = ""
for char in password:
    final_password+=char
#print the final shuffled passowrd
print (f"The password generated for your use is {final_password}")