#program to caluculate number of weeks left in life, it they leave for 90 years 

#Take user age
current_age= input("Please enter your age:")
#conver the age to integer
age=int(current_age)

#caluculation
life_span= 90-age
weeks_left=life_span*52
print ("Life left for you is Weeks.",weeks_left)