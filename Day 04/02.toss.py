# Heads and Tails - Programs
import random

toss= random.randint(0,1)
if toss == 0:
    result= "Tails"
else:
    result= "Heads"

print(f"The Toss is {result}")