#Program to write highest score in a class
print ("Find Highest score in the class \n")
#take information of students
student_info = input ("Enter Marks of students in your class by seperating with , :")
#convert information to list 
marks =student_info.split(",")
numofstudents = len(marks)
#print num of students info
print(f" In the class there are {numofstudents} students")
best =0
# Core Logic
for mark in marks:
    mark =int(mark)
    if mark > best:
        best =mark

print(f" The Best score in all the student in your class is: {best} marks") 
