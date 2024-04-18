class Animal:
    def __init__(self):
        self.num_eyes =2
    def breathe(self):
        print("Inhale , Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print ("Moving in water")
    
    def breathe(self):
        super().breathe()
        print ("Doing this under water...")

nemo = Fish()
nemo.swim()
nemo.breathe()