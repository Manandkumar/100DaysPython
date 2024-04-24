from datetime import time, date

with open("./Day 24 - Local Files/my_file.txt","a") as data:
    local_time= str(date.day)
    data.write(f" Time the file is opened: {local_time} \n")
    data.close()

file1 = open("./Day 24 - Local Files/my_file.txt","r")
text = file1.read()
print(text)
file1.close()