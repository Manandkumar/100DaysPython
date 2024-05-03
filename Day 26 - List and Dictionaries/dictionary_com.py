import random
parent =["father", "mother", "child", "GrandFather", "GrandMother"]
new_dict ={item:random.randint(1,100) for item in parent}
print(new_dict)