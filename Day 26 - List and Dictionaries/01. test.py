with open("./Day 26 - List and Dictionaries/file1.txt") as fl:
    list1 = fl.readlines()

with open("./Day 26 - List and Dictionaries/file2.txt") as fl:
    list2 = fl.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)