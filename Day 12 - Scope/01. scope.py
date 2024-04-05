#global scope
enemies =1 
def increase():
    enemies =2
    print(f"Value inside fucntion: {enemies}")
increase()
print(f"value of enemines outside function is {enemies}")

#Local Scope
def drink_potion():
   postion_strenght =2 #local scope of this variable
   print(postion_strenght)
drink_potion()
#print(portion_strenght) - wont' work as as variable has local scope