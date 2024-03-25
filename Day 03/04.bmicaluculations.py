# Take user inputs for caluculating the user BMI
name= str(input("Enter your Name:"))
weight= float(input("Enter your weight in KGs:"))
height= float(input("Enter your height in Meters:"))

#BMI caluculation
caluculated_bmi= round((weight/(height**2)),2)

if caluculated_bmi <18.5:
    print (f"Hi {name} !, Your BMI is {caluculated_bmi} and you are under weight")
elif (caluculated_bmi >18.5) and (caluculated_bmi <25):
    print (f"Hi {name} !, Your BMI is {caluculated_bmi} and you are normal weight")
elif (caluculated_bmi >=25) and  (caluculated_bmi <30):
    print (f"Hi {name} !, Your BMI is {caluculated_bmi} and you are slighlty over weight")
elif (caluculated_bmi >=30) and  (caluculated_bmi <35):
    print (f"Hi {name} !, Your BMI is {caluculated_bmi} and you are Obese")
elif caluculated_bmi >=35:
    print (f"Hi {name} !, Your BMI is {caluculated_bmi} and you are clinically Obese")