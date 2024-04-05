# Modify Global Scope

enemies =1

def increase_enemies():
    enemies =2
    print(f"Value inside fucntion: {enemies}")

increase_enemies()
print(f"Value outside fucntion: {enemies}")

# naming convention in python for Global is always in upper case seperated with underscore