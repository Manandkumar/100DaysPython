# Program for using Range in Loop 
total = 0
#take user input
range_out = int(input("Please enter a number for the max range [only upto 1000]: "))
if(range_out <=1000):
    for number in range (0,range_out +1,2):
        total +=number
print (f"The total of the even numbers in the range you have given is : {total}")