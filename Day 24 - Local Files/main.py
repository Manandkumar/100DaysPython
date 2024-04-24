with open("../my_file.txt",mode="a") as file :
    contents = file.read
    print(contents)
    file.write("Anand Kumar ")

file.close()