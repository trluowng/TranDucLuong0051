numbers=[1,2,3,4,5,6,7,8]
types=["standard",'superior garden view',"superior ocean view","garden  view bungalow","pool view bungalow","family room","beach front bungalow","VIP sea view"]
for index in range(len(numbers)):
    print("type["+str(index)+"] is "+ types[index])
n=int(input('type room:'))
m=int(input("number of night to rent:"))
if n==1:
    cost=1.260
elif n==2:
    cost=1.550
elif n==3:
    cost=1.830
elif n==4:
    cost=1.830
elif n==5:
    cost=2.120
elif n==6:
    cost=2.120
elif n==7:
    cost=2.540
elif n==8:
    cost=4.800
else:
    print("Room types errol!")
# tính tổng số tieèn phải thanh toán
TotalPrice1 =cost
TotalPrice2=cost *m*0.75
TotalPrice3=cost*m*0.7
if m==1:
    print("Total Price:",TotalPrice1)
elif m<=3:
    print("Total Price:",TotalPrice2)
else:
    print("Total Price:",TotalPrice3)