#defining function

def painting_wall(height, width, coverage):
    canvas_count= (height* width)/coverage
    return("You will need ", round(canvas_count,0), "can of paint!")

u_width = int(input("Enter a value for the widht of wall: "))
u_height = int(input("Enter a value for the height of the wall: "))
d_coverage = 5

print(painting_wall(height=u_height, width=u_width, coverage=d_coverage))