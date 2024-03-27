# Love Caluculator Program
print ("Welcome to Love Caluculator")
# Take Names 
name1 = str(input("Enter the First Name: "))
name2 = str(input("Enter the Second Name: "))
#combined names
combined_names = name1+name2
#convert to lowercase
lower_names = combined_names.lower()
#count the first half - True
t= lower_names.count("t")
r= lower_names.count("r")
u= lower_names.count("u")
e= lower_names.count("e")
first_half = t+r+u+e
#count the second half - Love
l= lower_names.count("l")
o= lower_names.count("o")
v= lower_names.count("v")
e= lower_names.count("e")

second_half=l+o+v+e

# Final score
score = int(str(first_half)+str(second_half))
print(f"The love score for {name1} and {name2} is {score} % ")