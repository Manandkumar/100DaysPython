#Fizz Buzz Program

print("Welcome to Fizz Buzz Program")
#take a number from User
numbers =int(input("Enter a number for the FizzBuzz Game: "))
#logic
for number in range(0,numbers+1):
    if number %3 ==0 and number %5==0:
        print("FizzBuzz")
    elif(number %3==0):
        print("Fizz")
    elif number %5==0:
        print("Buzz")
    else:
        print(number)
