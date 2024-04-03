# program for a simiple caluculator
def addition(a,b):
    return a+b
def substaction(a,b):
    return a-b
def multipliation(a,b):
    return a*b
def division(a,b):
    return a/b

#user input 
def calc():
    num1 = int(input("What's your first number: "))
    oper = str(input(" + \n - \n * \n / \n Pick an operation :"))
    num2 = int(input("What's your second number: "))
    should_continue =True
    while should_continue:
        if oper=='+':
            print(addition(num1,num2))
        if oper=='-':
            if num2 > num1:
                print(f"For the choosen operation ' {oper} ' the second number '{num2}' should be less than first")
            else:
                print(substaction(num1,num2))
        if oper=='*':
            print(multipliation(num1,num2))
        if oper=='/':
            if num2 > num1:
                print(f"For the choosen operation ' {oper} ' the second number '{num2}' should be less than first")
            else:
                print(division(num1,num2))
        repeatop= str(input("Do you want to try again? Y / N: "))
        if repeatop =='N':
            should_continue= False
        else:
            calc()

calc()
    