number =[1,2,3]
#list comprehension

new_list = [n+10 for n in number]

with open("./Day 26 - List and Dictionaries/file2.txt",'+a') as fl:
    fl.write(str(new_list))

print(new_list)