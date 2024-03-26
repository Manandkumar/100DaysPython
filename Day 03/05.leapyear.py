# Find a Leap Year 
print("Leap Year Program")
#take user inputs
year = int (input ("Please Enter a year to find if it's a Leap year:"))

if year%4==0:
    if year%100==0:
        if year%400 ==0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap Year")
else: 
    print("It's not a leap year")
