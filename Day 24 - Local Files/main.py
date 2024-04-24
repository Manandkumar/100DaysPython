from datetime import time, date

with open("./Day 24 - Local Files/my_file.txt","a") as data:
    local_time= date.month
    data.write(f" Time the file is opened: {local_time} \n")
    data.close()

file1 = open("my_file.txt","r")
text = file1.readlines()
print(text)
file1.close()