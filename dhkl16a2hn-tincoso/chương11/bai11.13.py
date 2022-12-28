print("Nhập END nếu muốn dừng")
set1=set()
set2=set()
while True:
    x=input("Nhập phần tử cho set 1:")
    if x =='END':
        break
    set1.add(int(x))
while True:
    y=input("Nhập phần tử cho set 2:")
    if y=='END':
        break
    set2.add(int(y))
print('set1:',set1)
print('set2:',set2)
#chieu dai va tong cua pha tu
print('1:',len(set1),'\n','2:',len(set2))
print('1:',sum(set1),'2:',sum(set2))
#MAX,MIN
print('max of set1',max(set1),'\n','min of set2',min(set1))
print('max of set1',max(set2),'\n','min of set2',min(set2))
#find
set11=set1.pop()
print(set11)
print(set1)
#union
set3=set1|set2
print(set3)
#intersection
set4=set1 &set2
print(set4)
#diference
set5=set1-set2
print(set5)
#symmetric diference
set6=set1^set2
print(set6)
#tang , giam
print(sorted(set1))
print(sorted(set2,reverse=True))
