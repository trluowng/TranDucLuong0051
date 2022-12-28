#nhập ma trận 
a=[]
m=int(input("m="))
n=int(input("n="))
for i in  range(m):
    print('nhaạp ma trận hàng thu',i+1,";")
    b=[]
    for j in range(n):
        x=int(input('nhập phần tử thú' +str(j+1)+";"))
        b=b+[x]
    a.append(b)
print("ma tran A da nhap xong!")
#in ma tran A ra man hinh
for i in range(m):
    for j in range(n):
        print(a[i] [j],end=" ")
    print()


