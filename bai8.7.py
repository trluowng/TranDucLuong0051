#tính tiền điện
n=eval(input("số kWh:"))
if n<=50:
    print("số tiên phải tra là:",n*1.678)
elif n<=100:
    print("số tiền phải trả là:",n*1.734)  
elif n<=200:
    print("số tiền phải trả là:",n*2.014)
elif n<=300:
    print("số tiền phải trả là:",n*2.536)
elif n<=400:
    print("số tiền phải trả là:",n*2.834)  
else:
    print("số tiền cần phải trả:",n*2.937)