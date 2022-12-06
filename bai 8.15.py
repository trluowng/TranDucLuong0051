# Tính tổng các số nguyên nhập vào , chấm dứt khi nhập số 0
s=0
x= int(input('nhap so: '))
while(x!=0):
    s=s+x
    x= int(input('nhap so: '))
print('tong S: ',s)

