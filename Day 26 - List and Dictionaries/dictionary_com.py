import random
parent =["father", "mother", "child", "GrandFather", "GrandMother"]
new_dict ={item:random.randint(1,100) for item in parent}

with open("./Day 26 - List and Dictionaries/file1.txt","a+") as fl:
    fl.write(str(new_dict))
    print(new_dict)