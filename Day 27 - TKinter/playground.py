# Advance Aruguments
def add (*args):
    print(args[2])
    total = 0
    for n in args:
        total = total+n
    return total

def caluculate(**kwargs):
    print(kwargs)    
    print(kwargs["add"])

print(add(1,2,3,4,5))

caluculate(add =3, multiply=10 )

class Car:
    # def __init__(self,**kw):
    #     self.make=kw["make"]
    #     self.color=kw["color"]
    def __init__(self,**kw):
         self.make=kw.get("make")
         self.color=kw.get("color")


my_car = Car(make="Skoda")
print(my_car.color)


