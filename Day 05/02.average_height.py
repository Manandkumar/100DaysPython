# program to find average student height in a class
print ("Find Average Height of Students in your class \n")
#take information of students
student_info = input ("Enter heights of students in your class by seperating with , :")
#convert information to list 
heights =student_info.split(",")
numofstudents = len(heights)
#print num of students info
print(f" In the class there are {numofstudents} students")
sum =0
# Core Logic
for height in heights:
    height =int(height)
    sum = sum + height
print(f" The Total sum of height is {sum} Meters")
avg_sum=round(sum/numofstudents,2)
print(f" The Average heigh of the student in your class is: {avg_sum} Meters") 
