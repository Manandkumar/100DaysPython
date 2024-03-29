# define function to check prime number 
def prime_number(number):
    is_prime = True
    for i in range (2,number):
        if number %i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

#user input
u_number = int(input("Enter a number to check if it's a prime number: "))

#print the result 
prime_number(u_number)