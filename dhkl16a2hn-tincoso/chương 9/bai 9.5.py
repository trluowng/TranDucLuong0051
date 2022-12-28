import math
def S(x,y):
    A=math.pow(math.pow(x,2)+x+1,y)+math.pow(math.pow(x,2)-x+1,y)
    return A
print("A=",S(2,2))