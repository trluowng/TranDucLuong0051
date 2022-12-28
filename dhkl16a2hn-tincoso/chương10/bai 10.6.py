import math
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
delta=pow(b,2)-4*a*c
if delta >0:
    print ("phương trình có 2 nghiệm pb!")
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("x1=",x1,"\n","x2=",x2)
elif delta==0:
    print('phương trình có nghiệm kép!')
    x1=x2=-b/(2*a)
    print("x1=x2=",x1)
else:
    print("phương trình vô nghiệm")

