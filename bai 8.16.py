# tìm UCLN(a,b)
a= int(input('nhap so a: '))
b= int(input('nhap so b: '))
i=0; x=0
c= a
if (b>a): c =b
while (i<=c):
    i+=1
    if(a%i==0): 
        if(b%i==0):
            x= i
print('UCLN của ',a,' và ',b,' là: ',x)
    