
def is_leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400 ==0:
                return 1
                #print("It's a leap year")
            else:
                return 0
                #print("It's not a leap year")
        else:
            return 1
            #print("It's a leap Year")
    else: 
        return 0
        #print("It's not a leap year")


def days_in_month(year,month):
    month_days =['31','28','31','30','31','30','31','31','30','31','30','31',]
    chkdays = month_days[month-1]
    chkyear = is_leapyear(year)
    if chkyear == 1:
        chkdays[1]==29
        print(f"It's a Leap year and days are {chkdays}")
    elif chkyear == 0:
        chkdays = month_days[month-1]
        print(f"It's not a Leap year and days are {chkdays}")

        
uyear=int(input("Enter the year you would like to check for Leap year: "))
umonth=int(input("Enter the number of the month you like to check the days: "))

days_in_month(uyear,umonth)