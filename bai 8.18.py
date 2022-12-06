#8.18
a= int(input('nhap so a: '))
i=1;s=0
while(i<a):
    if(a%i==0):
        s= s +i
    i+=1
if(a==s):
    print(a,' là số hoàn hảo')
else: print(a,' không là số hoàn hảo')