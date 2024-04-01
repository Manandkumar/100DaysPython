# student dictionary

student_scores ={
    "Anand" :60,
    "Kumar" :85,
    "Ahaan" :99,
    "Mitul":62,
}

# student grades 
student_grades={}

for student in student_scores:
    score = student_scores[student]
    if score >90:
        student_grades[student] ="Outstanding"
    if score >=80 and score<90:
        student_grades[student] ="Exceeds Expectations"
    if score >=70 and score<80:
        student_grades[student] ="Acceptable"
    else: 
        student_grades[student] ="Fail"

#logic

for student in student_grades:
    score = student_scores[student]

print (student_grades)