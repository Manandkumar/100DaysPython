#creating a class
class User:
 #constructor is called initialization 
    def __init__(self,id,name):
        print("A new user is created!")
        self.id=id
        self.name=name
        self.follower =0
        self.following =0
    def add_followers(self,user):
        user.follower +=1
        self.following +=1


user_1= User("004","Anand")
user_2= User("005","Kumar")


print(f"First user ID is :{user_1.id}")
print(f"First user name is :{user_1.name}")
print(f"First user ID is :{user_2.id}")
print(f"First user name is :{user_2.name}")

user_1.add_followers(user_2)

print(f"{user_1.follower} - No of Followers for User 1 ")
print(f"{user_1.following} - No of Following for Useer 1")

print(f"{user_2.follower} - No of Followers for User 2")
print(f"{user_2.following} - No of Following for Useer 2")

