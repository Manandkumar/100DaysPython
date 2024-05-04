student_disc ={
    "student":["anand","Ahaan","Mitul"],
    "score":[56,78,99]

}
for (key,value) in student_disc.items():
    print(value)

import pandas
student_dataframe= pandas.DataFrame(student_disc)
print(student_dataframe)
#loop through

for (key,value) in student_dataframe.items():
    print(value)

for(index, row)in student_dataframe.iterrows():
    print(row)