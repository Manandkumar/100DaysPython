# Take user inputs for caluculating the user BMI
name= input()
weight= input()
height= input()

#convert the values 

weight =float(weight)
height =float(height)

#BMI caluculation

caluculagted_bmi= (weight/(height**2))

print("Your BMI is: ",caluculagted_bmi)