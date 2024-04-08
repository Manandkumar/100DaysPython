#creating a class
class User:
 #constructor is called initialization 
    def __init__(self,id,name):
        print("A new user is created!")
        self.id=id
        self.name=name
    pass

user_1= User("004","Anand")
user_2= User("005","Kumar")

print(f"First user ID is :{user_1.id}")
print(f"First user name is :{user_1.name}")
print(f"First user ID is :{user_2.id}")
print(f"First user name is :{user_2.name}")