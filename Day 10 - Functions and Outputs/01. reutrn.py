# define functions

def capitalize(f_name,l_name):
    if f_name =="" or l_name =="":
        print("Didn't enter First name or Last name")
        return
    else:
        formated_fname=f_name.title()
        formated_lname=l_name.title()
        return f"{formated_fname} {formated_lname}"
   
    
    
# Welcome Message 

f_name= input(str("Enter your First Name: "))
l_name= input(str("Enter your First Name: "))

print(capitalize(f_name,l_name))

