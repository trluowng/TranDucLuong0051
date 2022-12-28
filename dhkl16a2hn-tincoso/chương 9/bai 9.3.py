import math
weight=float(input("weight:"))
height=float(input("height:"))
def tinh_BMI(w,h):
    return w/(pow(h,2))
print("BMI:",tinh_BMI(weight,height))
x=tinh_BMI(weight,height)
if x<18.5:
    print("gầy")
elif x>=25:
    print("béo")
else:
    print("bình thường") 